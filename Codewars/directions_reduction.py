# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dirReduc(arr):
    y_axis = [['NORTH', 'SOUTH'], ['SOUTH', 'NORTH']]
    x_axis = [['WEST', 'EAST'], ['EAST', 'WEST']]
    new_array = []
    temp_array = []

    while len(arr) != 0:
        if len(arr) == 1 and len(new_array) == 1:
            return new_array + arr
        elif len(arr) == 1:
            return new_array + arr

        temp_array.append(arr.pop(0))
        temp_array.append(arr.pop(0))
        if temp_array in y_axis or temp_array in x_axis:
            temp_array = []
            if len(new_array) > 0:
                arr = [new_array.pop(-1)] + arr
            continue

        new_array += temp_array
        temp_array = []
        arr = [new_array.pop(-1)] + arr
    
    return new_array
