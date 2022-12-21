# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    my_dict = {}
    for i in seq:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    
    for j in my_dict:
        if my_dict[j] % 2 == 1:
            return j
