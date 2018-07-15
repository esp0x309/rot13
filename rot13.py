import string

alphabet = string.ascii_lowercase # a...z
key = "nopqrstuvwxyzabcdefghijklm" # rot13

plaintext = "sEbaStIan12 sepo"
plaintext = plaintext.lower()

print(plaintext)

for i in plaintext:
    position = str.find(alphabet, i)
    if position != -1:
        print(key[position], end = "")
    else:
         print(i, end = "")
    

