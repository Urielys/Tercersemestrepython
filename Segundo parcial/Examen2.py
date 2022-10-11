h=1
while(h==1):
    u=int(input("Introdusca el primer numero: "))
    d=int(input("\nIntrodusca el segundo numero: "))
    t=int(input("\nIntrodusca el tercer numero: "))
    p=u**2+d**2
    s=d**2
    a=t**2
    if(p+s==a):
        print("\nES CORRESTO\n")
    else:
        print("\nES INCORRESTO\n")


    ter=input("quieres seguir SI O NO: ")
    if(ter=="NO"):
        h+=1
        print("\nQue tenga un exelente dia ._.")
    else:
        print("\nPerfecto\n")