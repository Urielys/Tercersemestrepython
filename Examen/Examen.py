
a=[0,0,0,0,0,0,0,0,0,0,0,0]
p=1
aux=0
while(p==1):
    for x in a:
        e=float(input("Introdusca el sueldo ingresado en este mes: "))
        aux=aux+e
        if(e>0):
            print("")
        else:
            print("Solo numeros positivos\n")
            a[x]=[0]
    if (e>0):
        res=float(aux)/12
        print("El promedio anual es $ ",res)
        ter=input("quieres seguir si O no ")

    if(ter=="NO"):
        p+=1
        print("Que tenga un exxelente dia ._.")
    aux=0

