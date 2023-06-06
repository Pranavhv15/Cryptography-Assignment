def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd == 1:
        return (x % m + m) % m
    else:
        return None


a = int(input("Enter number to find modular multiplicative inverse:"))
m = int(input("Enter Modular value:"))
inverse = mod_inverse(a, m)

print("The modular inverse of", a, "modulo", m, "is:", inverse)