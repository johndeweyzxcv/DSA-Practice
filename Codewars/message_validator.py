# https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc

def is_valid_message(message):
    if message == '': return True
    list_msg = list(message)
    nums = []

    for i, n in enumerate(list_msg):
        try:
            if isinstance(int(n), int) and i > 0 and len(nums) == 0:
                return False
            elif isinstance(int(n), int) and i == len(list_msg) - 1:
                return False
            elif isinstance(int(n), int):
                nums.append(n)
                list_msg[i] = '-' 
                if isinstance(int(list_msg[i + 1]), int):
                    a = ''
                    a += n + list_msg[i + 1]
                    nums.pop(-1)
                    nums.append(a)
                    list_msg[i + 1] = '-'
                    continue   
        except ValueError as e:
            continue
    
    list_msg = ''.join(list_msg).split('-')
    list_msg = [x for x in list_msg if x != '']

    if len(list_msg) != len(nums): return False

    for i, n in enumerate(list_msg):
        if len(n) == int(nums[i]):
            continue
        else:
            return False
    return True
