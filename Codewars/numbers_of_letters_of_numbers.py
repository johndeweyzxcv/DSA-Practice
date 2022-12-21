# https://www.codewars.com/kata/599febdc3f64cd21d8000117

def func(n, l=None):
    my_dict = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    b = ''
    my_list = []
    if l != None:
        for i in l:
            my_list.append(i)
    for i in n:
        b += my_dict[str(i)]
    my_list.append(b)
    if 'four' in my_list:
        return my_list
    else:
        conv_str = str(len(b))
        return func(conv_str, l=my_list)

def numbers_of_letters(n):
    string = str(n)
    return func(string)
