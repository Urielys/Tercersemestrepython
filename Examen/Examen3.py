m=1
while(m==1):
    p=int(input("Introdusca la cantidad de numeros que quiere debe ser positivo: "))
    h=1
    while(h<=p):
        f=int(input("Introdusca un numero mayor a 4: "))
        if(f>4):
            if(f%4==0):
                print("YES")
                h+=1
            else:
                print("NO")
                h+=1
        m+=1