def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

try:
    print("===== BMI Calculator =====")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
    else:
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