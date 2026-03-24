# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Math Quiz Maker** application designed for high school students, featuring high-quality mathematical formulas, interactive charts, and geometric visualizations. The application uses a unique architecture where **quiz content is generated from PDFs using Claude Code Skills** rather than manual entry.

### Key Concept: Skills-Based Quiz Generation

Instead of traditional API calls, this project uses **Claude Code Skills** - modular, auto-invoked capabilities that Claude uses to generate quizzes from PDF documents. When you upload a PDF and ask to create a quiz, Claude automatically activates the relevant skills to extract content, generate questions, create visualizations, and compile the final markdown files.

## Technology Stack

### Frontend Framework
- **React 18.3+** with **TypeScript 5.6+** for type-safe component development
- **Vite 6.0+** as the build tool and dev server (fast HMR, optimized builds)
- **Tailwind CSS 3.4+** for utility-first styling

### Markdown & Math Rendering
- **react-markdown 9.0+**: Render markdown content with GitHub Flavored Markdown support
- **remark-math 6.0+** & **rehype-katex 7.0+**: LaTeX math formula support in markdown
- **KaTeX 0.16+**: Fast, synchronous math typesetting
- **gray-matter 4.0+**: Parse YAML frontmatter from quiz markdown files

### Interactive Visualizations
- **Mafs.js 0.21+**: React components for interactive math visualizations
  - Cartesian/polar coordinate systems
  - Function plots, geometric shapes, vectors
  - Built-in TypeScript support

### State Management
- **Zustand 5.0+**: Lightweight state management for quiz sessions

### Testing
- **Vitest 2.1+**: Fast unit testing with Jest-compatible API

## Architecture

### Directory Structure

```
quiz-maker/
├── .claude/
│   └── skills/                      # Claude Code Skills (auto-invoked)
│       ├── pdf-quiz-generator/      # Extracts content and generates questions
│       ├── math-visualizer/         # Creates graphs, diagrams, Mafs configs
│       └── quiz-compiler/           # Assembles markdown files
├── quizzes/                         # Generated quiz content (bundled with app)
│   ├── algebra/
│   │   └── [quiz-name]/
│   │       ├── quiz.md              # Markdown with YAML frontmatter
│   │       ├── graph-001.png        # Visual assets
│   │       └── mafs-config-001.json # Interactive graph configs
│   ├── geometry/
│   ├── trigonometry/
│   ├── calculus/
│   ├── statistics/
│   └── functions/
├── scripts/
│   ├── requirements.txt             # Python dependencies for skill scripts
│   └── generateQuizIndex.js         # Generates src/data/quizIndex.ts
├── src/
│   ├── components/
│   │   └── quiz/
│   │       ├── MarkdownRenderer.tsx # Renders quiz markdown with math
│   │       ├── MafsRenderer.tsx     # Renders interactive Mafs graphs
│   │       └── QuizBrowser.tsx      # Browse and search quizzes
│   ├── data/
│   │   └── quizIndex.ts             # Auto-generated quiz metadata index
│   └── types/
│       └── quiz.ts                  # TypeScript interfaces
└── vite.config.ts
```

## Claude Code Skills

This project includes three specialized Skills that Claude automatically uses when generating quizzes:

### 1. `pdf-quiz-generator`
**Location:** `.claude/skills/pdf-quiz-generator/SKILL.md`

**Purpose:** Analyzes PDF files and generates math quiz questions

**Auto-activates when:**
- User uploads a PDF and asks to create a quiz
- User mentions generating questions from textbooks or study materials

**What it does:**
- Extracts text, formulas, and structure from PDFs using pdfplumber
- Identifies math topics and difficulty levels
- Generates questions in JSON format following quality criteria
- Creates multiple question types (MC, T/F, numeric, graph-interactive)
- Ensures proper LaTeX formatting and detailed explanations

**Key script:** `.claude/skills/pdf-quiz-generator/scripts/analyze_pdf.py`

### 2. `math-visualizer`
**Location:** `.claude/skills/math-visualizer/SKILL.md`

**Purpose:** Creates mathematical visualizations and interactive graphs

**Auto-activates when:**
- Quiz questions need visual aids
- User requests graphs or geometric diagrams
- Questions involve function plotting or geometry

