"""
Project Utilities Module
Common utility functions used across the project.
"""

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")

def validate_input(data):
    """Validate input data."""
    return data is not None and len(str(data)) > 0
