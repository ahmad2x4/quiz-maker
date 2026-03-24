---
name: quiz-compiler
description: Compiles quiz questions into properly formatted markdown files with YAML frontmatter, organizes assets, and prepares quizzes for the React frontend. Use after generating questions and visual assets to assemble the final quiz files.
---

# Quiz Compiler

This skill assembles generated quiz questions, visual assets, and metadata into well-structured markdown files ready for the React frontend to consume.

## When to Use

Activate this skill when:
- Quiz questions have been generated and need to be compiled
- Visual assets are ready and need to be integrated
- User wants to finalize and save a quiz
- Need to organize quiz files in the proper folder structure
- Updating or modifying existing quiz files

## Output Structure

Each quiz is stored as:

```
quizzes/[topic]/[quiz-name]/
├── quiz.md                 # Main quiz file with frontmatter
├── graph-001.png           # Visual assets
├── mafs-config-001.json    # Mafs.js configurations
└── diagram-001.svg         # SVG diagrams
```

## Markdown Quiz Format

### YAML Frontmatter
Every quiz.md must start with YAML frontmatter:

```yaml
---
id: algebra-linear-equations-001
title: "Linear Equations Practice"
topic: algebra
difficulty: medium
questionCount: 10
createdFrom: "textbook-chapter-3.pdf"
dateGenerated: "2025-11-02"
estimatedTime: 15
tags: ["linear-equations", "solving", "variables"]
---
```

### Required Fields
- `id`: Unique identifier (kebab-case)
- `title`: Human-readable quiz title
- `topic`: One of: algebra, geometry, trigonometry, calculus, statistics, functions
- `difficulty`: easy, medium, or hard
- `questionCount`: Number of questions
- `dateGenerated`: ISO date string

### Optional Fields
- `createdFrom`: Source PDF filename
- `estimatedTime`: Minutes to complete
- `tags`: Array of relevant keywords
- `description`: Brief description of quiz content
- `prerequisites`: Topics students should know first

## Question Markdown Format

Each question follows this structure:

```markdown
## Question 1

**Topic:** Algebra • **Difficulty:** Medium • **Points:** 10

Solve for $x$: $2x + 5 = 13$

![Diagram](./linear-equations/graph-001.png)

**Options:**
- A) $x = 3$
- B) $x = 4$ ✓
- C) $x = 8$
- D) $x = 9$

<details>
<summary>Show Explanation</summary>

### Solution

Step 1: Subtract 5 from both sides
$$2x + 5 - 5 = 13 - 5$$
$$2x = 8$$

Step 2: Divide both sides by 2
$$x = \frac{8}{2} = 4$$

Therefore, $x = 4$ (Option B).

</details>

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": {"x": [-5, 15], "y": [0, 20]},
  "elements": [
    {
      "type": "plot",
      "function": "x => 2*x + 5",
      "color": "#3b82f6",
      "label": "y = 2x + 5"
    },
    {
      "type": "line",
      "point1": [-5, 13],
      "point2": [15, 13],
      "color": "#ef4444",
      "style": "dashed",
      "label": "y = 13"
    },
    {
      "type": "point",
      "coordinates": [4, 13],
      "label": "Solution",
      "color": "#10b981"
    }
  ]
}
```

---
```

## Compilation Workflow

### Step 1: Validate Questions
Check that each question has:
- Valid type (multiple-choice, true-false, numeric, graph-interactive)
- Proper LaTeX formatting
- Correct answer specified
- Detailed explanation
- Appropriate difficulty level

### Step 2: Organize Assets
Move visual assets to quiz folder:

```python
import shutil
from pathlib import Path

quiz_dir = Path(f"quizzes/{topic}/{quiz_name}")
quiz_dir.mkdir(parents=True, exist_ok=True)

# Move images
shutil.move("temp/graph-001.png", quiz_dir / "graph-001.png")

# Move Mafs configs
shutil.move("temp/mafs-config-001.json", quiz_dir / "mafs-config-001.json")
```

### Step 3: Build Frontmatter
Generate YAML from quiz metadata:

```python
import yaml
from datetime import datetime

frontmatter = {
    "id": generate_id(title, topic),
    "title": title,
    "topic": topic,
    "difficulty": calculate_overall_difficulty(questions),
    "questionCount": len(questions),
    "createdFrom": source_pdf_name,
    "dateGenerated": datetime.now().isoformat()[:10],
    "estimatedTime": estimate_time(questions),
    "tags": extract_tags(questions)
}

