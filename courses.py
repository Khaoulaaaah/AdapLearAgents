from pathlib import Path

course_material = {
    "gradient_descent.txt": """Gradient Descent
Definition:
Gradient descent is an optimization algorithm used to minimize a function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient.

Example:
In linear regression, gradient descent updates weights to minimize the MSE between predicted and actual values.

Key Formula:
Update rule:
θ = θ - α * ∇J(θ)
Where:
- θ is the parameter (weights)
- α is the learning rate
- ∇J(θ) is the gradient of the cost function

Terms: Cost function, learning rate, convergence, local minima
""",

    "overfitting_underfitting.txt": """Overfitting vs Underfitting
Definition:
- Overfitting: Model learns noise and performs poorly on unseen data.
- Underfitting: Model is too simple and fails to capture the underlying trend.

Example:
- Overfitting: A deep decision tree fits all training points but generalizes poorly.
- Underfitting: A linear model used for non-linear data.

Solution: Cross-validation, regularization (L1/L2), early stopping
""",

    "regularization.txt": """Regularization
Definition:
Technique to prevent overfitting by adding a penalty to the loss function.

Types:
- L1 (Lasso): λ Σ|θᵢ| — leads to sparse models
- L2 (Ridge): λ Σθᵢ² — reduces coefficients smoothly

Example:
Regularized logistic regression

Terms: penalty term, hyperparameter (λ), norm
""",

    "bias_variance.txt": """Bias-Variance Tradeoff
Definition:
The balance between bias (error due to assumptions) and variance (error due to sensitivity to data fluctuations).

Visualization:
- High Bias, Low Variance → Underfitting
- Low Bias, High Variance → Overfitting

Goal: Find a model that generalizes well.
""",

    "evaluation_metrics.txt": """Evaluation Metrics
Classification:
- Accuracy = (TP + TN) / Total
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1-score = 2 × (Precision × Recall) / (Precision + Recall)

Regression:
- MSE (Mean Squared Error)
- RMSE
- MAE (Mean Absolute Error)
- R² score

Example:
Evaluate binary classifier predicting spam
""",

    "supervised_unsupervised.txt": """Supervised vs Unsupervised Learning
Supervised:
Labeled data used to train models (e.g., classification, regression)

Unsupervised:
Unlabeled data used to find patterns (e.g., clustering, dimensionality reduction)

Example:
- Supervised: Predicting housing prices
- Unsupervised: Customer segmentation
""",

    "decision_trees.txt": """Decision Trees
Definition:
A flowchart-like model used for classification and regression.

Splitting Criteria:
- Gini impurity
- Entropy

Pros: Easy to interpret
Cons: Prone to overfitting (mitigated by pruning or using ensembles)
""",

    "knn.txt": """k-Nearest Neighbors (k-NN)
Definition:
Non-parametric algorithm that classifies based on the majority label of the k closest points.

Distance Metrics:
- Euclidean
- Manhattan

Example:
Handwritten digit classification
""",

    "svm.txt": """Support Vector Machines (SVM)
Definition:
Finds the optimal hyperplane that separates classes with the maximum margin.

Key Concepts:
- Margin
- Kernel trick (for non-linear separation)

Example:
Email spam classification
""",

    "neural_networks.txt": """Neural Networks
Definition:
Models inspired by the brain’s neural structure with layers of interconnected nodes.

Components:
- Input layer
- Hidden layers (with activation functions)
- Output layer

Popular Variants:
- CNNs (images)
- RNNs (sequences)
"""
}

output_dir = Path("course_material")
output_dir.mkdir(parents=True, exist_ok=True)

for filename, content in course_material.items():
    (output_dir / filename).write_text(content, encoding='utf-8')


output_files = list(output_dir.glob("*.txt"))
output_files

