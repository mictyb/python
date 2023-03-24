


#  answer 1
path = input('podaj nazwe pliku: ')
with open(path) as stream:
    text = stream.read()
#  zamkniecie nastepuja tutaj chyba ze wciecia ponizej sa
for i in text:
    if i.isdigit():
        text = text.replace(i,'x')


with open('M03/new_file5.txt', 'w') as variab1:
    variab1.write(text)
    
    
    # implicit writer.close() - daje nam to gwarancję, że faktycznie zmiany dotrą na dysk
print(':-) Sukces')    

#  answer 2
file_open = input('podaj nazwe pliku wejsciowego: ')
with open(file_open) as stream:
    text = stream.read()

for i in text:
    if i.isdigit():
        text = text.replace(i,'x')
file_exit = input('podaj nazwe pliku wyjsciowego: ')

    


#answer 3 and 4 

if file_exit:
    with open(file_exit, 'x') as writer:
        writer.write(text)
else:
    print(text)
print(':-) Sukces plik zapisany')  







        ### 🔴 Ćwiczenie

# 1. Rozwiń program z poprzedniego ćwiczenia tak, aby zapisać zanonimizowany tekst do nowego wyjściowego pliku. 
# 2. Poproś użytkownika zarówno o nazwę pliku wejściowego (tego, który mamy odczytać, np. plik.txt), jak i wyjściowego (tego, do którego mamy zapisać). 
# 3. Jeżeli użytkownik nie poda nazwy pliku wyjściowego, wówczas wypisz zanominimizowany tekst funkcją print.
# 4. Jeżeli plik wyjściowy już istnieje, to go nie nadpisuj. W tym celu trzeba wykorzystać funkcję open w inny sposób. Jak? Znajdź w dokumentacji tej funkcji!
