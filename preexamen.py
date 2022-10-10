'hacer un programa que llene una matriz de 3 por 3 exclusivamente de numero pares, y otra matriz de numeros inpares'
'el programa mostrara la multiplicasion del valor mayor y menos de las 2 matrices y ademas guardara en un'
'arreglo los numeros primos que existan en las dos matrices'

print('----------------------------Primera matriz-------------------')
def validar1():
    a = int(input('Escribe un numero par: '))
    if a%2==0:
            return a
    else:
        print('error')
        return validar1()

def llenar1():
    for x in range(3):
        for y in range(3):
            ar[x][y] = int(validar1())

def validar():
    a = int(input('Escribe un numero inpar: '))
    if a%2:
            return a
    else:
        print('error')
        return validar()

def llenar():
    for x in range(3):
        for y in range(3):
                arr[x][y] = int(validar())

def mult():
    if len(ar)==len(arr):
        for x in range(3):
            for y in range(3):
                res[x][y] = ar[x][y]*arr[x][y]
    else:
        print("Los arreglos no son del mismo tamaño")

def mayor():
    aux = 0
    aux1 = 0
    for x in range(3):
        for y in range(3):
            if aux<ar[x][y]:
                aux = ar[x][y]
    for x in range(3):
        for y in range(3):
            if aux1<arr[x][y]:
                aux1 = arr[x][y]
    mu = aux*aux1
    print('Mayor de pares: ',aux)
    print('Mayor de inpares: ',aux1)
    print('Multiplicacion de mayores: ',mu)

def menor():
    aux = 1000
    aux1 = 1000
    for x in range(3):
        for y in range(3):
            if aux>ar[x][y]:
                aux = ar[x][y]
    for x in range(3):
        for y in range(3):
            if aux1>arr[x][y]:
                aux1 = arr[x][y]
    mu = aux*aux1
    print('Menor de los pares: ',aux)
    print('Menor de los inpares: ',aux1)
    print('Multiplicacion de menores: ',mu)

def matrizP():
    for x in range(3):
        for y in range(3):
            cont=0
            cont1=0
            for i in range(2,ar[x][y]):
                if ar[x][y]%i==0:
                    cont+=1
            for z in range(2,arr[x][y]):
                if arr[x][y]%z==0:
                    cont1+=1
            if cont==0:
                arre.append(ar[x][y])
            if cont1==0:
                arre.append(arr[x][y])

ar = [[0,0,0],[0,0,0],[0,0,0]]
arr = [[0,0,0],[0,0,0],[0,0,0]]
res = [[0,0,0],[0,0,0],[0,0,0]]
arre = []
llenar1()
print('----------------------------Segunda matriz-------------------')
llenar()
mult()
print('Primer matriz')
for i in ar:
    print(i)
print('Segunda matriz')
for i in arr:
    print(i)
mayor()
menor()
matrizP()
print('Matriz de numeros primos')
for i in arre:
    print([i])
print('Matriz resultante')
for i in res:
    print(i)




