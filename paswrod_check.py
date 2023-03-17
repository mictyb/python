



text = input("podaj haslo ")



for i in text:
    if i.isnumeric():
        print(i + ":  to liczba")
    elif i.isalpha():
        print(i + ": to  litera")
    elif i.isspace():
        print(i + ":  to bialy znak ")
    else:
        print(i + ": to znak specjalny")
