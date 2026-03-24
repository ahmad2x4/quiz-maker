# Getting Started with Quiz Maker

This guide will help you set up and start using the Math Quiz Maker application.

## Quick Start

### 1. Install Dependencies

```bash
# Install Node.js dependencies
npm install

# Install Python dependencies (for Skills)
pip install -r scripts/requirements.txt
```

### 2. Start Development Server

```bash
npm run dev
```

Visit http://localhost:5173 to see the quiz browser.

### 3. Create Your First Quiz from PDF

1. Find a math textbook PDF or worksheet
2. In Claude Code, upload the PDF
3. Ask Claude to create a quiz:

```
Create a quiz from this PDF about [topic].
Generate 10 questions with mixed difficulty.
```

Claude will automatically:
- Extract content using the `pdf-quiz-generator` skill
- Generate questions with proper LaTeX formatting
- Create visualizations if needed using `math-visualizer`
- Compile everything into markdown using `quiz-compiler`

### 4. View Your Quiz

The quiz is saved to `quizzes/[topic]/[quiz-name]/quiz.md`

Rebuild the quiz index:
```bash
npm run generate-quiz-index
```

Refresh your browser to see the new quiz in the browser!

## Project Structure

```
quiz-maker/
├── .claude/skills/          # Claude Code Skills (auto-invoked)
│   ├── pdf-quiz-generator/  # PDF analysis and question generation
│   ├── math-visualizer/     # Graph and diagram creation
│   └── quiz-compiler/       # Markdown assembly
├── quizzes/                 # Generated quizzes (organized by topic)
├── src/
│   ├── components/quiz/     # React components
│   └── data/quizIndex.ts    # Auto-generated quiz metadata
└── scripts/                 # Build and generation scripts
```

## Key Features

### Claude Code Skills
- **Automatic activation**: Just upload a PDF and ask for a quiz
- **No API keys needed**: Skills use Claude Code's built-in capabilities
- **Customizable**: Edit `.claude/skills/*/SKILL.md` to change behavior

### Math Rendering
- **LaTeX formulas**: Rendered with KaTeX for crisp display
- **Interactive graphs**: Using Mafs.js for Cartesian/polar plots
- **Geometric shapes**: Circles, polygons, vectors, and more

### Quiz Format
- **Markdown-based**: Easy to read and edit
- **YAML frontmatter**: Rich metadata (topic, difficulty, tags)
- **Visual assets**: PNG/SVG images and JSON graph configs

## Common Tasks

### Generate Quiz Index
After adding or modifying quizzes:
```bash
npm run generate-quiz-index
```

### Add a New Topic
1. Create directory: `quizzes/[new-topic]/`
2. Update `scripts/generateQuizIndex.js` TOPICS array
3. Update `src/data/quizIndex.ts` topics constant
4. Add topic color in `QuizBrowser.tsx`

### Modify a Quiz
1. Edit `quizzes/[topic]/[quiz-name]/quiz.md`
2. Run `npm run generate-quiz-index`
3. Refresh browser

### Create Graph Manually
```bash
python .claude/skills/math-visualizer/scripts/create_graph.py \
  --function "x**2" \
  --xrange -5 5 \
  --output quizzes/algebra/my-quiz/graph.png
```

## Example: Creating a Linear Equations Quiz

**Step 1:** Upload a textbook PDF

**Step 2:** Ask Claude:
```
Create a quiz from this chapter on linear equations.
Generate 8 questions:
- 3 easy (one-step equations)
- 4 medium (two-step equations)
- 1 hard (equations with fractions)

Include a graph for the hardest question.
```

**Step 3:** Claude uses Skills automatically:
- Analyzes PDF content
- Generates 8 questions with LaTeX formulas
- Creates a graph showing the solution
- Saves to `quizzes/algebra/linear-equations-practice/quiz.md`

**Step 4:** Rebuild and view:
```bash
npm run generate-quiz-index
# Refresh browser
```

## Troubleshooting

**PDF won't extract:**
- Check if PDF is encrypted
- Ensure `pdfplumber` is installed: `pip install pdfplumber`

**Formulas not rendering:**
- Verify LaTeX syntax at https://katex.org/docs/supported.html
- Check delimiters: `$x^2$` (inline) or `$$\frac{1}{2}$$` (display)

**Quiz not showing in browser:**
- Run `npm run generate-quiz-index`
- Check YAML frontmatter is valid
- Ensure file is named `quiz.md`

**Graphs not displaying:**
- Validate JSON in Mafs config blocks
- Check function syntax (must be valid JavaScript)
- View browser console for errors

## Next Steps

- Read [CLAUDE.md](./CLAUDE.md) for full architecture details
- Explore [.claude/skills/README.md](./.claude/skills/README.md) to learn about Skills
- Check out the example quiz in `quizzes/algebra/sample-linear-equations/`

## Support

- Report issues at your project repository
- Read Claude Code docs: https://docs.claude.com/en/docs/claude-code
- Learn about Skills: https://docs.claude.com/en/docs/agents-and-tools/agent-skills

Happy quiz making! 🎓
