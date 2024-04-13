def countword(str1, word):
    s = str1.split()
    count = 0
    for w in s:
        if w == word:
            count += 1
    return count
    
str1 = input("Enter any sentence: ")
word = input("Enter word to search in sentence: ")
count = countword(str1, word)
if count == 0:
    print("Sorry no such word exists.")
else:
    print(word, "occurs", count, "times.")