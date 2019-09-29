AÑO=int(input("ingrese el año "))
if ((AÑO%4)==0 and (AÑO%100)!=0) or (((AÑO%4)==0)and((AÑO%100)==0)and((AÑO%400)==0)):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")
   
  