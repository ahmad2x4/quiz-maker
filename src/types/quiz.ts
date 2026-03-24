/**
 * Core types for the quiz application
 */

export type QuestionType = 'multiple-choice' | 'true-false' | 'numeric' | 'graph-interactive';

export type DifficultyLevel = 'easy' | 'medium' | 'hard';

export type MathTopic =
  | 'algebra'
  | 'geometry'
  | 'trigonometry'
  | 'calculus'
  | 'statistics'
  | 'functions';

export interface QuizQuestion {
  id: string;
  type: QuestionType;
  topic: MathTopic;
  difficulty: DifficultyLevel;
  question: string;
  /** LaTeX formula if needed */
  formula?: string;
  /** For multiple choice questions */
  options?: string[];
  /** Correct answer - can be index for MC, boolean for T/F, number for numeric */
  correctAnswer: number | boolean | string;
  /** Explanation shown after answering */
  explanation: string;
  /** Points awarded for correct answer */
  points: number;
  /** Configuration for interactive graph questions */
  graphConfig?: GraphConfig;
}

export interface GraphConfig {
  /** Type of graph to display */
  type: 'cartesian' | 'polar' | 'geometry';
  /** X-axis range */
  xRange: [number, number];
  /** Y-axis range */
  yRange: [number, number];
  /** Functions to plot (LaTeX format) */
  functions?: string[];
  /** Geometric shapes to display */
  shapes?: GeometricShape[];
}

export interface GeometricShape {
  type: 'point' | 'line' | 'circle' | 'polygon' | 'vector';
  points: [number, number][];
  label?: string;
  color?: string;
}

export interface QuizSession {
  id: string;
  startTime: Date;
  questions: QuizQuestion[];
  currentQuestionIndex: number;
  answers: Map<string, UserAnswer>;
  isCompleted: boolean;
}

export interface UserAnswer {
  questionId: string;
  answer: number | boolean | string;
  isCorrect: boolean;
  timeSpent: number; // in seconds
}

export interface QuizResult {
  sessionId: string;
  totalQuestions: number;
  correctAnswers: number;
  totalPoints: number;
  earnedPoints: number;
  percentage: number;
  timeSpent: number; // total time in seconds
  answers: UserAnswer[];
}
