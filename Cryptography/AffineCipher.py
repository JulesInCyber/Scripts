import random
from termcolor import colored
import sys

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
    print(f"\t[+] Encryption Key: ({a},{b})\n\n\t[+] Encoded Message: {cipher_text}")
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
    print(f"[+] Key used for encryption; ({key_a}, {key_b})")
    print(f"[+] decoded Message: {clear_text}")
    return clear_text

prog_option = sys.argv[1]

def main():
    if prog_option == "-e":
        try:
            message = sys.argv[2]
            encode_affine(message)
        except:
            print("[?] No Message specified!")
    elif prog_option == "-d":
        try:
            key_a = int(sys.argv[2])
            key_b = int(sys.argv[3])
            message = sys.argv[4]
            decode_affine(key_a, key_b, message)
        except:
            print("[?] Missing arguments")
    elif prog_option == "-h":
        print("[~] Usage: AffineCypher.py [OPTION] [Arguments] \n\n")
        # Encrypting
        print("-e\tEncryption mode\n" \
        "\tRandomly key values\n" \
        "\tUsage: AffineCypher.py -e 'Hello World!'\n")
        # Decrypting
        print("-d\tDecryption mode\n" \
        "\tDecrypts a message with a provided key\n" \
        "\tUsage: AffineCipher.py -d key_a key_b 'Cipher Text'")
    else:
        print("[!] Unknown Option. Use '-h' for help")


if __name__ =='__main__':
    main()

