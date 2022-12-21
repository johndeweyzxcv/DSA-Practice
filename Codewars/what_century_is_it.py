# https://www.codewars.com/kata/52fb87703c1351ebd200081f

def what_century(year):
    my_dict = {1: 'st', 2: 'nd', 3: 'rd'}
    a = list(year)
    int_a = int(a[1])

    res = ''.join(a[:2])
    if a[-1] == '0' and a[-2] == '0':
        if a[0] == '1':
            res += 'th'
        else:
            if int_a not in my_dict:
                res += 'th'
            else:
                res += my_dict[int_a]
        return res
    else:
        res = str(int(''.join(a[:2])) + 1)
        if a[0] == '1':
            res += 'th'
        else:
            if int_a + 1 not in my_dict:
                res += 'th'
            elif int_a + 1 in my_dict:
                res += my_dict[int_a + 1]
        return res
