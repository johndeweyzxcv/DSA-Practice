# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    
    while len(str(n)) != 1:
        calc = 0
        for i in str(n):
            calc += int(i)
        n = calc
    
    return n