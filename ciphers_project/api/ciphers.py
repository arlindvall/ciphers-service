

def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if 'a' <= c <= 'z':
            c_encoded = ord('a') + (ord(c) - ord('a') + shift) % 26
        elif 'A' <= c <= 'Z':
            c_encoded = ord('A') + (ord(c) - ord('A') + shift) % 26
        else:
            c_encoded = ord(c)
        cipher_text += chr(c_encoded)
    return cipher_text