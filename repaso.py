#hacer un programa que en un arreglo de 10 posiciones en las posiciones pares se alamcenen numeros pares y en las impares
#hacer un programa que llene un arreglo de 10 posiiones exclusivamnete con numeros de 1 a 50 el programa mostrara al final cuantos pares y cuantos impares se introdujeron
def validar(p):
    if a[p]==0:
        arreglo(p)

def arreglo(x):
    ban=True
    n=int(input("Escribe un numero diferente a 0 "))
    if(a[x]==0):
        if((x%2)==0 and (x%2)==0):
            a[x]=n
            if ((x%2)!=0 and (n%2)!=0):
                a[x]=n
                if(a[x]==0):
                    validar(x)



a =[0,0,0,0,0,0,0,0,0,0]
for x in range(0,10):
    arreglo(x)
    print(x+" "+a[x])