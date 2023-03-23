path = input("podaj nazwe pliku")


with open(path) as stream:
    text = stream.read()


for i in text:
    if i.isdigit():
        text = text.replace(i,"x")

print(text)


