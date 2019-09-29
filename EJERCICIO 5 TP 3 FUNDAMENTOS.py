BASE=int(input("ingrese la base del triangulo en cm: "))
ALT=int(input("ingrese la altura del triangulo en cm: "))
if (BASE and ALT)>=0:
    print("la superficie del triangulo es %.2f" %((BASE*ALT)/2),"cm")
else:
    print("los numeros ingresados no son validos para la formula")
    print("por favor ingrese valores positivos")