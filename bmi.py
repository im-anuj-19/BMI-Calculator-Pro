def calculate_bmi(weight, height):
 
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
   
    if bmi < 18.5:
        return (
            "Underweight",
            "Your body weight is below the recommended range.\n\n"
            "• Eat a balanced diet rich in protein.\n"
            "• Increase healthy calorie intake.\n"
            "• Include strength training.\n"
            "• Consult a doctor if weight loss is unexplained."
        )

    elif bmi < 25:
        return (
            "Normal",
            "Excellent! Your BMI is within the healthy range.\n\n"
            "• Continue exercising regularly.\n"
            "• Eat a balanced diet.\n"
            "• Stay hydrated.\n"
            "• Maintain your current lifestyle."
        )

    elif bmi < 30:
        return (
            "Overweight",
            "Your BMI is above the recommended range.\n\n"
            "• Reduce junk food and sugary drinks.\n"
            "• Walk or exercise at least 30 minutes daily.\n"
            "• Eat more fruits and vegetables.\n"
            "• Monitor your weight regularly."
        )

    else:
        return (
            "Obese",
            "Your BMI is significantly above the healthy range.\n\n"
            "• Consult a healthcare professional.\n"
            "• Follow a medically supervised weight-loss plan.\n"
            "• Exercise regularly after medical advice.\n"
            "• Focus on long-term healthy habits."
        )


def healthy_weight_range(height):
   
    minimum = round(18.5 * height * height, 1)
    maximum = round(24.9 * height * height, 1)

    return minimum, maximum
