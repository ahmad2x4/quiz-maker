# Claude Code Skills for Quiz Maker

This directory contains Claude Code Skills that automatically generate math quizzes from PDF documents.

## What are Skills?

Skills are modular capabilities that Claude Code invokes automatically based on your requests. Unlike slash commands (which you manually trigger), Skills activate when Claude determines they're relevant to your task.

## Available Skills

### 1. **pdf-quiz-generator**
Analyzes PDFs and generates quiz questions.

**Triggers when you:**
- Upload a PDF and ask to create a quiz
- Mention generating questions from textbooks or study materials

**What it does:**
- Extracts text and formulas from PDFs
- Generates high-quality quiz questions
- Ensures proper LaTeX formatting
- Creates multiple question types (MC, T/F, numeric, interactive)

### 2. **math-visualizer**
Creates mathematical visualizations and interactive graphs.

**Triggers when:**
- Questions need visual aids
- You request graphs or geometric diagrams
- Questions involve function plotting

**What it creates:**
- Interactive Mafs.js graph configurations
- Static PNG/SVG images using matplotlib
- Geometric diagrams
- Mermaid flowcharts

### 3. **quiz-compiler**
Assembles questions and assets into formatted markdown files.

**Triggers when:**
- Questions are ready to be saved
- You want to finalize a quiz

**What it does:**
- Validates questions and LaTeX formulas
- Organizes visual assets
- Generates markdown with YAML frontmatter
- Creates collapsible explanation sections

## Usage Example

Simply upload a PDF and ask:

```
"Create a quiz from this algebra textbook chapter.
Generate 10 questions with mixed difficulty covering linear equations."
```

Claude will automatically:
1. Use `pdf-quiz-generator` to extract content and create questions
2. Use `math-visualizer` to generate any needed graphs
3. Use `quiz-compiler` to save the final quiz markdown

The quiz will be saved to `quizzes/[topic]/[quiz-name]/quiz.md`

## Python Dependencies

Skills use Python scripts for PDF processing and visualization:

```bash
pip install -r ../scripts/requirements.txt
```

Required packages:
- `pdfplumber` - PDF extraction
- `matplotlib` - Graph generation
- `numpy` - Math operations
- `pillow` - Image processing

## Modifying Skills

Each skill has a `SKILL.md` file that defines its behavior:

1. **Edit SKILL.md** - Change instructions and workflows
2. **Update scripts/** - Modify helper Python scripts
3. **Test** - Upload a PDF and request a quiz
4. **Commit** - Skills are version-controlled

## Best Practices

- **Specific descriptions**: Help Claude know when to activate the skill
- **Clear instructions**: Step-by-step workflows in SKILL.md
- **Progressive disclosure**: Keep main SKILL.md concise, use reference files for details
- **Error handling**: Provide fallbacks if scripts fail

## Learn More

- [Claude Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- Project CLAUDE.md for full architecture details
