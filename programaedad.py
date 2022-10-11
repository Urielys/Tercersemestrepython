from platform import java_ver


def mostrar(e,s):
    if e>=18:
        if s=="hombre" or s=="mujer":
            print("Mayor de edad")
    elif e<18:
            print("Menor de edad")


for i in range(0,2):
    s = input("Escribe el sexo de la persona: ")
    n = input("Escribe el nombre de la persona: ")
    e = int(input("Escribe la edad de la persona: "))
mostrar(n+""+s+" "+e)

