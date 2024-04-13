def main():
    face = input("Type a sentence: ")
    smth = convert(face)
    print(smth)

def convert(x):
    return x.replace(":)","🙂").replace(":(","🙁")

main()
