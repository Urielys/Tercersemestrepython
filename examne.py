'''
p = 0
arr = ["-1","-1","-1","-1","-1"]
nu = ["0","1","2","3","4","5","6","7","8","9"]
while(p<5):
    a = input('Escribe una cadena')
    r = True
    while (r==True):
        for x in nu:
            if a[0]==x:
                r = False
        if r == True:
            print("Dato incorrecto")
            r = False
        else:
            if arr[p]=="-1":
                arr[p]=a
                p +=1
            else:
                print("posicion ocupada")

for x in arr:
    print(arr)
'''
p = 0
arr = ["-1","-1","-1","-1","-1"]
while(p<=4):
    a = input('Escribe una cadena')
    r = True
    while (r==True):
        if a[0]=="0" or a[0]=="1" or a[0]=="2" or a[0]=="3" or a[0]=="4" or a[0]=="5" or a[0]=="6" or a[0]=="7" or a[0]=="8" or a[0]=="9":
            r = False
        else:
            print("Error")
            a = input('Escribe una cadena')
    if arr[p]=="-1":
        arr[p]=a
        p +=1

for x in arr:
    print(arr)