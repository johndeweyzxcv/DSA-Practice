# https://www.codewars.com/kata/526dbd6c8c0eb53254000110
import re


def alphanumeric(password):
    if password == '':
        return False

    alpha = re.findall('[a-zA-Z]', password)
    num = re.findall('[0-9]', password)
    
    if len(alpha + num) == len(password):
        return True
    return False
