def main():
    frac = get_fraction("Fraction: ")
    print(frac)

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/") #the split function splits the string at "/", the default value is " " and stores the values in a list
            div = int(x)/int(y)
            if 0<=div<=0.1:
                return("E")
            elif 0.9<=div<=1:
                return("F")
            elif 0.1<=div<=0.9:
                return str(round(div*100)) + "%"
        except (ZeroDivisionError, ValueError):
            pass

main()