
import random


def gensqrs(nu):
    for x in range(nu):
        yield x**2


for x in gensqrs(10):
    print(x)


def rand_ints(l, h, x):

    for i in range(x):
        yield random.randint(l ,h)


for n in rand_ints(1, 20, 5):
    print("\t")
    print(n)


sen = "Hello World"

print(next(iter(sen)))


