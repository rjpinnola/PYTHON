DINERO=int(input("ingrese la cantidad de dinero a entregar $"))
print("la cantidad de billetes a entregar es de:")
b100=(DINERO%100)
b50=b100%50
b10=b50%10
b5=b10%5
b1=b5%1
if b100==0:
    print("entregar",(DINERO//100),"billetes de 100")
if b100>0 and b50==0:
    print("entregar",(DINERO//100),"billetes de 100","y",b100//50,"billetes de 50")
if b100>0 and b50>0 and b10==0:
    print("entregar",(DINERO//100),"billetes de 100",";",b100//50,"billetes de 50","y",b50//10,"billetes de 10")
if b100>0 and b50>0 and b10>0 and b5==0:
    print("entregar",(DINERO//100),"billetes de 100",";",b100//50,"billetes de 50",";",b50//10,"billetes de 10","y",b10//5,"billetes de 5")
if b100>0 and b50>0 and b10>0 and b5>0 and b1==0:
    print("entregar",(DINERO//100),"billetes de 100",";",b100//50,"billetes de 50",";",b50//10,"billetes de 10",";",b10//5,"billetes de 5","y",b5//1,"billete de 1")
    

    
    
    