password = input(" podaj haslo :  ")
counter = 0 
for i in password:
    if i == "a" or i== "A":
        counter += 1

print("liczba wszystkich a , A wynosi" , counter)

