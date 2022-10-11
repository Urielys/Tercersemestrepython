
cont = 0
acum = 0

def arreglo(x):

    n=int(input("Escribe un numero entre 1-50: "))

    if(n>=1 and n<=50):
        if((n%2)==0 and (n%2)==0):

            cont+=1

            if ((n%2)!=0 and (n%2)!=0):
                acum+=1

    else:
        print("Este numero no esta dentro del rango\n"+"Inserte otro numero")
        arreglo(a[x])


a =[0,0,0,0,0,0,0,0,0,0]
for x in range(0,10):
    arreglo(x)

print("La catidad de numeros pares es: ",cont)
print("La catidad de numeros inpares es: ",acum)
