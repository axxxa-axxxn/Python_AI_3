def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

try:
    print("===== BMI Calculator =====")

    weight = float(input("Enter your weight (kg): "))
    height_cm = float(input("Enter your height (cm): "))

    # Check for positive values
    if weight <= 0 or height_cm <= 0:
        print("Weight and height must be greater than zero.")

    # Check for realistic weight range
    elif weight < 10 or weight > 500:
        print("Please enter a realistic weight (10 - 500 kg).")

    # Check for realistic height range in centimeters
    elif height_cm < 50 or height_cm > 300:
        print("Please enter a realistic height (50 - 300 cm).")

    else:
        # Convert centimeters to meters
        height = height_cm / 100

        bmi = calculate_bmi(weight, height)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Please enter valid numeric values.")