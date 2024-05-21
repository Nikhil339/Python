import string

punc = list(string.punctuation)
punc.append(" ")

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def length(s):
    return 2 <= len(s) <= 6

def others(s):
    return not any(i in punc for i in s)

def start2(s):
    return s[:2].isalpha()

def zero(s):
    for i in range(1, len(s)):
        if s[i].isdigit() and s[i] == '0' and s[i-1].isalpha():
            return False
    return True

def btw(s):
    found_digit = False
    for i in s:
        if i.isdigit():
            found_digit = True
        elif found_digit and i.isalpha():
            return False
    return True

def is_valid(s):
    return length(s) and others(s) and start2(s) and zero(s) and btw(s)

main()
