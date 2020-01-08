"""BUSCAMINAS"""
import random
import os

"""
REFERENCIAS:
fil = filas
col = columnas
val = valor
elem = elemento
"""

def crea_tablero(fil, col, val):

    tablero=[]
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero

def muestra_tablero(tablero):
    print("* * * * * * * * * * * * * * * * * *")
    for fila in tablero:
        print("*", end=" ")
        for elem in fila:
            print(elem,end=" ")
        print("*")
    print("* * * * * * * * * * * * * * * * * *")

def coloca_minas(tablero, minas, fil, col):
    minas_ocultas=[]
    numero=0
    while numero<minas:
        y=random.randint(0,fil-1)
        x=random.randint(0,col-1)
        if tablero[y][x] !=9:
            tablero[y][x] =9
            numero += 1
            minas_ocultas.append((y,x))
    return tablero, minas_ocultas

def coloca_pistas(tablero, fil, col):
    for y in range(fil):
        for x in range(col):
            if tablero [y][x]==9:
                if x<col-1:
                    if tablero[y][x+1] !=9:
                        tablero[y][x+1]+=1
                if x>0:
                    if tablero[y][x-1]!=9:
                        tablero[y][x-1]+=1
                if y>0:
                    if tablero[y-1][x]!=9:
                        tablero[y-1][x]+=1
                if y<fil-1:
                    if tablero[y+1][x]!=9:
                        tablero[y+1][x]+=1
    return tablero

def tablero_completo(tablero,fil,col,val):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x]==val:
                return False
    return True

"""DESCUBRE MINAS"""
def rellenado(oculto,visible,y,x,fil,col,val):
    ceros=[(y,x)]
    while len(ceros)>0:
        y,x=ceros.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0<=y+1<=fil-1 and 0<=x+j<=col-1:
                    if visible[y+1][x+j]==val and oculto[y+i][x+j]==0:
                        visible[y+i][x+j]=0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i,x+j))
                        else:
                            visible[y+1][x+j]=oculto[y+1][x+j]
    return visible
                      

"""DISEÑO DEL TABLERO"""
def presentacion():
    os.system("cls")

    print("***************************************")
    print("*                                     *")
    print("*             BUSCAMINAS              *")
    print("*                                     *")
    print("*          w/a/s/d - moverse          *")
    print("*                                     *")
    print("*             m - mostrar             *")
    print("*                                     *")
    print("*        b/v - marcar/desmarcar       *")
    print("*                                     *")
    print("*                                     *")
    print("***************************************")
    print()
    input(" Presiona un botón para continuar ")

def menu():
    print()
    opcion=input("Presiona una opción: ")
    return opcion

"""ELECCIÓN DE DIFICULTAD-AGREGAR"""
columnas=16
filas=12

"""MINAS ESCONDIDAS"""
visible=crea_tablero(filas, columnas, "-")

"""MINAS DESCUBRIERTAS"""
oculto=crea_tablero(filas, columnas,0)
oculto, minas_ocultas=coloca_minas(oculto, 15, filas, columnas)
presentacion()
oculto=coloca_pistas(oculto,filas,columnas)

"""RELLENO ALEATORIO"""
y=random.randint(2, filas-3)
x=random.randint(2, columnas-3)

"""CURSOR 'X' EN EL TABLERO"""
real=visible[y][x]
visible[y][x]="x"
os.system("cls")
muestra_tablero(visible)
minas_marcadas=[]

"""MOVIMIENTOS"""
jugando=True
while jugando:
    mov=menu()

    if mov=="w":
        if y ==0:
            y=0
        else:
            visible[y][x]=real
            y-=1
            real=visible[y][x]
            visible[y][x]="x"

    elif mov=="s":
        if y==filas-1:
            y=filas-1
        else:
            visible[y][x]=real
            y+=1
            real=visible[y][x]
            visible[y][x]="x"

    elif mov=="d":
        if x==columnas-1:
            x=columnas-1
        else:
            visible[y][x]=real
            x+=1
            real=visible[y][x]
            visible[y][x]="x"

    elif mov=="b":
        if real=="-":
            visible[y][x]="#"
            real=visible[y][x]
        if (y,x) not in minas_marcadas:
                minas_marcadas.append((y,x))

    elif mov=="v":
        if real=="#":
            visible[y][x]="-"
            real=visible[y][x]
            if (y,x) in minas_marcadas:
                minas_marcadas.remove((y,x))    

    elif mov=="m":
        if oculto[y][x]==9:
            visible[y][x]="@"
            jugando=False

        elif oculto[y][x]!=0:
            visible[y][x]=oculto[y][x]
            real=visible[y][x]
        elif oculto[y][x]==0:
            visible[y][x]=0
            visible=rellenado(oculto, visible, y, x, "-")
            real=visible[y][x]

    os.system("cls")
    muestra_tablero(visible)

    ganas=False
    if tablero_completo(visible,filas,columnas,"-") and \
       sorted(minas_ocultas)==sorted(minas_marcadas) and\
       real!="-":
        ganas=True
        jugando=False

        if not ganas:
            print("¡PERDISTE! :(")
        else:
            print("¡GANASTE! :D")

            
