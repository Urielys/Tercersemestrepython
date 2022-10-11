#hacer un proma que pida un numero conprendido entre 5 - 20 de lo controrario se volveraa pedir.el programa mostrara
#todos los numero pares que se encuentran entre 0 y el numero escrito

a=1
while(a<5 or a>20):
    a=int(input("Escribe un numero entre 5-20:"))
    b=0
    if(a>=5 and a<=20):
        if((a%2)==0):
            while(b<a):
                b+=2
                print(b)
        else:
            c=a-1
            while(b<c):
                b+=2
                print(b)
        break
    else:
        print(a,"","Este numero no esta en el rango ingrese otro numero")

