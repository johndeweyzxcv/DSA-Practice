# https://www.codewars.com/kata/5742e725f81ca04d64000c11
import os

def random_bits(n_bits):
    n_bytes, _ = divmod(n_bits, 8)
    random_data = os.urandom(n_bytes)
    return random_data

def random_int(n_bits):
    random_data = random_bits(n_bits)
    val = int.from_bytes(
        random_data, 'big', signed=False
        )
    return val

def randint(max_val):
    bit_size = int(max_val).bit_length()

    tried = 0
    while True:
        val = random_int(bit_size)
        if val <= max_val:
            break
        
        if tried % 10 == 0 and tried:
            bit_size -= 1
        
        tried += 1
    
    return val

def prime_or_composite(n):
    first_primes = [2, 3, 5, 7]
    first_composites = [1, 4, 6, 8, 9, 10]
    if n in first_primes:
        return 'Probable Prime'
    
    if n in first_composites:
        return 'Composite'
    
    if not (n & 1):
        return 'Composite'

    if n < 2:
        return 'Composite'
    
    d = n - 1
    r = 0

    while not (d & 1):
        r += 1
        d >>= 1
    
    for _ in range(3):
        a = randint(n - 3) + 1
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return 'Composite'
            if x == n - 1:
                break
        else:
            return 'Composite'
    
    return 'Probable Prime'
