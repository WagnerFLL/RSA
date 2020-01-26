import random

max_PrimLength = 1000000000000

alphabet = {"A": 2, "B": 3, "C": 4,
            "D": 5, "E": 6, "F": 7, "G": 8,
            "H": 9, "I": 10, "J": 11, "K": 12,
            "L": 13, "M": 14, "N": 15, "O": 16,
            "P": 17, "Q": 18, "R": 19, "S": 20,
            "T": 21, "U": 22, "V": 23, "W": 24,
            "X": 25, "Y": 26, "Z": 27, " ": 28
            }

alphabet_invert = {v: k for k, v in alphabet.items()}


def egcd(a, b):
    """
    calculates the modular inverse from e and phi
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def gcd(a, b):
    """
    calculates the gcd of two ints
    """
    while b != 0:
        a, b = b, a % b
    return a


def generate_keys(p, q, e):

    n = p * q
    print("n ", n)
    '''phi(n) = phi(p)*phi(q)'''
    phi = (p - 1) * (q - 1)
    print("phi ", phi)

    print("e=", e, " ", "phi=", phi)
    '''d[1] = modular inverse of e and phi'''
    d = egcd(e, phi)[1]

    '''make sure d is positive'''
    d = d % phi
    if d < 0:
        d += phi

    return (e, n), (d, n)


def decrypt(ctext, private_key):
    try:
        key, n = private_key
        text = [alphabet_invert[pow(char, key, n)] for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)


def encrypt(text, public_key):
    key, n = public_key
    ctext = [pow(alphabet[char], key, n) for char in text]
    return ctext


if __name__ == '__main__':
    public_key, private_key = generate_keys()
    print("Public: ", public_key)
    print("Private: ", private_key)

    ctext = encrypt("HELLO WORLD", public_key)
    print("encrypted  =", ctext)
    plaintext = decrypt(ctext, private_key)
    print("decrypted =", plaintext)
