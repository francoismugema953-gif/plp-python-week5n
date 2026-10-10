import math

def calculate_hypotenuse(a, b):
    """
    Calculates the hypotenuse of a right-angled triangle using the math module.
    Formula: c = sqrt(a^2 + b^2)
    """
    return math.hypot(a, b)

def greet_user(name):
    """
    Returns a customized greeting string.
    """
    return f"Hello, {name}! Welcome to your custom Python module."
