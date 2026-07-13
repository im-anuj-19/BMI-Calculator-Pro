def validate_inputs(weight, height):
   
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
  
    try:
        float(value)
        return True
    except ValueError:
        return False
