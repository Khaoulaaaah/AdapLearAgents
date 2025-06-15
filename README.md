# Adaptive Quiz Tutor

This project is an AI-powered, **adaptive quiz system** that helps learners master machine learning concepts through interactive quizzes and targeted explanations.

---

## Features

- **Multiple-choice quizzes** on core ML topics
-  **Adaptive difficulty**: Questions become harder or easier based on user performance
-  **Progress tracking** using SQLite
-  **Retry misunderstood concepts** with focused explanations
-  **Local vector search (RAG)** with Qdrant + HuggingFace embeddings for content retrieval
-  **Explanations** generated via a RAG agent using embedded course material

---

## How It Works

    The quiz starts by selecting your weakest concepts using past performance data.

    Questions are chosen based on your current mastery level (easy → medium → hard).

    If you answer incorrectly, the system shows a personalized explanation using RAG.

    You can retry misunderstood concepts with 2 questions per concept until you master them.

## Requirements

    Python 3.8+

    LangChain

    Qdrant (local)

    HuggingFace Transformers / Sentence-Transformers
