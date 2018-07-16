import sys
import string

alphabet = string.ascii_lowercase # a...z
filename = sys.argv[0]

"This print a text after rot<num> only alphanumeric(lowercase)"
def rot(text, num=13):
    key = alphabet[num:] + alphabet[:num]
    text = text.lower()
    print(text.translate(str.maketrans(alphabet, key)))

"Display help"
def help():
    print("[i] Usage: {} [text] [key]".format(filename))
    print("    [text] - the text containing spaces must be enclosed in quotation marks")
    print("    [key] - max/min 25/-25, default 13")

if 2 <= len(sys.argv) <=3:
    text = sys.argv[1]
    if len(sys.argv) == 2:
        rot(text)
    elif len(sys.argv) == 3:
        try: # sys.argv[2] is a numeric?
            if(-26 < int(sys.argv[2]) < 26):
                rot(text, int(sys.argv[2]))
            else:
                print("[error] The second arg must be in range -25 to 25")
        except ValueError: # if sys.argv[2] is not numeric then error
            print("[error] The second arg is valid number.")
else:
    help()
