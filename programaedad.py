'''
def recursividad(a,p):
    print(p)
    if (len(a)==1):
        if a[0]=="0" or a[0]=="1" or a[0]=="2" or a[0]=="3" or a[0]=="4" or a[0]=="5" or a[0]=="6" or a[0]=="7" or a[0]=="8" or a[0]=="9":
            print("es numero")
            if arr[p]=="-1":
                arr[p]=a
                p += 1
                return p
            else:
                print("Posicion ocupada")
        else:
            print("Error")
            a = input('Escribe una cadena')
            recursividad(a,p)
    else:
        print("Error")
        a = input('Escribe una cadena')
        recursividad(a,p)
p = 0
arr = ["-1","-1","-1","-1","-1"]
#a = " "
while(p<=4):
    a = input('Escribe una cadena')
    p = recursividad(a,p)

for x in arr:
    print(arr)

'''
p=0
ar=[0,0,0,0]
while(p<4):
    a = input("escribe un numero")
    if len(a)==1:
        if a[0]=="0" or a[0]=="1" or a[0]=="2" or a[0]=="3" or a[0]=="4" or a[0]=="5" or a[0]=="6" or a[0]=="7" or a[0]=="8" or a[0]=="9":
            ar[p]=int(a)
            p +=1
        else:
            print("Error")
    else:
        print("Error")

for x in ar:
    print(ar)
