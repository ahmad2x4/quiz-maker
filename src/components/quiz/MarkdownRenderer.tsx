import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import { Components } from 'react-markdown';
import { MafsRenderer } from './MafsRenderer';

interface MarkdownRendererProps {
  content: string;
  className?: string;
}

/**
 * Renders markdown content with support for:
 * - LaTeX math formulas (via KaTeX)
 * - GitHub Flavored Markdown
 * - Raw HTML (for details/summary tags)
 * - Custom styling for quiz elements
 */
export function MarkdownRenderer({ content, className = '' }: MarkdownRendererProps) {
  const components: Components = {
    // Style headings
    h1: ({ children, ...props }) => (
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-4" {...props}>
        {children}
      </h1>
    ),
    h2: ({ children, ...props }) => (
      <h2 className="text-2xl font-semibold text-gray-800 dark:text-gray-100 mb-3 mt-6" {...props}>
        {children}
      </h2>
    ),
    h3: ({ children, ...props }) => (
      <h3 className="text-xl font-semibold text-gray-700 dark:text-gray-200 mb-2 mt-4" {...props}>
        {children}
      </h3>
    ),

    // Style paragraphs
    p: ({ children, ...props }) => (
      <p className="text-gray-700 dark:text-gray-300 mb-4 leading-relaxed" {...props}>
        {children}
      </p>
    ),

    // Style lists
    ul: ({ children, ...props }) => (
      <ul className="list-disc list-inside mb-4 space-y-2 text-gray-700 dark:text-gray-300" {...props}>
        {children}
      </ul>
    ),
    ol: ({ children, ...props }) => (
      <ol className="list-decimal list-inside mb-4 space-y-2 text-gray-700 dark:text-gray-300" {...props}>
        {children}
      </ol>
    ),
    li: ({ children, ...props }) => (
      <li className="ml-4" {...props}>
        {children}
      </li>
    ),

    // Style code blocks
    code: ({ inline, className, children, ...props }: {
      inline?: boolean;
      className?: string;
      children?: React.ReactNode;
    }) => {
      // Check if this is a Mafs config block
      if (className === 'language-json:mafs') {
        try {
          // Parse the JSON content and render with MafsRenderer
          const configJson = String(children).trim();
          return <MafsRenderer config={configJson} />;
        } catch (error) {
          console.error('Error parsing Mafs config:', error);
          return (
            <div className="mafs-error my-4 p-4 bg-red-100 dark:bg-red-900 rounded-lg text-red-700 dark:text-red-200">
              <strong>Error rendering interactive graph:</strong> Invalid configuration
            </div>
          );
        }
      }

      if (inline) {
        return (
          <code
            className="px-1.5 py-0.5 bg-gray-100 dark:bg-gray-800 text-sm rounded font-mono text-pink-600 dark:text-pink-400"
            {...props}
          >
            {children}
          </code>
        );
      }

      return (
        <pre className="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg overflow-x-auto mb-4">
          <code className={className} {...props}>
            {children}
          </code>
        </pre>
      );
    },

    // Style images
    img: ({ src, alt, ...props }) => (
      <img
        src={src}
        alt={alt}
        className="max-w-full h-auto rounded-lg shadow-md my-4 mx-auto"
        {...props}
      />
    ),

    // Style blockquotes
    blockquote: ({ children, ...props }) => (
      <blockquote
        className="border-l-4 border-indigo-500 pl-4 italic text-gray-600 dark:text-gray-400 my-4"
        {...props}
      >
        {children}
      </blockquote>
    ),

    // Style horizontal rules
    hr: ({ ...props }) => (
      <hr className="my-8 border-t-2 border-gray-200 dark:border-gray-700" {...props} />
    ),

    // Style tables
    table: ({ children, ...props }) => (
      <div className="overflow-x-auto my-4">
        <table className="min-w-full border-collapse border border-gray-300 dark:border-gray-700" {...props}>
          {children}
        </table>
      </div>
    ),
    thead: ({ children, ...props }) => (
      <thead className="bg-gray-100 dark:bg-gray-800" {...props}>
        {children}
      </thead>
    ),
    tbody: ({ children, ...props }) => (
      <tbody {...props}>
        {children}
      </tbody>
    ),
    tr: ({ children, ...props }) => (
      <tr className="border-b border-gray-200 dark:border-gray-700" {...props}>
        {children}
      </tr>
    ),
    th: ({ children, ...props }) => (
      <th className="px-4 py-2 text-left font-semibold text-gray-900 dark:text-white" {...props}>
        {children}
      </th>
    ),
    td: ({ children, ...props }) => (
      <td className="px-4 py-2 text-gray-700 dark:text-gray-300" {...props}>
        {children}
      </td>
    ),

    // Style links
    a: ({ children, href, ...props }) => (
      <a
        href={href}
        className="text-indigo-600 dark:text-indigo-400 hover:underline"
        target="_blank"
        rel="noopener noreferrer"
        {...props}
      >
        {children}
      </a>
    ),

    // Style strong/bold
    strong: ({ children, ...props }) => (
      <strong className="font-bold text-gray-900 dark:text-white" {...props}>
        {children}
      </strong>
    ),

    // Style emphasis/italic
    em: ({ children, ...props }) => (
      <em className="italic text-gray-800 dark:text-gray-200" {...props}>
        {children}
      </em>
    ),
  };

  return (
    <div className={`markdown-content ${className}`}>
      <ReactMarkdown
        remarkPlugins={[remarkMath, remarkGfm]}
        rehypePlugins={[rehypeKatex, rehypeRaw]}
        components={components}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
