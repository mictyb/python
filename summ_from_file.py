path = "M03/expenses.txt"

with open(path) as stream:
    content = stream.read()
    numbers = content.split()

sum = 0
for i in numbers:
    sum = sum + float(i)

print("suma liczb w pliku wynosi : ", sum)
