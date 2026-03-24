# Math Quiz Maker

A high-quality math quiz application for high school students featuring interactive charts, geometric visualizations, and beautifully rendered mathematical formulas.

## Features

- 📐 **Interactive Geometry**: Built with Mafs.js for dynamic geometric visualizations
- 📊 **Mathematical Formulas**: KaTeX rendering for crisp, fast LaTeX formulas
- 🎯 **Multiple Question Types**: Multiple choice, true/false, numeric input, and interactive graph questions
- 📚 **Comprehensive Topics**: Algebra, geometry, trigonometry, calculus, and statistics
- ⚡ **Instant Feedback**: Immediate answer validation with detailed explanations
- 🎨 **Modern UI**: Responsive design with Tailwind CSS and dark mode support

## Tech Stack

- **React** + **TypeScript** for type-safe component development
- **Vite** for blazing-fast development and optimized builds
- **KaTeX** for mathematical formula rendering
- **Mafs.js** for interactive math visualizations
- **Zustand** for lightweight state management
- **Tailwind CSS** for utility-first styling
- **Vitest** for unit testing

## Getting Started

### Prerequisites

- Node.js 18+ and npm

### Installation

```bash
# Install dependencies
npm install
```

### Development

```bash
# Start development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Build

```bash
# Create production build
npm run build

# Preview production build
npm run preview
```

### Testing

```bash
# Run tests
npm run test

# Run tests with UI
npm run test:ui
```

### Linting & Type Checking

```bash
# Run ESLint
npm run lint

# Type check without emitting
npm run type-check
```

## Project Structure

```
src/
├── components/     # React components
│   ├── quiz/      # Quiz components
│   ├── math/      # Math visualization components
│   └── ui/        # Reusable UI components
├── types/         # TypeScript types
├── stores/        # Zustand stores
├── data/          # Quiz questions
├── utils/         # Utilities
└── styles/        # Global styles
```

## Documentation

See [CLAUDE.md](./CLAUDE.md) for detailed architecture documentation and development guidelines.

## License

MIT
