A=int(input("ingrese un numero "))
B=int(input("ingrese otro numero "))
if (A%B)==0:
    print("el numero",A,"es multiplo de",B)
else:
    print("el numero",A,"no es multiplo de",B)
if (B%A)==0:
    print("el numero",B,"es multiplo de",A)
else:
    print("el numero",B,"no es multiplo de",A)    