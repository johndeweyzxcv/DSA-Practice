# https://www.codewars.com/kata/5efae11e2d12df00331f91a6
import hashlib


def crack(hash):
    hash = bytes.fromhex(hash)
    print(hash)

    for i in range(0, 99999):
        res = hashlib.md5(("%05d" % i).encode())
        if res.digest() == hash:
            return "%05d" % i
