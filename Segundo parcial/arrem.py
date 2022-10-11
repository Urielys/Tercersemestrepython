'''el programa realizara las siguientes operaciones
1-. encontrar el valor mas grande del arreglo
2-. encontrar la cantidad de numeros pares
3-. encontrar la cantidad de numeros primos
4-. calcular el promedio'''
from curses.ascii import isdigit


def validarNumeros2(a):
    if a.isdigit():
        return True
    else:
        return False

def validarNumeros(a):
    c =0
    for x in a:
        if isdigit(x):
            c+=1
    if c == len(a):
        return True
    else:
        return False

def promedio():
    suma =0
    for x in ar:
        suma += x
    pro = suma / 5
    print('El promedio es ',pro)

def primos():
    canp=0
    cp=0
    for y in ar:
        cp=0
        for x in range(1,y+1):
            if (y%x)==0:
                cp+=1
        if cp==2:
            canp+=1
    print("Los primos son ",canp)

def pares():
    pa=0
    for x in ar:
        p=x%2
        if p==0:
            pa+=1
    print("numeros pares ",pa)

def mayor():
    p=0
    m=0
    for x in ar:
        p=x
        if p>=m:
            m=p
    print("mayor ",m)



ar = []
b =0
con = 0
while(con<5):
    a = input('Escribe un numero')
    if (validarNumeros(a)):
        #print("solo son numeros ",con)
        b = int(a)
        ar.append(b)
        con +=1
    else:
        print("no son numeros")

promedio()
primos()
pares()
mayor()