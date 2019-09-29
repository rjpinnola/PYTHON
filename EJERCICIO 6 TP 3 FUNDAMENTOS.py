NUMP=int(input("ingrese la cantidad de paginas que contiene el libro "))
BAS=125
PAG=NUMP*2.20
if NUMP<=300:
    print("el costo del libro será de $%2.f" %(PAG+BAS))
if NUMP>300 and NUMP<=600:
    print("el costo del libro será de $%2.f" %(BAS+PAG+80))
if NUMP>600:
    print(" el costo del libro será de $%2.f" %(BAS+PAG+80+160))
#    CONSULTAR SI SE AGREGAN TBN LOS $80 ANTERIORES A ESTA CONDICION
