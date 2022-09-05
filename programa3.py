
'''
programa que muestra en pantalla si eres mayor de edad

'''

def mayor(e):
    if e >= 18:
        print("Mayor")
    else:
        print("Menor")

valor = int(input("Escribe la edad de una persona"))
mayor( valor )


