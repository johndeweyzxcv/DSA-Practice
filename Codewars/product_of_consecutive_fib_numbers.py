# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def productFib(prod):
    a, b = 0, 1
    while a * b != prod:
        a, b = b, a + b
        if a * b > prod:
            return [a, b, False]
    return [a, b, True]
