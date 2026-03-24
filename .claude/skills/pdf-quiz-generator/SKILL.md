---
name: pdf-quiz-generator
description: Generates high-quality math quiz questions from PDF files (textbooks, worksheets, study materials). Use when the user wants to create a quiz from a PDF document or mentions uploading educational materials.
---

# PDF Quiz Generator

This skill helps you generate high-quality math quiz questions for high school students based on PDF content.

## When to Use

Activate this skill when:
- User uploads a PDF file and asks to create a quiz
- User mentions generating questions from textbook chapters, worksheets, or study materials
- User wants to extract math problems from educational PDFs
- User asks to analyze PDF content for quiz creation

## Workflow

### 1. PDF Analysis
First, extract and analyze the PDF content:

```bash
# Use pdfplumber or PyPDF2 to extract text
python .claude/skills/pdf-quiz-generator/scripts/analyze_pdf.py <pdf_path>
```

Extract:
- Text content from all pages
- Mathematical formulas (LaTeX format if present)
- Images and diagrams
- Section structure (chapters, topics, examples)

### 2. Content Understanding
Review the extracted content to identify:
- Main mathematical topics covered (algebra, geometry, trigonometry, etc.)
- Difficulty level of material
- Examples and worked problems
- Key concepts and formulas

### 3. Question Generation
Generate quiz questions following this structure:

**Question Types:**
- **Multiple Choice** (60%): 4 options, one correct answer
- **True/False** (20%): Binary choice with explanation
- **Numeric** (10%): Calculate and enter a number
- **Graph Interactive** (10%): Visualize or interact with graphs

**Difficulty Distribution:**
- Easy: 30% (basic recall and simple application)
- Medium: 50% (multi-step problems, moderate reasoning)
- Hard: 20% (complex problems, deep understanding)

**Quality Criteria:**
- Clear, unambiguous question text
- Proper LaTeX formatting for all math expressions
- Accurate and detailed explanations
- Age-appropriate for high school students
- Cover diverse concepts from the PDF

### 4. Output Format
Generate questions in JSON format that will be compiled into markdown:

```json
{
  "id": "unique-id",
  "type": "multiple-choice",
  "topic": "algebra",
  "difficulty": "medium",
  "question": "Solve for $x$: $2x + 5 = 13$",
  "formula": "2x + 5 = 13",
  "options": ["A) $x = 3$", "B) $x = 4$", "C) $x = 8$", "D) $x = 9$"],
  "correctAnswer": 1,
  "explanation": "Subtract 5 from both sides: $2x = 8$, then divide by 2: $x = 4$",
  "points": 10,
  "graphConfig": null,
  "visualAssets": {
    "needsDiagram": false
  }
}
```

### 5. Visual Assets
For questions requiring visualizations, indicate in `visualAssets`:

```json
"visualAssets": {
  "needsDiagram": true,
  "diagramType": "graph",
  "description": "Graph of y = 2x + 5 showing the solution point"
}
```

The math-visualizer skill will handle creating these assets.

## LaTeX Guidelines

- Use `$...$` for inline math: `$x^2 + 1$`
- Use `$$...$$` for display math: `$$\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$$`
- Escape backslashes in JSON strings: `"\\frac{1}{2}"`
- Validate LaTeX is KaTeX-compatible (see: https://katex.org/docs/supported.html)

## Common Math Topics

- **Algebra**: Linear equations, quadratic equations, polynomials, systems of equations
- **Geometry**: Angles, triangles, circles, polygons, area, volume
- **Trigonometry**: Sine, cosine, tangent, unit circle, identities
- **Calculus**: Limits, derivatives, integrals, related rates
- **Statistics**: Mean, median, mode, probability, standard deviation
- **Functions**: Domain, range, transformations, composition

## Best Practices

1. **Extract thoroughly**: Read entire PDF to understand context
2. **Vary question types**: Don't create all multiple choice
3. **Provide detailed explanations**: Help students learn from mistakes
4. **Check formula accuracy**: Validate all mathematical expressions
5. **Consider prerequisite knowledge**: Match high school curriculum
6. **Cite PDF sections**: Reference where content came from
7. **Generate 8-15 questions**: Enough for a meaningful quiz

## Error Handling

If PDF cannot be read:
- Check if file is encrypted or password-protected
- Try alternative PDF libraries (PyPDF2, pdfplumber, pymupdf)
- Ask user to provide plain text if extraction fails

If formulas are unclear:
- Use OCR or manual interpretation
- Ask user to clarify mathematical notation
- Default to standard LaTeX conventions

## Supporting Scripts

- `scripts/analyze_pdf.py`: Extract and analyze PDF content
- `templates/question_template.json`: JSON schema for questions
- `templates/quiz_metadata.yaml`: YAML frontmatter template
