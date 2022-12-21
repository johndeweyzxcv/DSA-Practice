# https://www.codewars.com/kata/5842df8ccbd22792a4000245

def expanded_form(num):
    a = list(str(num))
    a.reverse()
    n_list = []

    for i, n in enumerate(a):
        num = n + '0' * i
        if int(num[0]) > 0:
            n_list.append(num)
    
    n_list.reverse()
    return ' + '.join(n_list)
