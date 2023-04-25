file = "M03/expenses_ex.txt"

with open(file) as stream:
    content = stream.read()
    new_line = content.split('\n')

print(new_line)
expenses = 0 


#  robie drugi podzial linii i nastepnie biore 1 element bo to liczba
sum_ex =0
minimum = 0
maximum = 0
average = 0 
new_list = []
for line in new_line:
    second_split = line.split()
    if second_split:
        new_list.append(float(second_split[0]))

print('new list', new_list)
minimum = min(new_list)
maximum = max(new_list)
sum_ex = sum(new_list)

print('min', minimum)
print('max', maximum)
print('sum', sum_ex)
average = sum_ex/len(new_list)
print('average', average)
