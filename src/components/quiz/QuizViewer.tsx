import { useState, useEffect } from 'react';
import { MarkdownRenderer } from './MarkdownRenderer';
import type { QuizMetadata } from '@/data/quizIndex';

/**
 * Simple frontmatter parser for browser environments
 * Extracts content after the YAML frontmatter (---...---)
 */
function parseFrontmatter(text: string): string {
  const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/;
  const match = text.match(frontmatterRegex);

  if (match) {
    // Return content after frontmatter
    return match[2] ?? '';
  }

  // No frontmatter found, return original text
  return text;
}

interface QuizViewerProps {
  quiz: QuizMetadata;
  onBack: () => void;
}

export function QuizViewer({ quiz, onBack }: QuizViewerProps) {
  const [content, setContent] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadQuiz() {
      try {
        setLoading(true);
        setError(null);

        // Fetch the quiz markdown file (BASE_URL handles /quiz-maker/ prefix on GitHub Pages)
        const response = await fetch(import.meta.env.BASE_URL + quiz.filePath.replace(/^\//, ''));

        if (!response.ok) {
          throw new Error(`Failed to load quiz: ${response.statusText}`);
        }

        const text = await response.text();

        // Parse frontmatter and extract only the markdown content
        const markdownContent = parseFrontmatter(text);
        setContent(markdownContent);
      } catch (err) {
        console.error('Error loading quiz:', err);
        setError(err instanceof Error ? err.message : 'Failed to load quiz');
      } finally {
        setLoading(false);
      }
    }

    loadQuiz();
  }, [quiz.filePath]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-400">Loading quiz...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center p-6">
        <div className="max-w-md w-full bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-6">
          <h2 className="text-xl font-semibold text-red-800 dark:text-red-200 mb-2">
            Error Loading Quiz
          </h2>
          <p className="text-red-600 dark:text-red-300 mb-4">{error}</p>
          <button
            onClick={onBack}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors"
          >
            Back to Quiz Browser
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      {/* Header */}
      <div className="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-10">
        <div className="max-w-4xl mx-auto px-6 py-4">
          <button
            onClick={onBack}
            className="text-indigo-600 dark:text-indigo-400 hover:underline mb-2 flex items-center"
          >
            ← Back to Quiz Browser
          </button>
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
                {quiz.title}
              </h1>
              <div className="flex items-center gap-3 mt-1 text-sm text-gray-600 dark:text-gray-400">
                <span className="capitalize">{quiz.topic}</span>
                <span>•</span>
                <span className="capitalize">{quiz.difficulty}</span>
                <span>•</span>
                <span>{quiz.questionCount} questions</span>
                {quiz.estimatedTime && (
                  <>
                    <span>•</span>
                    <span>{quiz.estimatedTime} min</span>
                  </>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Quiz Content */}
      <div className="max-w-4xl mx-auto px-6 py-8">
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-8">
          <MarkdownRenderer content={content} />
        </div>
      </div>
    </div>
  );
}
