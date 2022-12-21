# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def word_order(string):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_string = string.split(' ')
    my_dict = {}
    new_string = []

    for i in list_string:
        for j in i:
            if j in nums:
                my_dict[int(j)] = i
    
    while len(my_dict) != 0:
        min_num = min(my_dict)
        new_string.append(my_dict[min_num])
        del my_dict[min_num]
    
    return ' '.join(new_string)
