"""Heart disease prediction logic."""

import math
from .coefficients import COEFFICIENTS

def sigmoid(x):
    """Apply sigmoid function to input."""
    return 1 / (1 + math.exp(-x))

def predict_heart_disease(features):
    """
    Predict heart disease probability using logistic regression.
    
    Args:
        features (dict): Medical features for prediction
        
    Returns:
        tuple: (bool: has_heart_disease, float: probability)
    """
    # Calculate the linear combination
    z = COEFFICIENTS['intercept']
    for feature, value in features.items():
        z += COEFFICIENTS[feature] * float(value)
    
    # Apply sigmoid function
    probability = sigmoid(z)
    return probability > 0.5, probability