# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    my_dict = {}
    for i in arr:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    val = list(my_dict.values())
    return list(my_dict.keys())[val.index(min(val))]