import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from xgboost import XGBClassifier

def load_dataset():
    """
    Placeholder function to load a dataset. 
    Replace this with actual dataset loading logic.
    """
    # Example: Create a dummy dataset with 100 samples and 10 features
    X = np.random.rand(100, 10)
    y = np.random.randint(0, 2, 100)  # Binary classification (0 or 1)
    return X, y

def split_dataset(X, y, test_size=0.2, random_state=42):
    """
    Utility function to split dataset into train and test sets.
    """
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return train_x, test_x, train_y, test_y

def fitness_func(solution, train_x, train_y):
    """
    Fitness function to evaluate the performance of the solution.
    In this case, the solution is expected to represent model parameters for XGBoost.
    
    Parameters:
        solution: array-like
            Represents model parameters, e.g., [learning_rate, max_depth, n_estimators].
        
        train_x: array-like
            Training data features.
        
        train_y: array-like
            Training data labels.
    
    Returns:
        fitness: float
            The fitness score (e.g., accuracy or AUC) of the model with the given parameters.
    """
    # Solution could represent hyperparameters like [learning_rate, max_depth, n_estimators]
    learning_rate, max_depth, n_estimators = solution

    # Create an XGBoost classifier with the given solution parameters
    model = XGBClassifier(learning_rate=learning_rate, max_depth=int(max_depth), n_estimators=int(n_estimators))

    # Fit the model to the training data
    model.fit(train_x, train_y)

    # Get predictions on the training set (in real cases, should evaluate on test set)
    predictions = model.predict(train_x)

    # Calculate fitness score (you can also use accuracy_score, or other metrics)
    if len(np.unique(train_y)) == 1:
        fitness = accuracy_score(train_y, predictions)
    else:
        fitness = roc_auc_score(train_y, predictions)

    return fitness

def scale_solution(solution, param_ranges):
    """
    Scales a solution vector to the given parameter ranges.
    
    Parameters:
        solution: array-like
            The raw solution vector from the nature-inspired algorithm (typically between 0 and 1).
        
        param_ranges: list of tuples
            Each tuple represents the min and max bounds for a hyperparameter.
            Example: [(0.001, 0.1), (2, 10), (10, 200)] for learning_rate, max_depth, n_estimators.
    
    Returns:
        scaled_solution: array-like
            Solution vector scaled to the parameter ranges.
    """
    scaled_solution = np.array([low + (high - low) * val for val, (low, high) in zip(solution, param_ranges)])
    return scaled_solution

def evaluate_solution(model, test_x, test_y):
    """
    Utility function to evaluate the model on the test data.
    
    Parameters:
        model: trained model
            The model to evaluate.
        
        test_x: array-like
            Test data features.
        
        test_y: array-like
            Test data labels.
    
    Returns:
        evaluation_metrics: dict
            Contains accuracy and AUC scores of the model on the test data.
    """
    predictions = model.predict(test_x)
    
    metrics = {}
    metrics['accuracy'] = accuracy_score(test_y, predictions)
    
    if len(np.unique(test_y)) > 1:
        metrics['roc_auc'] = roc_auc_score(test_y, predictions)
    else:
        metrics['roc_auc'] = None

    return metrics
