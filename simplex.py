from math import *
from time import sleep
from numpy import *
from Tkinter import *

print 'A CONTINUACION INGRESE LOS DATOS DEL PROBLEMA A MINIMIZAR.'
print ''
def vuelva():
    print 'INGRESE LOS DATOS DE OTRO PROBLEMA:'
    print ''
    main()
def main():
    A=[]
    b=[]
    cont=0
    m=input('Ingrese el numero de filas de la matriz A:')
    n=input('Ingrese el numero de columnas de la matriz A:')
    for i in range(m):
        A.append([0]*(n))
    for i in range(m):
        b.append(0)
    for i in range(m):
        print'Ingrese los %d elementos de la fila %d:'%(n,i+1)
        for j in range(n):
            A[i][j]=input('')
        simb=raw_input('Escriba " <= " o " = " segun le corresponda a esta fila:')
        if '<='==simb:
            cont+=1
            for j in range (m):
                A[j].append(0)
            A[i][n-1+cont]=1
    print'Ingrese el vector b:'
    for i in range(m):
        b[i]=input('')
    print 'Ingrese el vector Costo'
    c=[]
    c1=[]
    for i in range(n+m):
        c.append(0)
        c1.append(0)
    for i in range(n):
        c[i]=input('')

    print 'El metodo simplex trabaja ahora de la siguiente forma:'
    print ''
    print 'Matriz A:'
    for i in range(m):
        print A[i]
    print ''
    print 'Vector b:'
    print b
    print ''
    print 'Vector Costo:'
    print c
    print ''
    simplex(A,b,m,n,c,c1)
def combi(A,m,n):
    B=[]
    for i in range(m):
        B.append([0]*(m))
    piv=[]
    for i in range(m):
        piv.append(0)
    todcom = []
    aux = [i for i in range(m)]
    cond = [k for k in range(n-m,n)]
    
    todcom = todcom + [guar(aux)]

    while todcom[-1]!=cond:
        if aux[-1]!=n-1:
            aux[-1] = aux[-1] + 1
            todcom = todcom +[guar(aux)]
        bolean,index = verif(todcom[-1],cond)
        if index == 0:
            break
        elif bolean == False and index!=0:
            aux = decen(todcom[-1],index)
            todcom = todcom + [guar(aux)]
    for i in range(len(todcom)):
        for j in range (m):
            piv[j]=todcom[i][j]
            for l in range (m):
                B[l][j]=A[l][todcom[i][j]]
        if linalg.det(B)!=0:
            break
    return B,piv
def guar(aux1):
    temp = []
    for t in range(len(aux1)):
        temp.append(aux1[t])
    return temp

def verif(arra,cond):
    m = len(arra)
    bolean = True
    k = -1
    for i in range(m):
        if arra[i]==cond[i]:
            k = i
            bolean = False
            break
    return bolean,k

def decen(arra,k):
    m = len(arra)
    temp = []
    for i in range(m):
        if i == k-1:
            temp = temp+[arra[i] + 1]
        elif i > k-1:
            temp = temp+[temp[i-1] + 1]
        else:
            temp = temp + [arra[i]]
    return temp

