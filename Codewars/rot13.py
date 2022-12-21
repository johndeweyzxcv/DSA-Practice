# https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = list(alphabet)
    c = ''
    for i in message:
        if i.isupper():
            c += a[(a.index(i) + 13) % len(a)]
        elif i.islower():
            c += a[(a.index(i.upper()) + 13) % len(a)].lower()
        else:
            c += i
    return c
