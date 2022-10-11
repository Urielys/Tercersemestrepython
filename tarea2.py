
cont = 0
acum = 0
a =[0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    n=int(input("Escribe un numero entre 1-50: "))

    if(n>=1 and n<=50):
            if n%2==0:
                cont+=1
            else:
                acum+=1
    else:
        print("Este numero no esta dentro del rango\n"+"Inserte otro numero")
        cont-=1

print("La catidad de numeros pares es: ",cont)
print("La catidad de numeros inpares es: ",acum)