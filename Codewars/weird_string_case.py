# https://www.codewars.com/kata/52b757663a95b11b3d00062d

def weird_case(word):
    w = ''
    for j, n in enumerate(word):
        if j % 2 == 0:
            w += n.upper()
        elif j % 2 == 1:
            w += n.lower()
    return w

def to_weird_case(words):
    c = ''
    if ' ' in words:
        a = words.split(' ')
        for i, n in enumerate(a):
            c += weird_case(n)
            if not i == len(a) - 1:
                c += ' '
    else:
        c += weird_case(words)
    return c
