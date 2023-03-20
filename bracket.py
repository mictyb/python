

text = input (" podaj text")

counter_O=0
counter_C=0

for i in text:
    if i == "(":
        counter_O += 1
    elif i == ")":
        counter_C +=1

if (counter_C != counter_O):
    print("liczba nawiasow ( oraz ) jest rozna")
else:
    print("liczba nawiasow ( oraz ) jest ok ")
