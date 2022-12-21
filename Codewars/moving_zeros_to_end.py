# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    zero_index = 0

    for i, n in enumerate(lst):
        if n != 0:
            lst[zero_index] = n
            if zero_index != i:
                lst[i] = 0
            zero_index += 1
    
    return lst
