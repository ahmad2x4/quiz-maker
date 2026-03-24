"""
Question Generator Agent
Generates quiz questions using Claude API based on extracted PDF content.
"""

import os
import json
from typing import Dict, List, Optional
from anthropic import Anthropic
from dotenv import load_dotenv


class QuestionGenerator:
    """Generates quiz questions using Claude API."""

    def __init__(self, config: Dict):
        self.config = config
        self.api_config = config.get('api', {})
        self.defaults = config.get('defaults', {})

        # Load API key from environment
        load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
        api_key = os.getenv('ANTHROPIC_API_KEY')

        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. "
                "Please set it in scripts/.env file"
            )

        self.client = Anthropic(api_key=api_key)

    def generate_questions(
        self,
        content: str,
        user_prompt: str,
        topic: str,
        num_questions: Optional[int] = None,
        difficulty_mix: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Generate quiz questions from content.

        Args:
            content: Extracted text from PDF
            user_prompt: User's custom instructions
            topic: Math topic (algebra, geometry, etc.)
            num_questions: Number of questions to generate
            difficulty_mix: Distribution of difficulty levels

        Returns:
            List of question dictionaries
        """
        if num_questions is None:
            num_questions = self.defaults.get('questions_per_quiz', 10)

        if difficulty_mix is None:
            difficulty_mix = self.defaults.get('difficulty_distribution', {})

        # Build the prompt for Claude
        system_prompt = self._build_system_prompt()
        user_message = self._build_user_message(
            content, user_prompt, topic, num_questions, difficulty_mix
        )

        # Call Claude API
        print("Calling Claude API to generate questions...")
        response = self.client.messages.create(
            model=self.api_config.get('model', 'claude-sonnet-4-5-20250929'),
            max_tokens=self.api_config.get('max_tokens', 8192),
            temperature=self.api_config.get('temperature', 0.7),
            system=system_prompt,
            messages=[{
                'role': 'user',
                'content': user_message
            }]
        )

        # Parse the response
        questions = self._parse_response(response.content[0].text)

        print(f"Generated {len(questions)} questions")
        return questions

    def _build_system_prompt(self) -> str:
        """Build the system prompt for Claude."""
        return """You are an expert mathematics educator creating high-quality quiz questions for high school students.

Your task is to generate quiz questions based on provided content. Each question should:
- Be clear, precise, and appropriate for high school level
- Include proper LaTeX formatting for mathematical expressions (use $ for inline, $$ for display)
- Have accurate answers and detailed explanations
- Include difficulty level and topic classification
- For graph-based questions, provide configuration for visualization

Output format: Return a JSON array of questions with this structure:
```json
[
  {
    "id": "unique-id",
    "type": "multiple-choice | true-false | numeric | graph-interactive",
    "topic": "algebra | geometry | trigonometry | calculus | statistics | functions",
    "difficulty": "easy | medium | hard",
    "question": "Question text with $LaTeX$ formulas",
    "formula": "Main formula if applicable (LaTeX)",
    "options": ["A) option1", "B) option2", "C) option3", "D) option4"],
    "correctAnswer": 1,
    "explanation": "Detailed explanation with step-by-step solution",
    "points": 10,
    "graphConfig": {
      "type": "cartesian | polar | geometry",
      "xRange": [-10, 10],
      "yRange": [-10, 10],
      "functions": ["f(x) = x^2"],
      "shapes": [{"type": "point", "points": [[0,0]], "label": "A"}]
    },
    "visualAssets": {
      "needsDiagram": true,
      "diagramType": "graph | geometry | flowchart | table",
      "description": "Description of visual needed"
    }
  }
]
```

Guidelines:
- For multiple-choice: correctAnswer is the index (0-based)
- For true-false: correctAnswer is boolean
- For numeric: correctAnswer is the number
- Only include graphConfig for graph-interactive questions
- Use visualAssets to indicate if diagrams should be generated
- Ensure LaTeX syntax is valid for KaTeX rendering
- Vary question types and difficulty according to requested distribution
"""

    def _build_user_message(
        self,
        content: str,
        user_prompt: str,
        topic: str,
        num_questions: int,
        difficulty_mix: Dict
    ) -> str:
        """Build the user message with content and instructions."""

        # Calculate target counts for each difficulty
        difficulty_counts = {
            level: int(num_questions * ratio)
            for level, ratio in difficulty_mix.items()
        }

        # Adjust for rounding
        total = sum(difficulty_counts.values())
        if total < num_questions:
            difficulty_counts['medium'] += (num_questions - total)

        message = f"""Content from PDF:

{content[:8000]}  # Truncate if too long

---

Topic: {topic}
Number of questions: {num_questions}
Difficulty distribution: {difficulty_counts}

User instructions:
{user_prompt}

Please generate {num_questions} high-quality quiz questions based on this content.
Ensure the questions cover the key concepts and follow the specified difficulty distribution.
Return ONLY the JSON array, no additional text."""

        return message

    def _parse_response(self, response_text: str) -> List[Dict]:
        """Parse Claude's response into question dictionaries."""
        try:
            # Try to extract JSON from response
            # Look for JSON array in the response
            json_start = response_text.find('[')
            json_end = response_text.rfind(']') + 1

            if json_start == -1 or json_end == 0:
                raise ValueError("No JSON array found in response")

            json_text = response_text[json_start:json_end]
            questions = json.loads(json_text)

            # Validate and clean up questions
            validated_questions = []
            for q in questions:
                validated = self._validate_question(q)
                if validated:
                    validated_questions.append(validated)

            return validated_questions

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print("Response text:", response_text[:500])
            return []

    def _validate_question(self, question: Dict) -> Optional[Dict]:
        """Validate and clean up a question."""
        required_fields = ['type', 'topic', 'difficulty', 'question', 'correctAnswer', 'explanation']

        for field in required_fields:
            if field not in question:
                print(f"Warning: Question missing required field '{field}'")
                return None

        # Set defaults
        if 'id' not in question:
            import uuid
            question['id'] = str(uuid.uuid4())[:8]

        if 'points' not in question:
            difficulty_points = {'easy': 5, 'medium': 10, 'hard': 15}
            question['points'] = difficulty_points.get(question['difficulty'], 10)

        # Validate question type
        valid_types = ['multiple-choice', 'true-false', 'numeric', 'graph-interactive']
        if question['type'] not in valid_types:
            print(f"Warning: Invalid question type '{question['type']}'")
            return None

        return question


def main():
    """Test the question generator."""
    import yaml
    from pathlib import Path

    # Load config
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path) as f:
        config = yaml.safe_load(f)

    # Example usage
    generator = QuestionGenerator(config)

    sample_content = """
    Linear Equations

    A linear equation is an equation of the form ax + b = c, where a, b, and c are constants.

    Example: Solve 2x + 5 = 13
    Solution:
    - Subtract 5 from both sides: 2x = 8
    - Divide both sides by 2: x = 4
    """

    questions = generator.generate_questions(
        content=sample_content,
        user_prompt="Create questions that test understanding of solving linear equations",
        topic="algebra",
        num_questions=3
    )

    print(json.dumps(questions, indent=2))


if __name__ == '__main__':
    main()
