age_dog = float(input(" podaj wiek psa"))

if 2 >= age_dog > 0:
    print("pies ma", age_dog*10.5, "lat ludzkich")
elif age_dog > 2:
    age_dog = 10.5 * 2 + (age_dog - 2)*4
    print("pies ma", age_dog, "lat ludzkich")
else:
    print("podaj wlasciwy wiek psa")
