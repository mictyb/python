path = "M03/comments.txt"

with open(path) as stream:
    content = stream.read()
    numbers = content.split()

sum = 0
for i in numbers:
    sum += 1

print("suma wyrazow wynosi : ", sum)



# Napisz program, który zlicza ile jest słów w pliku tekstowym.
