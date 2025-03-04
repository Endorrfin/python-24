print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age <= 22:
        print("Please pay $9.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


# Exercise 5: BMI Calculator with Interpretations

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi <= 24.9:
    print("normal weight")
else:
    print("overweight")