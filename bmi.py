

Weight= input("podaj wage")
Height = input("podaj wzrost w metrch format z kropka ")

BMI = (float(Weight) / float(Height)**2)
print(BMI)
if (BMI >= 18.5 and BMI <= 25):
    print(" jestes  fit - zyjesz zdrowo")
elif (BMI > 30 ):
    print( " jest nadwaga akcja redukcja ")
else :
    print ( "masz niedowage lub nadwage " )
