import { useState } from 'react'
import { QuizBrowser } from './components/quiz/QuizBrowser'
import { QuizViewer } from './components/quiz/QuizViewer'
import type { QuizMetadata } from './data/quizIndex'

function App() {
  const [selectedQuiz, setSelectedQuiz] = useState<QuizMetadata | null>(null)

  const handleSelectQuiz = (quiz: QuizMetadata) => {
    setSelectedQuiz(quiz)
  }

  const handleBack = () => {
    setSelectedQuiz(null)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      {selectedQuiz ? (
        <QuizViewer quiz={selectedQuiz} onBack={handleBack} />
      ) : (
        <QuizBrowser onSelectQuiz={handleSelectQuiz} />
      )}
    </div>
  )
}

export default App
