# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    p = ['?', '!']
    text = [i for i in text.split(' ')]
    new_text = ''
    for j, n in enumerate(text):
        if len(n) == 1:
            if n in p:
                new_text += n
            else:
                new_text += n + 'ay'
        else:
            new_text += n[1:] + n[0] + 'ay'
        if not j == len(text) - 1:
            new_text += ' '

    return new_text
