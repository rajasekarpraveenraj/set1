alphabet=input("enter the alphabet")
var=alphabet.lower()
if var.isalpha():
    if var=="a" or var=="e" or var=="i" or var=="o" or var=="u":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
