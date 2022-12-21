# TWO SUM

def two_sum(numbers, n):
    # Run for loop then Store the number and the index of that number
    # indexes = {1: 0, 2: 1, 3: 2}
    indexes = {}

    for i, b in enumerate(numbers):
        # a + b = n
        # To find (a) subtract (n) to (b) and to find (b) subtract (n) to (a) 
        a = n - b

        # Kinda like 3 + 5 = 8; 3 = 8 - 5; 5 = 8 - 3 

        if a in indexes:
            # Returns index
            return [indexes[a], i]
        elif a not in indexes:
            indexes[b] = i

print(two_sum([1, 2, 3], 4))
print(two_sum([12, 5, 32, 6, 10, 7], 15))