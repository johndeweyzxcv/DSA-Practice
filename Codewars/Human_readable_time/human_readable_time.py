# # https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds):
    if seconds == 0:
        return '00:00:00'
    
    formats = [0, 0, 0]

    for i in range(3):
        if seconds < 60 or i == 2:
            formats[i] = seconds
            break
        elif seconds >= 60:
            q, r = divmod(seconds, 60)
            formats[i] = r
            seconds = q
    
    formats.reverse()
    return ':'.join(['%02d' % i for i in formats])

print(make_readable(4728))