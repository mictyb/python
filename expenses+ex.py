file = "M03/expenses_ex.txt"

with open(file) as stream:
    content = stream.read()
    new_line = content.split('\n')

print(new_line)
expenses = 0 

for i in new_line:
    second_split = i.split()
    if second_split:
        current_expenses = second_split[0]
        expenses += float(current_expenses)








print('suma wydatkow ' , expenses)



   







