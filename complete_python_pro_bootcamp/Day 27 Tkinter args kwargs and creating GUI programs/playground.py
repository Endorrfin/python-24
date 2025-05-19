

def set(*args):
    for n in args:
        print(n)
    print(type(args))


set(3, 5, 6)


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('KEY', key)
        print('VALUE', value)

    print(kwargs['add'])


calculate(add=3, multiply=5)



def calculate_2(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate_2(2, add=3, multiply=5)