yaml_str = yaml.dump(frontmatter, default_flow_style=False)
```

### Step 4: Format Questions
Convert JSON questions to markdown:

```python
def format_question(q, index):
    md = f"## Question {index}\n\n"
    md += f"**Topic:** {q['topic'].title()} • "
    md += f"**Difficulty:** {q['difficulty'].title()} • "
    md += f"**Points:** {q['points']}\n\n"
    md += f"{q['question']}\n\n"

    # Add visual assets if present
    if q.get('visualAssets', {}).get('imagePath'):
        md += f"![Diagram](./{quiz_name}/{q['visualAssets']['imagePath']})\n\n"

    # Add options for MC questions
    if q['type'] == 'multiple-choice':
        md += "**Options:**\n"
        for i, option in enumerate(q['options']):
            check = " ✓" if i == q['correctAnswer'] else ""
            md += f"- {option}{check}\n"
        md += "\n"

    # Add explanation in details/summary
    md += "<details>\n<summary>Show Explanation</summary>\n\n"
    md += "### Solution\n\n"
    md += f"{q['explanation']}\n\n"
    md += "</details>\n\n"

    # Add Mafs config if present
    if q.get('graphConfig'):
        md += "**Interactive Graph:**\n"
        md += "```json:mafs\n"
        md += json.dumps(q['graphConfig'], indent=2)
        md += "\n```\n\n"

    md += "---\n\n"
    return md
```

### Step 5: Assemble Final File
Combine frontmatter and questions:

```python
def compile_quiz(frontmatter, questions, quiz_name):
    content = "---\n"
    content += yaml.dump(frontmatter, default_flow_style=False)
    content += "---\n\n"
    content += f"# {frontmatter['title']}\n\n"

    for i, question in enumerate(questions, start=1):
        content += format_question(question, i)

    return content
```

### Step 6: Save to File
Write to appropriate topic folder:

```python
quiz_path = Path(f"quizzes/{topic}/{quiz_name}/quiz.md")
quiz_path.parent.mkdir(parents=True, exist_ok=True)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(compiled_content)

print(f"Quiz saved to: {quiz_path}")
```

### Step 7: Update Quiz Index
Add entry to index for frontend:

```python
# This will be handled by the Node.js script later
# Just ensure the quiz is in the right location
```

## Helper Functions

### Generate ID
```python
def generate_id(title, topic):
    # Convert title to kebab-case
    id_base = title.lower().replace(' ', '-')
    # Remove special characters
    id_base = ''.join(c for c in id_base if c.isalnum() or c == '-')
    # Add topic prefix
    return f"{topic}-{id_base}"
```

### Calculate Difficulty
```python
def calculate_overall_difficulty(questions):
    difficulty_scores = {
        'easy': 1,
        'medium': 2,
        'hard': 3
    }
    avg = sum(difficulty_scores[q['difficulty']] for q in questions) / len(questions)

    if avg < 1.5:
        return 'easy'
    elif avg < 2.5:
        return 'medium'
    else:
        return 'hard'
```

### Estimate Time
```python
def estimate_time(questions):
    # Rough estimates in minutes
    time_per_type = {
        'multiple-choice': 1,
        'true-false': 0.5,
        'numeric': 1.5,
        'graph-interactive': 2
    }

    total = sum(time_per_type.get(q['type'], 1) for q in questions)
    return int(total)
```

### Extract Tags
```python
def extract_tags(questions):
    tags = set()

    # Add difficulty-specific tags
    for q in questions:
        # Add topic-specific keywords
        if q['topic'] == 'algebra':
            if 'quadratic' in q['question'].lower():
                tags.add('quadratic')
            if 'linear' in q['question'].lower():
                tags.add('linear-equations')
        # ... more topic-specific logic

    return sorted(list(tags))
```

## Quality Checks

Before saving, verify:
- [ ] All LaTeX formulas use proper delimiters ($..$ or $$..$$)
- [ ] Image paths are relative and correct
- [ ] Mafs configs are valid JSON
- [ ] All questions have explanations
- [ ] Frontmatter has all required fields
- [ ] File paths use forward slashes (not backslashes)
- [ ] No sensitive information in content
- [ ] Quiz ID is unique

## Error Handling

If compilation fails:
- Log specific errors with question numbers
- Create partial quiz with working questions
- Save problematic questions to separate file for review
- Validate JSON before embedding in markdown
- Check file permissions before writing

## Supporting Scripts

- `scripts/compile.py`: Main compilation script
- `templates/quiz_template.md`: Base template
- `templates/frontmatter_schema.yaml`: Frontmatter validation
