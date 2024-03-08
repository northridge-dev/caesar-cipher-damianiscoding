#!/usr/bin/env python
from decrypt import decrypt


def encrypt(plaintext, shift=0):
    #Does decrypt but the opposite
    plaintext = decrypt(plaintext, -shift)

    """
    Uses the Caesar cipher to encrypt a plaintext message.
    :param plaintext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    return plaintext


if __name__ == "__main__":
    plaintext = input("Message to encrypt: ")
    shift = int(input("Shift: "))
    print(encrypt(plaintext, shift))
