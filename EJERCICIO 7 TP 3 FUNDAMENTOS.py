NUMC=int(input("ingrese el n° de cliente: "))
VALORT=int(input("ingrese el valor total de la factura $"))
if (VALORT*0.02)>=120:
    print(".si abona dentro de los primeros 10 dias del mes tiene que abonar: $",VALORT-120)
else:  
    print(".si abona dentro de los primeros 10 dias del mes tiene que abonar: $%2.f" %(VALORT/1.02))
    
print(".si abona en los siguientes dias del mes, tiene que abonar el importe original que es de: $%2.f" %VALORT)

if (VALORT*0.1)>=150:
    print(".si abona luego de los 20 dias pasados del mes, tiene que abonar: $%2.f" %(VALORT*1.10))
else:
    print(".si abona luego de los 20 dias pasados del mes, tiene que abonar: $%2.f" %(VALORT+150))
    

    