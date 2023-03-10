

text = input(" podaj dowolny tekst Redaktorze: ")
words = len(text.split())
length_of_char = len(text)
average = (length_of_char - words)/ words

print('liczba znakow :  ', length_of_char)
print('liczba znakow :  ', words)
print('srednia dlugosc slow wynosi :  ', average )
