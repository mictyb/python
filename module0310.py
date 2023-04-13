Name_file = input('Podaj nazwe plikow z rozszerzeniem:  ')


EXTENSION = '.bak'

#  powoduje zaimportowanie biblioteki glob
# Biblioteka glob jest częścią STANDARDOWEJ BIBLIOTEKI, czyli zestawu bibliotek dostępnych w Pythonie out-of-the-box, bez potrzeby doinstalowywania czegokolwiek
import glob



files = glob.glob(Name_file)
print('files =', files)

# glob.glob('*.txt')  # ✅ ok
# glob.glob(r'C:\katalog\*.txt')  # ✅ ok  







# # Hint: jak sprawdzić, czy nazwa pliku zawiera kropkę? Bardzo prosto:
for i in files:

    if '.' in i:
        print('ma kropkę')
        separator_from_right = i.rsplit('.', 1)
        core = separator_from_right[0]
        filename =  core + EXTENSION
        print('stara nazwa ', i, 'nowa nazwa pliku = ' , filename)
    
    
    
       

# else:
#     print('nie ma kropki')
#     core = Name_file 
    

# filename =  core + EXTENSION
# print('nowa nazwa pliku = ' , filename)








