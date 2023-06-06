def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    else:
        for x in range(1, m):
            if (a * x) % m == 1:
                return x

def affine_encrypt(text, key):
    a, b = key
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            else:
                char = chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
        encrypted_text += char
    return encrypted_text

def affine_decrypt(ciphertext, key):
    a, b = key
    decrypted_text = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "The key is not valid. The value of 'a' must be coprime to 26."
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                char = chr((a_inverse * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            else:
                char = chr((a_inverse * (ord(char) - ord('A') - b)) % 26 + ord('A'))
        decrypted_text += char
    return decrypted_text


plaintext = input("Enter Plain Text:")
key = (5,7)
encrypted_text = affine_encrypt(plaintext, key)
decrypted_text = affine_decrypt(encrypted_text, key)

print("Plaintext: " + plaintext)
print("Encrypted text: " + encrypted_text)
print("Decrypted text: " + decrypted_text)