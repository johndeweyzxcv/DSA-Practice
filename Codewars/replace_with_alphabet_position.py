# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    text = ''.join(char for char in text if char.isalnum())
    a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    string = ''
    for i, n in enumerate(text):
        if i == len(text) - 1:
            string += str(a.index(n.upper()) + 1)
        else:
            string += str(a.index(n.upper()) + 1)
            string += ' '
    return string
