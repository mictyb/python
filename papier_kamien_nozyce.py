# Napisz program, który sprawdza pojedynczy ruch w grę "kamień, papier, nożyce". Program przyjmuje Twój ruch oraz ruch przeciwnika. Następnie wyświetla, czy wygrałeś, czy zremisowałeś, czy przegrałeś. Podpowiedź: nie potrzebujemy pętli for. Zamiast tego potrzebujemy wiele rozgałęzień warunkowych if-else.


user1 =  input (" wybierz kamien, papier, nozyce: ")
user2 =  input (" wybierz kamien, papier, nozyce: ")

#  user 1 win

if user1 != user2:
    if user1 == "nozyce" and user2 == "papier":
        print(" wygrywa user 1", user1)
    elif user1 == "kamien" and user2 =="nozyce":
        print(" wygrywa user 1", user1)
    elif user1 =="papier" and user2 == "kamien":
        print(" wygrywa user 1", user1)
#  user 2 win 
    if user2 == "nozyce" and user1 == "papier":
        print(" wygrywa user 2", user2)
    elif user2 == "kamien" and user1 =="nozyce":
        print(" wygrywa user 2", user2)
    elif user2 =="papier" and user1 == "kamien":
        print(" wygrywa user 2", user2)



#  remis
else:
    print("mamy remis")
