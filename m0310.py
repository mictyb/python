Name_file = input('Podaj nazwe pliku z rozszerzeniem:  ')


EXTENSION = '.bak'

# Hint: jak sprawdzić, czy nazwa pliku zawiera kropkę? Bardzo prosto:

if '.' in Name_file:
    print('ma kropkę')
    separator_from_right = Name_file.rsplit('.', 1)
    core = separator_from_right[0]
    
    
    
       

else:
    print('nie ma kropki')
    core = Name_file 
    

filename =  core + EXTENSION
print('nowa nazwa pliku = ' , filename)









