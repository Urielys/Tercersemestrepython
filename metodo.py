


def validar():
    a = input('Escribe un numero ')
    if len(a)==2:
        if a.isdigit:
            return a
        else:
            print('error')
            return validar()
    else:
        print('error')
        return validar()

def llenar():
    for x in range(2):
        for y in range(2):
            ar[x][y] = int(validar())

def mayor():
    aux = 0
    for x in range(2):
        for y in range(2):
            if aux<ar[x][y]:
                aux = ar[x][y]
    print('El mayor es: ',aux)

ar = [[0,0],[0,0]]
llenar()
mayor()
for i in ar:
    print(i)