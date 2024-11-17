file = open("sample.txt", 'r')
words = file.read().split()
length = []

for word in words:
    x = len(word)
    length.append(x)

max_length = max(length)

for word in words:
    if len(word) == max_length:
        print(word)

