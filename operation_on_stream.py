#  zamiana liczb na x 
text = "Tutaj są tajemne dane - mój PESEL to 1234567890 i zarabiam 8000000$"


for i in text:
    if i.isdigit():
        text = text.replace(i,"x")

print(text)

# stream = open('M03/plik.txt')

# Rozwiń program z M02L11. Tamten program pytał użytkownika o tekst do zanonimizowania, czyli zastępował wszelkie występujące tam liczby iksami, np. 1234 -> XXXX. Tym razem zapytaj użytkownika o nazwę pliku (np. plik.txt) i wczytaj tekst właśnie z niego. Zanonimizuj go, a następnie wyświetl na ekranie.

path = input("podaj nazwe pliku")

#  otwarcie strumienia 
stream = open(path, 'r')

# wczytanie strumienia koniecznie do zmiennej
content = stream.read()  # wczytaj całą zawartość pliku

for i in content:
    if i.isdigit():
        content= content.replace(i,"x")

#  wyprintowanie
print('content =', content)

#  zamkniecie strumienia
stream.close()
