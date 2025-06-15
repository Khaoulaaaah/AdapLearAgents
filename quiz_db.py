import random
from progress_db import get_concept_accuracy

QUIZ_DB = {
  "supervised learning": [
    {
      "question": "What is the primary goal of supervised learning?",
      "options": ["To find patterns in data", "To label new data based on past labels", "To reduce dimensionality", "To detect anomalies"],
      "answer": "To label new data based on past labels",
      "difficulty": "easy"
    },
    {
      "question": "Which of these is a supervised learning algorithm?",
      "options": ["K-Means", "Linear Regression", "PCA", "Apriori"],
      "answer": "Linear Regression",
      "difficulty": "medium"
    },
    {
      "question": "Which of the following tasks can be solved using supervised learning?",
      "options": ["Clustering", "Anomaly detection", "Classification", "Dimensionality reduction"],
      "answer": "Classification",
      "difficulty": "medium"
    },
    {
      "question": "In supervised learning, the dataset used for training contains:",
      "options": ["Only features", "Only labels", "Features and labels", "Unlabeled data"],
      "answer": "Features and labels",
      "difficulty": "hard"
    }
  ],
  "unsupervised learning": [
    {
      "question": "Which algorithm is typically used for unsupervised learning?",
      "options": ["Linear Regression", "Decision Trees", "K-Means", "Logistic Regression"],
      "answer": "K-Means",
      "difficulty": "medium"
    },
    {
      "question": "What does unsupervised learning aim to do?",
      "options": ["Predict labels", "Classify data", "Find hidden patterns", "Improve accuracy"],
      "answer": "Find hidden patterns",
      "difficulty": "easy"
    },
    {
      "question": "Which of the following is *not* typically an unsupervised learning algorithm?",
      "options": ["K-Means", "DBSCAN", "Hierarchical Clustering", "Random Forest"],
      "answer": "Random Forest",
      "difficulty": "hard"
    },
    {
      "question": "Unsupervised learning algorithms work best with which type of data?",
      "options": ["Labeled data", "Unlabeled data", "Numerical labels", "Balanced datasets"],
      "answer": "Unlabeled data",
      "difficulty": "easy"
    }
  ],
  "overfitting": [
    {
      "question": "What is overfitting?",
      "options": ["Model fits training data too well", "Model fits test data well", "Model underperforms", "Model is too simple"],
      "answer": "Model fits training data too well",
      "difficulty": "easy"
    },
    {
      "question": "How can we reduce overfitting?",
      "options": ["Add more layers", "Use smaller datasets", "Regularization", "Increase complexity"],
      "answer": "Regularization",
      "difficulty": "medium"
    },
    {
      "question": "Which of the following is a sign of overfitting?",
      "options": ["Low training accuracy", "Low variance", "High training accuracy but low test accuracy", "High bias"],
      "answer": "High training accuracy but low test accuracy",
      "difficulty": "hard"
    },
    {
      "question": "Which technique helps prevent overfitting in decision trees?",
      "options": ["Boosting", "Bagging", "Pruning", "Stacking"],
      "answer": "Pruning",
      "difficulty": "medium"
    }
  ],
  "cross-validation": [
    {
      "question": "Why is cross-validation used?",
      "options": ["To reduce training time", "To optimize hyperparameters", "To evaluate generalization", "To train faster"],
      "answer": "To evaluate generalization",
      "difficulty": "easy"
    },
    {
      "question": "Which is a popular type of cross-validation?",
      "options": ["Leave-One-Out", "Min-Max Scaling", "T-SNE", "SMOTE"],
      "answer": "Leave-One-Out",
      "difficulty": "medium"
    },
    {
      "question": "In k-fold cross-validation, what does ‘k’ represent?",
      "options": ["Number of features", "Number of datasets", "Number of splits", "Number of epochs"],
      "answer": "Number of splits",
      "difficulty": "easy"
    },
    {
      "question": "Which cross-validation technique is more computationally expensive?",
      "options": ["Train/test split", "3-fold CV", "Leave-One-Out", "5-fold CV"],
      "answer": "Leave-One-Out",
      "difficulty": "hard"
    }
  ],
  "gradient descent": [
    {
      "question": "What does gradient descent aim to minimize?",
      "options": ["Variance", "Bias", "Cost function", "Accuracy"],
      "answer": "Cost function",
      "difficulty": "easy"
    },
    {
      "question": "What happens if the learning rate is too high?",
      "options": ["It converges faster", "It might overshoot", "It underfits", "It fits perfectly"],
      "answer": "It might overshoot",
      "difficulty": "medium"
    },
    {
      "question": "Which of the following is a variant of gradient descent?",
      "options": ["RMSProp", "Naive Bayes", "ID3", "Apriori"],
      "answer": "RMSProp",
      "difficulty": "hard"
    },
    {
      "question": "In which direction does gradient descent move?",
      "options": ["Toward maximum", "Toward saddle point", "Toward minimum", "Randomly"],
      "answer": "Toward minimum",
      "difficulty": "easy"
    }
  ]
}


def get_random_quiz(concepts, num_questions=1):
    quiz = []
    for concept in concepts:
        questions = QUIZ_DB.get(concept, [])
        acc = get_concept_accuracy(concept)
        if acc < 0.4:
            level = "easy"
        elif acc < 0.7:
            level = "medium"
        else:
            level = "hard"
        filtered = [q for q in questions if q.get("difficulty") == level]
        if not filtered:
            filtered = questions  # fallback
        quiz.append((concept, random.choice(filtered)))
    return quiz


