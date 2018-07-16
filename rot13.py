import sys
import string

alphabet = string.ascii_lowercase # a...z
key = "nopqrstuvwxyzabcdefghijklm" # rot13

def rot13(text):
    "This prints a text after rot13 (lowercase)"
    text = text.lower()
    print("[output]: ", end = "")
    for i in text:
        position = str.find(alphabet, i)
        if position != -1:
            print(key[position], end = "")
        else:
            print(i, end = "")

if len(sys.argv) < 2:
    print("[!] Too few arguments.")
    print("[i] Usage: {} \"text to encrypt/decrypt\"".format(sys.argv[0]))
else:
    plaintext = sys.argv[1]
    print("[input]: {}".format(plaintext))
    rot13(plaintext)


    

