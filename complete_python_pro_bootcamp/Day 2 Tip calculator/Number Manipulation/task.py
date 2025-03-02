bmi = 84 / 1.65 ** 2

print(bmi)
print(int(bmi))
print(round(bmi))

print(round(bmi, 2))

height = 1.65
weight = 84

print(height ** 2)

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)

# score ======================
score = 0

# User scores a point
score += 1
print(score)

# f-strings
print("Your score is " + str(score))


score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, Your are winning is {is_winning}")

# Case 1
name = input("What is your name? ")
print(f"Hello, {name}")

# Case 2
name = input("What is your name? ")
print("Hello, " + name)

# Case 3
age = 12
print(f"Your are {age} years old")

# Case 4
age = 12
print(f"Your are " + age + " years old")
