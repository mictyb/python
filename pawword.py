password = input(" podaj haslo :  ")





#  check Upper char 

counter = 0 
for i in password:
    if (i.isalpha() and  i.isupper()):
        counter += 1
if counter < 1:
    print("brak wielkiej litery - musi byc conajmniej jedna")



#  check lower char 

counter = 0 
for i in password:
    if (i.isalpha() and  i.islower()):
        counter += 1
if counter < 1:
    print("brak malej litery - musi byc conajmniej jedna")
    
# check space

counter = 0 
for i in password:
    if i.isspace():
        counter += 1
if counter > 0:
    print("w hasle wystepuje spacja nie powinno jej byc")





# special character check
counter = 0 
for i in password:
    if not i.isalpha() and  not i.isdigit():
        counter += 1
if counter < 1:
    print("brak znaku specjalnego musi byc conajmniej jeden")



#  check length of password
if len(password)< 8:
    print(" haslo jest za krotkie . haslo powinno skladac sie co najmniej z 8 znakow")

























