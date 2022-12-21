# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    s = []
    
    for i in string:
        if i == '(':
            s.append(i)
        if i == ')':
            if len(s) == 0:
                return False
            else:
                s.pop()
    
    return len(s) == 0