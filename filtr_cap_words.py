path = "M03/comments.txt"

with open(path) as stream:
    content = stream.read()
    numbers = content.split()

Big_letter = [i for i in content if i.isupper()]
print("".join(Big_letter))
i = str(Big_letter)
with open('M03/new_file.txt', 'w') as writer:
    writer.write(i)
