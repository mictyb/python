import glob

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)






print( 'zostana wyswietlone nastpujace pliki ' , filenames )
for filename in filenames:
    print('\n', filename)


while True:
    a = input("Enter yes/no to continue: ")
    if a=="yes":
        for filename in filenames:
            with open(filename, 'r') as stream:
                content = stream.read()
                lines = content.split('\n')
                first_line = lines[0]
            print(filename, ':', first_line)
        continue
    elif a=="no":
        break
    else:
        print("Enter either yes/no")
