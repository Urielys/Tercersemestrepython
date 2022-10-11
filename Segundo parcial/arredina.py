

def validarnumero(a):
    print("Numeros")
def validarletras(a):
    print("Letras")
def validareales(a):
    print("Numero con decimales")

def llenar():
    a = input("Escribe un valor o dato ")
    if(validarnumero(a)):
        numeros.append(int(a))
    elif(validarletras(a)):
        letras.append(a)
    elif(validareales(a)):
        Flotantes.append(float(a))
    res = input("Desea ingresar otro valo/dato\n")
    if (res=="S" or res=="si"):
        llenar()

def multNL():
    if len(numeros)==len(letras):
        for x in letras:
            letras2.append(len(x))
        for x in range(0,len(numeros)):
            print(letras2[x],"*",numeros[x],"*",letras2[x]*numeros[x])
    else:
        print("Los arreglos no son del mismo tamaño")

letras2=[]
numeros = []
letras = []
Flotantes = []
llenar()
op=1
while(op!=4):
    print("Menu")
    print("1-. N * L ")
    print("2-. N* D ")
    print("3-. L * D")
    print("4-. Salir")
    o = input("Elige una opcion")
    if (validarnumero(o)):
        op = int(o)
        if op==1:
            multNL()
        elif op==2:
            multND()
        elif op==3:
            multLD()
    else:
        print("ERROR DE OPCION\n")