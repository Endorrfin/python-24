# Question 1: What is the output of this code?
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
    # the optional arguments, toast and ham, get assigned their default values.

bar(1, 2)

# Question 2: What is the output of this code?
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
    # When keywords are used the order of the arguments listed does not matter. Python matches by name not position

bar(toast='nah', spam=4, eggs=2)

# Question 3: What is the # data # type of args?
# Output: Integer, String, List, ✅ Tuple
def test(*args):
    print(args)

test(1, 2, 3, 5)


# Question 4: What is the output of the code above?
def test(*args):
    print(args)
    # (1, 2, 3, 5) args is a tuple, hence it will print the parenthesis

test(1, 2, 3, 5)


# Question 5: What is the output of the code above?
def all_aboard(a, *args, **kw):
    print(a, args, kw)
    # 4 is passed by position
    # (7, 3, 0) are collected into a tuple,
    # x and y are in a keyword dictionary


all_aboard(4, 7, 3, 0, x=10, y=64)

