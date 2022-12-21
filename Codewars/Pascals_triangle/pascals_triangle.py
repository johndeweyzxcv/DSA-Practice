# https://www.codewars.com/kata/5226eb40316b56c8d500030f

def pascals_triangle(n):
    res = []

    for _ in range(n):
        if len(res) == 0:
            res.append([1])
        elif len(res) == 1:
            res.append([1, 1])
        else:
            temp_list = []
            temp_list.append(1)
            last_item = res[-1]
            for i, n in enumerate(last_item):
                if not i + 1 > len(last_item) - 1:
                    temp_list.append(n + last_item[i + 1])
            temp_list.append(1)
            res.append(temp_list)
            temp_list = []

    new_res = []
    for i in res:
        for j in i:
            new_res.append(j)

    return new_res
