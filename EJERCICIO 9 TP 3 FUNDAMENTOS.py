AÑO=int(input("ingrese el año "))
A=AÑO/19
B=AÑO%4
C=AÑO%7
D=((AÑO*19)+24)%30
E=((B*2)+(C*4)+(D*6)+5)%7
PASCUA=D+E+22
if PASCUA<31:
    print("pascua cae el",PASCUA,"de marzo")
if PASCUA>31:
    print("pascua cae el",PASCUA-31,"de abril")
if PASCUA==31:
    print("pascua cae el", PASCUA,"de marzo")