# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def split_string(s):
    s_list = list(s)
    ls = []

    while len(s_list) != 0:
        if not len(s_list) == 1:
            ls.append(s_list[0] + s_list[1])
            del s_list[0]
            del s_list[0]
        else:
            ls.append(s_list[0] + '_')
            del s_list[0]
    
    return ls
