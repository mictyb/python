ext = input("podaj swoj pessel")



new_text = ""
for i in text:
    if i.isdigit():
        
        new_text = new_text + "x"
    else:
        new_text = new_text + i
print(new_text)


print( " drugie rozwiazanie ")
new_text = ""
for i in text:
    if i.isdigit():
        
        new_text += "x"
    else:
        new_text += i
print(new_text)



#  3 rozwiazanie jest najwpl
print( " 3 rozwiazanie ")
new_text3 = text
for i in text:
    if i.isdigit():
        new_text3 = new_text3.replace(i,"x")  
    
print(new_text3)
