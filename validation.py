"""
validation.py
BMI Calculator Pro v1.0

Contains all input validation functions.
"""


def validate_inputs(weight, height):
    """
    Validate weight and height entered by the user.

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        tuple:
            (True, "") if valid
            (False, error_message) if invalid
    """

    # Weight validation
    if weight <= 0:
        return False, "Weight must be greater than 0."

    if weight < 10:
        return False, "Weight is too low. Please enter a valid value."

    if weight > 500:
        return False, "Weight is too high. Please enter a valid value."

    # Height validation
    if height <= 0:
        return False, "Height must be greater than 0."

    if height < 0.5:
        return False, "Height is too low. Please enter a valid value."

    if height > 2.8:
        return False, "Height is too high. Please enter a valid value."

    return True, ""


def is_number(value):
    """
    Check whether a string can be converted to float.

    Args:
        value (str)

    Returns:
        bool
    """

    try:
        float(value)
        return True
    except ValueError:
        return False