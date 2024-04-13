with open("sample2.txt", "r") as f1, open("sample2copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)

print("File Copied Successfully!")
