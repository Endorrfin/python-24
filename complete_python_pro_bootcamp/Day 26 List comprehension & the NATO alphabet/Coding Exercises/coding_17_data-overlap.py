# Data Overlap
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:
# 1
# 2
# 3

# and file2.txt contained:
# 2
# 3
# 4

# result = [2, 3]

# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.

# ✅ SOLUTION
# Read numbers for both files
with open('file1.txt', 'r') as file1:
    file_1_data = file1.read().splitlines()
    print('FILE 1 DATA', file_1_data)

with open('file2.txt', 'r') as file2:
    file_2_data = file2.read().splitlines()
    print('FILE 2 DATA', file_2_data)

# Convert to integers and find common numbers using list comprehension
file_1_numbers = [int(number) for number in file_1_data]
print('FILE 1 NUMBERS', file_1_numbers)

file_2_numbers = [int(number) for number in file_2_data]
print('FILE 2 NUMBERS', file_2_numbers)

# Find the overlap (common numbers)
overlap_numbers = [number for number in file_1_numbers if number in file_2_numbers]
print('OVERLAP NUMBERS', overlap_numbers)