def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def operator(func, x, y):
    temp = func(x, y)
    return temp


print(operator(sub, 10, 5))
print(operator(add, 20, 5))
