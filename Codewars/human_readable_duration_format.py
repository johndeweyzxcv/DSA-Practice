# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if seconds == 0:
        return 'Now'
    else:
        seconds_list = [31_536_000, 86_400, 3_600, 60]
        list = [0, 0, 0, 0, 0]

        for i in range(len(list)):
            if i == 4 and seconds < seconds_list[i - 1]:
                list[i] = seconds
                break  
            elif seconds >= seconds_list[i]:
                quotient, remainder = divmod(seconds, seconds_list[i])
                list[i] = quotient
                seconds = remainder
                continue
            elif seconds < seconds_list[i]:
                continue
        
        readable_format = []
        word_list = ['year', 'day', 'hour', 'minute', 'second']
        for i, n in enumerate(list):
            if n > 1:
                readable_format.append(f'{n} {word_list[i]}s')
            elif n == 1:
                readable_format.append(f'{n} {word_list[i]}')
        
        res = ''
        if len(readable_format) > 2:
            last_item = readable_format.pop(-1)
            for i, n in enumerate(readable_format):
                if i == len(readable_format) - 1:
                    res += str(n) + ' and '
                else:
                    res += str(n) + ', '
            res += str(last_item)
        elif len(readable_format) == 2:
            res = readable_format[0] + ' and ' + readable_format[1]
        elif len(readable_format) == 1:
            res = readable_format[0]
        
        return res