**What it does:**
- Generates Mafs.js configuration JSON for interactive graphs
- Creates static PNG/SVG images using matplotlib
- Builds geometric diagrams programmatically
- Supports mermaid diagrams for flowcharts

**Key script:** `.claude/skills/math-visualizer/scripts/create_graph.py`

**Output formats:**
- `mafs-config-001.json` - Interactive graph configuration
- `graph-001.png` - Static matplotlib graph
- `diagram-001.svg` - Geometric SVG diagram

### 3. `quiz-compiler`
**Location:** `.claude/skills/quiz-compiler/SKILL.md`

**Purpose:** Assembles questions and assets into formatted markdown files

**Auto-activates when:**
- Questions have been generated and need to be saved
- User wants to finalize a quiz

**What it does:**
- Validates all questions and formulas
- Organizes visual assets in topic folders
- Generates YAML frontmatter with metadata
- Formats questions in markdown with LaTeX support
- Creates collapsible explanation sections using `<details>`

## Quiz Validation Agent

**IMPORTANT:** After generating any new quiz, you MUST use the `quiz-answer-validator` agent to validate all answers and explanations before considering the quiz complete.

### `quiz-answer-validator` Agent
**Type:** Specialized validation agent

**When to use:**
- **Proactively** after the quiz-compiler skill has assembled the markdown file
- **Before** the final save to the quizzes/ directory
- When the user requests validation of an existing quiz

**What it validates:**
- Mathematical accuracy of all answer keys
- Correctness of solution steps in explanations
- Proper LaTeX formula syntax
- Logical consistency between questions and answers
- Completeness of explanations

**How to invoke:**
After quiz compilation is complete, use the Task tool:
```
Task tool -> quiz-answer-validator agent -> "Validate the quiz at quizzes/[topic]/[quiz-name]/quiz.md"
```

**Example workflow:**
1. Generate quiz using skills (pdf-quiz-generator, math-visualizer, quiz-compiler)
2. Quiz markdown file is created
3. **→ Launch quiz-answer-validator agent** (do this proactively)
4. Agent validates all answers and reports any issues
5. Fix any issues found
6. Final save and quiz index generation

**Why this is critical:**
- Ensures students receive accurate information
- Catches calculation errors in answer keys
- Verifies solution steps are mathematically sound
- Maintains quiz quality and educational value

## Quiz Markdown Format

Each quiz is stored as `quizzes/[topic]/[quiz-name]/quiz.md`:

```markdown
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
description: "Practice solving basic linear equations"
---

# Linear Equations Practice

## Question 1

**Topic:** Algebra • **Difficulty:** Medium • **Points:** 10

Solve for $x$: $2x + 5 = 13$

**Options:**
- A) $x = 3$
- B) $x = 4$
- C) $x = 8$
- D) $x = 9$

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) $x = 4$**

### Solution
Step 1: Subtract 5 from both sides
$$2x = 8$$

Step 2: Divide by 2
$$x = 4$$

</details>

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": {"x": [-5, 15], "y": [0, 20]},
  "elements": [
    {"type": "plot", "function": "x => 2*x + 5", "color": "#3b82f6"}
  ]
}
```

---
```

## Development Workflow

### Creating a Quiz from PDF

1. **Upload PDF** and provide a prompt:
   ```
   "Create a quiz from this textbook chapter on linear equations.
   Generate 10 questions with mixed difficulty."
   ```

2. **Claude automatically invokes skills:**
   - `pdf-quiz-generator` extracts content and generates questions
   - `math-visualizer` creates any needed graphs or diagrams
   - `quiz-compiler` assembles the final markdown file

3. **Quiz is saved** to `quizzes/[topic]/[quiz-name]/`

4. **Rebuild app** to include the new quiz:
   ```bash
   npm run generate-quiz-index
   npm run build
   ```

### Development Commands

```bash
# Install dependencies
npm install

# Install Python dependencies for skills
pip install -r scripts/requirements.txt

# Start development server
npm run dev

# Generate quiz index (scans quizzes/ folder)
npm run generate-quiz-index

# Build for production (includes quiz index generation)
npm run build

# Type checking
npm run type-check

# Linting
npm run lint

# Testing
npm run test          # Run tests
npm run test:ui       # Visual test debugging
```

## Frontend Components

### MarkdownRenderer
**File:** `src/components/quiz/MarkdownRenderer.tsx`

Renders quiz markdown with:
- LaTeX math formulas (KaTeX)
- GitHub Flavored Markdown
- Custom styling for quiz elements
- Support for `<details>` tags (explanations)

Usage:
```tsx
import { MarkdownRenderer } from '@/components/quiz/MarkdownRenderer';

