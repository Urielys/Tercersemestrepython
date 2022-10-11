
#arreglos en python

from curses.ascii import isdigit

def ValidarNumeros(a):
    c = 0
    x = 0
    for i in a:
        if isdigit(a[x]):
            c+=1
    x += 1
    if c == len(a):
        return True
    else:
        return False


def arreglo(po):
    res = "S"
    while res == "S" or res == "s":
        a = input("Valor")
        if ValidarNumeros(a):
            ar[po]=int(a)
            po += 1
        else:
            print("Error solo se permiten numeros")
        if  po < len(ar):
            res = input("Deseas otro valor s/n \n")
        else:
            mostrar()

def mostrar():
    for x in ar:
        if (x != 0):
            print(x," ")
po=0
ar=[0,0,0,0,0,0,0,0,0,0]
arreglo(po)
mostrar()