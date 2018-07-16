import sys
import string

alphabet = string.ascii_lowercase # a...z


def rot13(text):
    "This prints a text after rot13 (lowercase)"
    key = "nopqrstuvwxyzabcdefghijklm" # rot13
    
    text = text.lower()
    print("[i] rot13: ", end = "")
    for i in text:
        position = str.find(alphabet, i)
        if position != -1:
            print(key[position], end = "")
        else:
            print(i, end = "")

def rot(text, key):
    "This print a text after rot<KEY> (lowercase)"
    alphabetKey = alphabet[key:]
    alphabetKey += alphabet[:key]
    text = text.lower()
    print("[i] rot{}: ".format(key), end = "")
    for i in text:
        position = str.find(alphabet, i)
        if position != -1:
            print(alphabetKey[position], end = "")
        else:
            print(i, end = "")

if len(sys.argv) < 2:
    print("[!] Too few arguments.")
    print("[i] Usage: {} \"text to encrypt/decrypt\"".format(sys.argv[0]))
elif len(sys.argv) == 3:
    plaintext = sys.argv[1]
    print("[input]: {}".format(plaintext))
    rot(plaintext, int(sys.argv[2]))
else:
    plaintext = sys.argv[1]
    print("[input]: {}".format(plaintext))
    rot13(plaintext)
    


    

