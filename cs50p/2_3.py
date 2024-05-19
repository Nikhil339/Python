vowels = ['a', 'e', 'i', 'o', 'u']

sent = input("Input: ")
twttr = print("Ouput: ", end="")

for c in sent:
    if c.lower() in vowels:
        continue
    else:
        print(c, end="")

