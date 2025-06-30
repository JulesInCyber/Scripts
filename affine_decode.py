import random
import sys

# message = sys.argv[1]

a_tup = ((1,1),(3,9),(5,21),(7,15),(9,3),(11,19),(15,7),(17,23),(19,11),(21,5),(23,17),(25,25))

def encode_affine(cleartext):
    cipher = []
    a = random.choice(a_tup[0])
    b = random.randint(0,25)
    for letter in cleartext.upper():
        if ord(letter) in range(65,91):
            x = ord(letter) - ord("A")
            c = (a * x + b) % 26
            c_letter= chr(c + ord("A"))
            cipher.append(c_letter)
        else:
            cipher.append(letter)
    cipher_text =  "".join(cipher)
    print(f"\t[!] Encryption Key: ({a},{b})\n\n\t[!] Encoded Message: {cipher_text}")
    return cipher_text 

def decode_affine(key_a, key_b, ciphertext):
    for pair in a_tup:
        if pair[0] == key_a:
            a_inv = pair[1]
            break
    clear = []
    for letter in ciphertext.upper():
        if ord(letter) in range(65,91):
            y = ord(letter) - ord("A")
            c = a_inv * (y - key_b) % 26
            c_letter = chr(c + ord("A"))
            clear.append(c_letter)
        else:
            clear.append(letter)
    clear_text = "".join(clear)
    print(clear_text)
    return clear_text

print(decode_affine(3,10,"Fkrra Ywrp"))
