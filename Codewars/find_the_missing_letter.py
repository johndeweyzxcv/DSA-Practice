# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(chars):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    upper = chars[0].isupper()
    chars = [i.upper() for i in chars]
    
    start = alphabet.index(chars[0])
    end = alphabet.index(chars[-1])
    new_list = alphabet[start : end + 1]

    for i in new_list:
        if i not in chars:
            if upper:
                return i.upper()
            else:
                return i.lower()