def simplex(A,b,m,n,c,c1):
    piv=[]
    for i in range(m):
        piv.append(0)
    B,piv=combi(A,m,n)
    print 'matriz B (inicial) tomada:'
    for i in range (m):
        print B[i]
    print ''
    no_acotado=1
    optimo=1
    u=[]
    cB=[]
    piv2=[]
    b1=[]
    a1_h=[]
    for i in range(m):
        u.append(0)
        cB.append(0)
        piv2.append(0)
        b1.append(0)
        a1_h.append(0)
    for i in range(m):
        cB[i]=c[piv[i]]
    while (optimo ==1) and (no_acotado==1):
        Bi=[]
        Bi=linalg.inv(B)
        B2=[]
        C=[]
        for i in range(n+m):
            C.append(0)
        for i in range(m):
            B2.append([0]*(m))
        for i in range(m):
            for j in range(m):
                B2[i][j]= '%.2f'%Bi[i][j]
        print 'B^(-1), inversa de B:'
        for i in range(m):
            print B2[i]
        print ''
        print 'cB:',cB
        print ''
        for i in range(m):
            suma=0
            for j in range(m):
                suma=suma+cB[j]*Bi[j][i]
            u[i]=suma
        for i in range(n+m):
            suma=0
            for j in range(m):
                suma=suma+u[j]*A[j][i]
            c1[i]=suma
        for i in range(m+n):
            c1[i]= c[i]-c1[i]
            if c1[i] < 10**(-14) and c1[i] > -10**(-14):
                c1[i]=0
        p=0
        for i in range(n+m):
            C[i]='%.2f'%c1[i]
        print 'vector de "Costos Reducidos":'
        print C
        print ''
        for j in range(n+m):
            if c1[j]<0:
                break
            else: p=j
        if p==(n+m-1):
            optimo = 0
            print 'Todos los elementos del Costo Reducido no son negativos, entonces:'
            print 'LA SOLUCION ES OPTIMA'
            print ''
        else:
            print 'Existe al menos un elemento del Costo Reducido menor que cero, entonces:'
            print 'LA SOLUCION AUN NO ES OPTIMA'
            print ''
            for h in range(n+m):
                if c1[h]<0:
                    break
            print 'Columna entrante "h" de la matriz A a la matriz B:',h+1
            print ''
            for i in range(m):
                suma=0
                for j in range(m):
                    suma=suma+Bi[i][j]*b[j]
                b1[i]=suma
            b2=[]
            for i in range (m):
                b2.append(0)
                b2[i]='%.2f'%b1[i]
            print 'Calculando b1=(B^(-1))*b:'
            print b2
            print ''
            for i in range(m):
                suma=0
                for j in range(m):
                    suma=suma+Bi[i][j]*A[j][h]
                a1_h[i]=suma
            b2=[]
            for i in range (m):
                b2.append(0)
                b2[i]='%.2f'%a1_h[i]
            print 'Calculando(B^(-1))*a_(%d), siendo a_(%d) la columna %d de a'%(h+1,h+1,h+1)
            print b2
            print ''
            p=0
            for i in range(m):
                if a1_h[i]>0:
                    break
                else: p=i
            if p==(m-1):
                print 'Todos los elementos del resultado anterior no son positivos, entonces:'
                print 'LA SOLUCION NO ESTA ACOTADA'
                print ''
                no_acotado=0
            else:
                
                for i in range(m):
                    if a1_h[i]>0:
                        minimo= b1[i]*(a1_h[i]**(-1))
                        r=i
                        break
                for j in range(i+1,m):
                    if a1_h[j]>0:
                        if (b1[j]*(a1_h[j]**(-1))) < minimo:
                            minimo = b1[j]*(a1_h[j]**(-1))
                            r=j
                print 'Columna saliente "r" de la matriz B:',r+1
                print ''
                for i in range(m):
                    B[i][r]=A[i][h]
                print 'Haciendo el cambio de la columna %d de B con la columna %d de  A'%(r+1,h+1) 
                print 'Matriz B mejorada:'
                for i in range(m):
                    print B[i]
                print ''
                cB[r]=c[h]
                piv[r]=h
                for i in range(m):
                    piv2[i]=piv[i]+1

    if optimo ==0:
        for i in range(m):
            suma=0
            for j in range(m):
                suma=suma+Bi[i][j]*b[j]
            b1[i]=suma
        x=[]
        for i in range(m+n):
            x.append(0)
        for i in range(m):
            x[piv[i]]='%.3f'%b1[i]
        print 'Solucion:'
        print x[0:n]
        print ''
    conf=raw_input ('Diga SI o NO si desea continuar con mas problemas:')
    if 'SI' == conf:
        vuelva()
    else:
        print 'LA TAREA HA FINALIZADO'
main()