<MarkdownRenderer content={quizMarkdown} />
```

### MafsRenderer
**File:** `src/components/quiz/MafsRenderer.tsx`

Renders interactive Mafs.js visualizations from JSON config:

```tsx
import { MafsRenderer } from '@/components/quiz/MafsRenderer';

const config = {
  type: 'cartesian',
  viewBox: { x: [-10, 10], y: [-10, 10] },
  elements: [
    { type: 'plot', function: 'x => x**2', color: '#3b82f6' },
    { type: 'point', coordinates: [2, 4], color: '#ef4444' }
  ]
};

<MafsRenderer config={config} />
```

### QuizBrowser
**File:** `src/components/quiz/QuizBrowser.tsx`

Browse, filter, and search quizzes:
- Filter by topic and difficulty
- Search by title, tags, description
- Display quiz cards with metadata
- Click to start quiz

## Quiz Index System

The `src/data/quizIndex.ts` file is auto-generated by `scripts/generateQuizIndex.js`:

**Generation:**
```bash
npm run generate-quiz-index
```

**What it does:**
1. Scans `quizzes/` directory for all `quiz.md` files
2. Extracts YAML frontmatter from each quiz
3. Generates TypeScript file with quiz metadata array
4. Provides helper functions (filter by topic, search, etc.)

**Usage:**
```typescript
import { quizzes, getQuizzesByTopic, searchQuizzes } from '@/data/quizIndex';

const algebraQuizzes = getQuizzesByTopic('algebra');
const results = searchQuizzes('linear equations');
```

## LaTeX Formula Guidelines

- **Inline math:** Use `$x^2 + 1$`
- **Display math:** Use `$$\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$`
- **KaTeX compatibility:** See https://katex.org/docs/supported.html
- **In JSON:** Escape backslashes `"\\frac{1}{2}"`

## Python Dependencies for Skills

Skills use Python scripts for PDF processing and visualization:

```bash
pip install -r scripts/requirements.txt
```

**Key libraries:**
- `pdfplumber` - PDF text extraction
- `matplotlib` - Graph generation
- `numpy` - Numerical operations
- `sympy` - Symbolic math
- `pillow` - Image processing

## Best Practices

### When Creating Quizzes
1. Provide clear context in your prompt (topic, difficulty, number of questions)
2. Reference specific sections of the PDF if needed
3. Review generated questions for accuracy
4. Test interactive graphs in the browser
5. **Never put a ✓ checkmark next to the correct option in the options list** — the correct answer must only be revealed inside the `<details>` block (e.g. `**Correct Answer: B) ...**`)

### When Adding New Quiz Topics
1. Create folder in `quizzes/[new-topic]/`
2. Update `TOPICS` array in `scripts/generateQuizIndex.js`
3. Update `topics` constant in `src/data/quizIndex.ts`
4. Add topic color in `QuizBrowser.tsx` `getTopicColor()` function

### When Modifying Skills
1. Edit the `SKILL.md` file to change behavior
2. Keep descriptions specific for better auto-activation
3. Test by uploading a PDF and requesting a quiz
4. Skills are version-controlled - commit changes to share with team

## Troubleshooting

**Quiz not appearing in browser:**
- Run `npm run generate-quiz-index` to rebuild index
- Check YAML frontmatter is valid
- Ensure file is named `quiz.md`

**LaTeX formulas not rendering:**
- Verify KaTeX syntax at https://katex.org/docs/supported.html
- Check for proper delimiters (`$` or `$$`)
- Escape backslashes in JSON strings

**Mafs graph not displaying:**
- Validate JSON configuration
- Check function syntax (must be valid JavaScript)
- Inspect browser console for errors

**PDF extraction failing:**
- Ensure PDF is not encrypted
- Check if `pdfplumber` is installed
- Try alternative libraries if needed

## Future Enhancements

Potential features:
- Real-time quiz taking mode with timer
- Score tracking and progress analytics
- Export quizzes as PDF worksheets
- Multi-language support
- Question bank randomization
- Adaptive difficulty based on performance
- Teacher dashboard for creating custom quizzes
