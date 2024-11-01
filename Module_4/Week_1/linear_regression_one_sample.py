import random

def initialize_params():
    """Initialize parameters with predefined values."""
    w1, w2, w3, b = (0.016992259082509283, 0.0070783670518262355, -0.002307860847821344, 0)
    return w1, w2, w3, b

def predict(x1, x2, x3, w1, w2, w3, b):
    """Predict the output y using linear model parameters."""
    return w1 * x1 + w2 * x2 + w3 * x3 + b

def compute_loss(y_hat, y):
    """Calculate Mean Squared Error (MSE) loss."""
    return (y_hat - y) ** 2

def compute_gradient_wi(xi, y, y_hat):
    """Calculate gradient with respect to a weight wi."""
    return 2 * (y_hat - y) * xi

def compute_gradient_b(y, y_hat):
    """Calculate gradient with respect to bias b."""
    return 2 * (y_hat - y)

def update_weight_wi(wi, dl_dwi, lr):
    """Update a weight wi using gradient descent."""
    return wi - lr * dl_dwi

def update_weight_b(b, dl_db, lr):
    """Update bias b using gradient descent."""
    return b - lr * dl_db
