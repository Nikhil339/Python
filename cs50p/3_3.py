def main():
    d = {}
    while True:
        try:
            item = input().upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            print()
            for key in d:
                print(d[key], key)
            break
    
main()