import random

a_tup = ((1,1),(3,9),(5,21),(7,15),(9,3),(11,19),(15,7),(17,23),(19,11),(21,5),(23,17),(25,25))

def encode_affine(cleartext):
    cipher = []
    a = random.choice(a_tup[0])
    b = random.randint(0,25)
    for letter in cleartext.upper():
        if ord(letter) in range(65,91):
            x = ord(letter) - ord("A")
            c = (a * x + b) % 26
            print(c)
            c_letter= chr(c + ord("A"))
            cipher.append(c_letter)
        else:
            cipher.append(letter)
    cipher_text =  "".join(cipher)
    print(f"Ciphertext: {cipher_text}\nKey: ({a},{b})")

encode_affine("Hello World!")