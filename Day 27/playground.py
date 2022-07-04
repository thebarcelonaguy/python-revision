def add(*args):
    sum1 = 0
    for n in args:
        sum1 += n
    print(sum1)


add(1, 3, 9, 4, 4, 45, 6, 6, 6, 6)


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=8)
