# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    string_hex = ''
    if r > 255:
        r = r - (r % 255)
    if g > 255:
        g = g - (g % 255)
    if b > 255:
        b = b - (b % 255)
    
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    
    string_hex = ''
    string_hex += format(r, '02x')
    string_hex += format(g, '02x')
    string_hex += format(b, '02x')
    return string_hex.upper()
