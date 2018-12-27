from math import *
from time import sleep
from Tkinter import *
A=[]
m=input('ingrese el numero de filas:')
n=input('ingrese el numero de columnas:') 
for i in range(m):
    A.append([0]*(n+1))
for i in range(m):
    print'ingrese los %d elementos de la fila %d:'%(n,i+1)
    for j in range(n):
        A[i][j]=input('')
print'ingrese el vector b:'
for i in range(m):
    A[i][n]=input('')
def multip(M1,M2,m,q,n):
    M3=[]
    for l1 in range (m):
        M3.append([0]*(n))

    for x in range (m):
        for y in range (n):
            suma=0
            for z in range (q):
                suma=suma+M1[x][z]*M2[z][y]
            M3[x][y]=suma
    return M3

def gauss():
    vent = Tk()
    vent.title('Eliminacion por metodo de Gauss')
    bot1 = Button(vent,text="Eliminacion de Gauss sin pivoteo",relief=SOLID,command= gaussnormal)
    bot1.grid(row=1,column=1)
    bot2 = Button(vent,text="Eliminacion de Gauss con pivoteo parcial",relief=SOLID,command= gausspp)
    bot2.grid(row=2,column=1)
def gaussnormal():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append([0])
    print 'GAUSS SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    print 'La matriz escalonada ampliada es:'
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=i+1
            mayor = M[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(M[j][i])):
                    mayor= M[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=M[i][l]
                M[i][l]=M[p][l]
                M[p][l]=Q[l]  
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] = M[j][k] - (w*M[i][k])
                M[j][i]=0
        print M[i]
    x=[]
    for s in range (n):
        x.append(0)
    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= M[j][k]*x[k]
        x[j]=(M[j][n]-suma)/M[j][j]
    print 'la solucion del sistema es:'
    print x
    
def gausspp():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append([0])
    print 'GAUSS CON PIVOTEO PARCIAL'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    print 'La matriz escalonada ampliada es:'
    for i in range (n):
        j=i
        p=i
        mayor = M[j][i]
        for j in range (i+1,n):
            if(abs(mayor) < abs(M[j][i])):
                mayor= M[j][i]
                p = j
        for l in range (i,n+1):
            Q[l]=M[i][l]
            M[i][l]=M[p][l]
            M[p][l]=Q[l]  
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
        print M[i]
    x=[]
    for s in range (n):
        x.append(0)
    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= M[j][k]*x[k]
        x[j]=(M[j][n]-suma)/M[j][j]
    print 'la solucion es:'
    print x
    
def gaussjordan():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append(0)
    print 'la matriz ampliada es:'
    for i in range(n):
        print M[i]
    print "matriz escalonada(ampliada):"
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=i+1
            mayor = M[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(M[j][i])):
                    mayor= M[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=M[i][l]
                M[i][l]=M[p][l]
                M[p][l]=Q[l]
        for j in range (0,i):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
    for i in range (n):
        print M[i]
    x=[]
    for s in range (n):
        x.append([0])
    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for j in range (n-2,-1,-1):
        v=0
        for k in range (j+1,n):
            v+= M[j][k]*x[k]
        x[j]=(M[j][n]-v)/M[j][j]
    print 'la solucion es:'
    print x

def croutLU1():
    venta = Tk()
    venta.title('Metodo de Crout LU1')
    boto1 = Button(venta,text="Crout LU1 sin pivoteo",relief=SOLID,command= croutLU1normal)
    boto1.grid(row=1,column=1)
    boto2 = Button(venta,text="Crout LU1 con pivoteo parcial",relief=SOLID,command= croutLU1pp)
    boto2.grid(row=2,column=1)
def croutLU1normal():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    U = []
    print 'CROUT LU1 SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        U.append([0]*(n))
    p = 0
    for i in range (n):
        U[i][i]=float(1)
    for i in range (n):
        for j in range(i,n):
            suma=0
            for p in range (0,i):
                suma=suma+L[j][p]*U[p][i]
            L[j][i] = M[j][i] - suma  
        for j in range(i+1,n):
            suma=0
            for p in range (0,i):
                suma=suma+L[i][p]*U[p][j]
            U[i][j]=(M[i][j]-suma)*(L[i][i])**(-1)
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz U es:"
    for i in range (n):
        print U[i]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]                     
    for s in range (n):
        y.append(0)
        
    y[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n,1):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*y[k]
        y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    x[n-1]=y[n-1]/U[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma= suma+ U[j][k]*x[k]
        x[j]=(y[j]-suma)*(U[j][j]**(-1))
    print 'la solucion es:'
    print x
    
def croutLU1pp():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    Q = []
    p = 0
    L = []
    U = []
    print 'CROUT LU1 CON PIVOTEO PARCIAL'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        U.append([0]*(n))
    for i in range (n):
        U[i][i]=float(1)
    for i in range (n+1):
        Q.append(0)
    for k in range (n):
        p=-1
        mayor=0
        for i in range (k,n):
            if(mayor < abs(M[i][k])):
                mayor=abs(M[i][k])
                p=i
        Q=M[k]
        M[k]=M[p]
        M[p]=Q
        for i in range(k,n):
            suma=0
            for p in range (k):
                suma=suma+L[i][p]*U[p][k]
            L[i][k]=M[i][k]-suma
        for i in range(k,n):
            suma=0
            for p in range (0,i):
                suma=suma+L[k][p]*U[p][i]
            U[k][i]=(M[k][i]-suma)*(L[k][k])**(-1)
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz U es:"
    for i in range (n):
        print U[i]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    y[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n,1):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*y[k]
        y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    x[n-1]=y[n-1]/U[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= U[j][k]*x[k]
        x[j]=(y[j]-suma)*(U[j][j]**(-1))
    print 'la solucion es:'
    print x

def croutL1U():
    ven = Tk()
    ven.title('Metodo de Crout L1U')
    bo1 = Button(ven,text="Crout L1U sin pivoteo",relief=SOLID,command= croutLU1normal)
    bo1.grid(row=1,column=1)
def croutL1Unormal():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    U = []
    print 'CROUT L1U SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        U.append([0]*(n))
    suma = 0
    p = 0
    for i in range (n):
        for j in range (n):
            L[i][j]=0
            U[i][j]=0
    for i in range (n):
        L[i][i]=float(1)
    for i in range (n):
        for j in range(i,n):
            suma =0
            for p in range (0,i):
                suma=suma+L[i][p]*U[p][j]
            U[i][j]=M[i][j]-suma  
        for j in range(i+1,n):
            suma=0
            for p in range (0,i):
                suma=suma+L[j][p]*U[p][i]
            L[j][i]=(M[j][i]-suma)*(U[i][i])**(-1)
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz U es:"
    for i in range (n):
        print U[i]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    y[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n,1):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*y[k]
        y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    x[n-1]=y[n-1]/U[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= U[j][k]*x[k]
        x[j]=(y[j]-suma)*(U[j][j]**(-1))
    print 'la solucion es:'
    print x
    
def LDLT():
    ve = Tk()
    ve.title('Factorizacion LDLt')
    bott1 = Button(ve,text="LDLt sin pivoteo",relief=SOLID,command= LDLTnormal)
    bott1.grid(row=1,column=1)
def LDLTnormal():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    D = []
    LT = []
    DLT = []
    print 'METODO LDLt SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range(n):
        L.append([0]*(n))
        D.append([0]*(n))
        LT.append([0]*(n))
        DLT.append([0]*(n))
    for i in range(n):
        L[i][i]=1
    for k in range (n):
        suma = 0
        for p in range(k):
            suma = suma + (L[k][p]**2)*D[p][p]
        D[k][k] = M[k][k] - suma
        for i in range(k+1,n):
            suma = 0
            for p in range (k):
                suma = suma + M[i][p]*M[k][p]*(D[p][p]**(-1))
            L[i][k] = (M[i][k] - suma)*(D[k][k]**(-1))
    for i in range(n):
        for j in range (n):
            LT[i][j]= L[j][i]
    for i in range (n):
        for j in range (n):
            for k in range (n):
                DLT[i][j] = DLT[i][j] + D[i][k]*LT[k][j]
    print 'La matriz L es:'
    for i in range(n):
        print L[i]
    print 'La matriz D es:'
    for i in range(n):
        print D[i]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    y[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n,1):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*y[k]
        y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    x[n-1]=y[n-1]/DLT[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= DLT[j][k]*x[k]
        x[j]=(y[j]-suma)*(DLT[j][j]**(-1))
    print 'la solucion es:'
    print x

def cholesky():
    v = Tk()
    v.title('Factorizacion de Cholesky')
    bottt1 = Button(v,text="Cholesky sin pivoteo",relief=SOLID,command= choleskynormal)
    bottt1.grid(row=1,column=1)
def choleskynormal():
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    G = []
    GT = []
    print 'METODO DE CHOLESKY SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range(n):
        G.append([0]*(n))
    for i in range(n):
        GT.append([0]*(n))    
    for k in range (n):
        suma = 0
        for p in range (k):
            suma = suma + (G[k][p])**2
        G[k][k] = sqrt(M[k][k] - suma)
        for i in range(k+1,n):
            suma = 0
            for p in range (k):
                suma = suma + (G[i][p] * G[k][p])
            G[i][k] = (M[i][k] - suma)/G[k][k]
    print 'la matriz G es:'
    for i in range(n):
        print G[i]
    for i in range(n):
        for j in range (n):
            GT[i][j]= G[j][i]       
    x=[]
    for s in range (n):
        x.append([0])
    y=[]
    for s in range (n):
        y.append([0])
    y[0]=M[0][n]*(G[0][0]**(-1))
    for j in range (1,n,1):       
        suma=0
        for k in range (j):
            suma+= G[j][k]*y[k]
        y[j]=(M[j][n]-suma)*(G[j][j]**(-1))
    x[n-1]=y[n-1]/GT[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= GT[j][k]*x[k]
        x[j]=(y[j]-suma)*(GT[j][j]**(-1))
    print 'la solucion es:'
    print x
    
def aasen():
    windows = Tk()
    windows.title('Metodo de Aasen')
    boo1 = Button(windows,text="Sin pivoteo",relief=SOLID,command = aasennormal)
    boo1.grid(row=1,column=1)
    boo2 = Button(windows,text="Con pivoteo parcial",relief=SOLID,command = aasenpp)
    boo2.grid(row=1,column=2)
def aasennormal():
    M = []
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    T = []
    h = []
    l = []
    v = []
    Lt = []
    TLt = []
    print 'METODO DE AASEN SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        T.append([0]*(n+1))
        Lt.append([0]*(n))
        TLt.append([0]*(n))
    for i in range (n):
        h.append(0)
        v.append(0)
        l.append(0)
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append(0)
    for i in range (n):
        L[i][i]=1
    for j in range (n):
        if j==0:
            h[0]=M[0][0]
        else:
            if j==1:
                h[0]=T[1][0]
                h[1]=M[1][1]
            else:
                l[0]=0
                for k in range (1,j):
                    l[k]=L[j][k]
                l[j]=1
                h[j]=M[j][j]
                h[0]=T[0][0]*l[0]+T[1][0]*l[1]
                h[j]=h[j]-l[0]*h[0]
                for k in range (1,j):
                    h[k]= T[k][k-1]*l[k-1]+T[k][k]*l[k]+T[k+1][k]*l[k+1]
                    h[j]=h[j]-l[k]*h[k]
        if j==0 or j==1:
            T[j][j]=h[j]
        else:
            T[j][j]=h[j]-T[j][j-1]*L[j][j-1]
        if j <(n-1):
            for r in range (j+1,n):
                suma=0
                for k in range (0,j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            T[j+1][j]=T[j][j+1]=v[j+1]
        if j<(n-2):
            for k in range (j+2,n):
                L[k][j+1]=v[k]*(v[j+1]**(-1))
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz T es:"
    for i in range (n):
        print T[i][0:n]
    z=[]
    for i in range (n):
        z.append(0)
    z[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    for i in range(n):
        T[i][n]=z[i]
    p=0
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=T[i][l]
                T[i][l]=T[p][l]
                T[p][l]=Q[l]  
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=T[n-1][n]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(T[j][n]-suma)/T[j][j]
    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    x=[]
    for i in range (n):
        x.append(0)
    x[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*x[k]
        x[j]=(W[j]-suma)*(Lt[j][j]**(-1))
    print 'la solucion es:'
    print x
def aasenpp():
    M = []
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    T = []
    h = []
    l = []
    v = []
    Lt = []
    TLt = []
    print 'METODO DE AASEN CON PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        T.append([0]*(n+1))
        Lt.append([0]*(n))
        TLt.append([0]*(n))
    for i in range (n):
        h.append(0)
        v.append(0)
        l.append(0)
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Q1=[]
    for s in range (n):
        Q.append(0)
    for i in range (n):
        L[i][i]=1
    I=[]
    for i in range (n):
        I.append([0]*(n))
    for i in range (n):
        I[i][i]=1
    for j in range (n):
        P=[]
        for k in range (n):
            P.append([0]*(n))
        for k in range (n):
            P[k][k]=1
        if j==0:
            h[0]=M[0][0]
        else:
            if j==1:
                h[0]=T[1][0]
                h[1]=M[1][1]
            else:
                l[0]=0
                for k in range (1,j):
                    l[k]=L[j][k]
                l[j]=1
                h[j]=M[j][j]
                h[0]=T[0][0]*l[0]+T[1][0]*l[1]
                h[j]=h[j]-l[0]*h[0]
                for k in range (1,j):
                    h[k]= T[k][k-1]*l[k-1]+T[k][k]*l[k]+T[k+1][k]*l[k+1]
                    h[j]=h[j]-l[k]*h[k]
        if j==0 or j==1:
            T[j][j]=h[j]
        else:
            T[j][j]=h[j]-T[j][j-1]*L[j][j-1]
            
        if j <(n-1):
            p=j+1
            for r in range (j+1,n):
                suma=0
                for k in range (0,j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            mayor =v[j+1]
            for k in range (j+2,n):
                if mayor < abs(v[k]):
                    p=k
            q=v[p]
            v[p]=v[j+1]
            v[j+1]=q
            Q1=P[p]
            P[p]=P[j+1]
            P[j+1]=Q1
            for k in range (2,j+1):
                q=L[j+1][k]
                L[j+1][k]=L[p][k]
                L[p][k]=q

            for k in range (j+1,n):
                q=M[j+1][k]
                M[j+1][k]=M[p][k]
                M[p][k]=q
            for k in range (j+1,n):
                q=M[k][j+1]
                M[k][j+1]=M[k][p]
                M[k][p]=q
            T[j+1][j]=T[j][j+1]=v[j+1]
        if j<(n-2):
            for k in range (j+2,n):
                L[k][j+1]=v[k]
            if v[j+1]!=0:
                for k in range (j+2,n):
                    L[k][j+1]=L[k][j+1]*(v[j+1]**(-1))
            print 'L:',L
        I=multip(P,I,n)
    print "la matriz L es:"
    for i in range (n):
        print L[i][0:n]
    print "La matriz T es:"
    for i in range (n):
        print T[i][0:n]
    print 'La matriz P es:'
    for i in range (n):
        print I[i]
    IT=[]
    for i in range (n):
        IT.append([0]*(n))
    for i in range (n):
        for j in range (n):
            IT[i][j]=I[j][i]
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Lt=[]
    for s in range (n):
        Lt.append([0]*n)    
    z=[]
    for i in range (n):
        z.append(0)
    B=[]
    for i in range(n):
        B.append(0)
    for i in range (n):
        suma=0
        for j in range (n):
            suma=suma+I[i][j]*M[j][n]
        B[i]=suma
    z[0]=B[0]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(B[j]-suma)*(L[j][j]**(-1))
    
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            
            Q=T[i]
            T[i]=T[p]
            T[p]=Q
            k=z[i]
            z[i]=z[p]
            z[p]=k
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
            z[j] = z[j] - (w*z[i])


    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=z[n-1]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(z[j]-suma)/T[j][j]

    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    y=[]
    for i in range (n):
        y.append(0)
    y[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*y[k]
        y[j]=(W[j]-suma)*(Lt[j][j]**(-1))

    x=[]
    for i in range (n):
        x.append(0)
    for j in range(n):
        suma = 0
        for l in range(n):
            suma=suma+IT[l][j]*y[l]
        x[j]=suma
    print 'la solucion del sistema es '
    print x

def inversa(M,n):
    I=[]
    for i in range (n):
        I.append([0]*(n))
    for i in range (n):
        I[i][i]=1
    mayor=0
    Q=[]
    Q1=[]
    for s in range (n):
        Q.append(0)
        Q1.append(0)
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=i+1
            mayor = M[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(M[j][i])):
                    mayor= M[j][i]
                    p = j
            Q=M[i]
            M[i]=M[p]
            M[p]=Q
            Q1=I[i]
            I[i]=I[p]
            I[p]=Q1
        for j in range (0,i):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
            for k in range (n):
                I[j][k] =I[j][k] - (w*I[i][k])
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
            for k in range (n):
                I[j][k] =I[j][k] - (w*I[i][k])
    for i in range (n):
        I[i][i]=I[i][i]*(M[i][i])**(-1)
    return I
def ParletReid():
    I=[]
    P=[]
    M=[]
    L=[]
    U=[]
    T=[]
    G=[]
    F=[]
    S=[]
    PP=[]
    W=[]
    PPT=[]
    b=[]
    for i in range (n):
        I.append([0]*(n))
        PPT.append([0]*(n))
        P.append([0]*(n))
        W.append([0]*(n))
        M.append([0]*(n))
        L.append([0]*(n))
        PP.append([0]*(n))
        U.append([0]*(n+1))
        T.append([0]*(n+1))
        S.append([0]*(n+1))
        G.append(0)
        F.append(0)
        b.append(0)
        P[i][i]=1
        PP[i][i]=1
        I[i][i]=1
        W[i][i]=1
    for i in range(n):
        L[i][i]=1
    for i in range(n):
        for j in range(n+1):
            T[i][j]=A[i][j]
    print 'METODO PARLET-REID'
    print " La matriz ampliada es:"
    for i in range(n):
        print T[i]
   #algoritmo#
    for i in range(n-2):
        P=[]
        for j in range (n):
            P.append([0]*(n))
            P[j][j]=1
        for j in range(n):
            for k in range(n):
                S[j][k] = I[j][k]
        #Pivoteo#
        p = i+1       
        mayor = abs(T[i+1][i])
        for j in range (i+2,n):    
            if mayor < abs(T[j][i]):
                mayor = abs(T[j][i])
                p = j
        P[i+1] = S[p]
        P[p] = S[i+1]       
    #multiplicacion PAPT#
        F=T[i+1]
        T[i+1] = T[p]
        T[p] = F        
        for j in range(n):
            for k in range(n+1):
                U[j][k] = T[j][k]       
        for j in range (n):
            for k in range (n):
                suma = 0
                for l in range (n):
                    suma = suma + U[j][l]*P[k][l]
                T[j][k] = suma
    #Gauss#
        for j in range (n):
            G[j]=0
            U.append([0]*(n+1))
        for j in range (i+2,n):
            G[j] = U[j][i]*(U[i+1][i]**(-1))        
    #matriz de gaus#
        for j in range (n):
            for l in range (n):
                M[j][l] = S[j][l] - G[j]*I[i+1][l]       
    #multiplicacion MPAPTMT#                
        for j in range(n):
            for k in range(n+1):
                U[j][k] = T[j][k]        
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    suma = suma  + M[j][l]*U[l][k]
                T[j][k] = suma
        for j in range(n):
            for k in range(n+1):
                U[j][k] = T[j][k]        
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    suma = suma  + U[j][l]*M[k][l]
                T[j][k] = suma
        
    #EL P TOTAL#
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    suma = suma + P[j][l]*W[l][k]
                PP[j][k] = suma
        for j in range (n):
            for k in range(n):
                W[j][k]=PP[j][k]
    #M2P2M1P1#
        L= multip(multip(M,P,n),L,n)            
    for j in range(n):
        for k in range(n):
            PPT[j][k]=PP[k][j]
    L=multip(L,PPT,n,n,n)
    L=inversa(L,n)
    print 'La matriz L es:'
    for i in range (n):
        print L[i]
    print 'La matriz tridiagonal T es:'
    for i in range (n):
        print T[i][0:n]
    print 'La matriz P es:'
    for i in range (n):
        print PP[i]
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Lt=[]
    for s in range (n):
        Lt.append([0]*n)    
    z=[]
    for i in range (n):
        z.append(0)
    z[0]=T[0][n]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(T[j][n]-suma)*(L[j][j]**(-1))
    
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            
            Q=T[i]
            T[i]=T[p]
            T[p]=Q
            k=z[i]
            z[i]=z[p]
            z[p]=k
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
            z[j] = z[j] - (w*z[i])


    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=z[n-1]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(z[j]-suma)/T[j][j]

    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    y=[]
    for i in range (n):
        y.append(0)
    y[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*y[k]
        y[j]=(W[j]-suma)*(Lt[j][j]**(-1))

    x=[]
    for i in range (n):
        x.append(0)
    for j in range(n):
        suma = 0
        for l in range(n):
            suma=suma+PPT[j][l]*y[l]
        x[j]=suma
    print 'la solucion del sistema es '
    print x
def GS():
    E=[]
    U=[]
    suma=0
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(m):
        for j in range(n+1):
            M[i][j]=A[i][j]
    print 'METODO DE GRAM-SCHIMDT'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range(m):
        E.append([0]*(n))
        U.append([0]*(n))
    
    for j in range(n):
        for k in range(m):
            E[k][j]=M[k][j]
        for i in range(j):
            suma = 0
            for k in range(m):
                suma = suma + E[k][i]*E[k][j]
            U[i][j] = suma
            for k in range(m):
                E[k][j]=E[k][j] - U[i][j]*E[k][i]
                    
        suma = 0
        for k in range(m):
            suma = suma + (E[k][j])**2
        U[j][j] = (suma)**(0.5)
        
        for k in range(m):
            E[k][j]=E[k][j]*(U[j][j])**(-1)
    print 'La matriz ortogonalizada E por columnas es:'
    for i in range (m):
        print E[i][0:n]
        
    print 'la matriz U es:'
    print U
    #solucion del sistema Ux=ETb#
    b=[]
    for i in range(n):
        b.append(0)
    for i in range (n):
        suma=0
        for j in range (m):
            suma=suma+E[j][i]*M[j][n]
        b[i]=suma
    x=[]
    for s in range (n):
        x.append(0)
    x[n-1]=b[n-1]/U[n-1][n-1]
    for j in range (n-2,-1,-1):
        v=0
        for k in range (j+1,n):
            v+= U[j][k]*x[k]
        x[j]=(b[j]-v)*(U[j][j]**(-1))
    print 'la solucion del sistema es:'
    print x
def Householder():
    M=[]
    for i in range (m):
        M.append([0]*(n+1))
    for i in range(m):
        for j in range(n+1):
            M[i][j]=A[i][j]
    print 'METODO DE HOUSEHOLDER'
    print " La matriz ampliada es:"
    for i in range(m):
        print M[i]
    b=[]
    for i in range(m):
        b.append(0)
    for i in range(m):
        b[i]=A[i][n]
    X=[]
    for i in range(n):
        X.append(0)
    w = [0]*m
    for j in range (n):
        #sacamos maximo de columnas
        MaxCol = M[j][j]
        for k in range(j+1,m):
            MaxCol = max(MaxCol, M[k][j])
        if MaxCol==0:
            break
        psum = 0
        for k in range (j,m):
            psum = psum + M[k][j]*M[k][j]
        ssign = copysign(1,M[j][j])
        sigma = sqrt(psum)*ssign
        for k in range (j,m):
            w[k] = M[k][j]
        w[j] = w[j]+sigma
        betha = 0
        psum = 0
        for k in range(j,m):
            psum = psum+ w[k]*w[k]
        betha = float(2/psum)
        M[j][j] = -sigma
        for l in range(j+1,n):
            s = 0
            for k in range(j,m):
                s = s+w[k]*M[k][l]
            for k in range(j,m):
                M[k][l] = M[k][l]-w[k]*s*betha
        #Transformar vector B
        s = 0
        for k in range(j,m):
            s = s+w[k]*b[k]
        for k in range(j,m):
            b[k] = b[k] - w[k]*s*betha
     
    #limpiar Matriz A
    for x in range(n):
        for y in range(n):
            if x>y:
                M[x][y]=0
    for x in range(n,m):
        for y in range(n):
            M[x][y]=0
    print 'la matriz reducida es:'
    for i in range(m):
        print M[i][0:n]
    #solucion RX=b
    for j in range(n-1,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma=suma+M[j][k]*X[k]
        X[j]=(b[j]-suma)*(M[j][j]**(-1))
    print 'la solucion del sistema es:'
    print X     
    res = 0
    #suma de residuos al cuadrado
    for k in range(n,m):
        res = res + b[k]*b[k]
    print 'la suma de residuos al cuadrado es:'
    print res
def Givens():
    M=[]
    for i in range (m):
        M.append([0]*(n+1))
    for i in range(m):
        for j in range(n+1):
            M[i][j]=A[i][j]
    print 'METODO DE GIVENS'
    print " La matriz ampliada es:"
    for i in range(m):
        print M[i]
    b=[]
    x=[]
    for i in range(m):
        b.append(0)
    for i in range(n):
        x.append(0)
    for i in range(m):
        b[i]=A[i][n]
    t=0
    c=0
    s=0
    aux=0
    for i in range(n):
        for k in range(i+1,m):
            #hacer nulo el elemento (k,i)
            if M[k][i]!=0:
                if abs(M[k][i])>= abs(M[i][i]):
                    t=M[i][i]*(M[k][i])**(-1)
                    s=sqrt(1+(t)**2)**(-1)
                    c=s*t
                else:
                    t=M[k][i]*(M[i][i])**(-1)
                    c=sqrt(1+(t)**2)**(-1)
                    s=c*t
                M[i][i]=c*M[i][i]+s*M[k][i]
                for j in range(i+1,n):
                    aux=c*M[i][j]+s*M[k][j]
                    M[k][j]= (-s*M[i][j])+c*M[k][j]
                    M[i][j]=aux
                #transformacion del vector b#
                aux=c*b[i]+s*b[k]
                b[k]= (-s*b[i])+c*b[k]
                b[i]=aux
    #limpiar Matriz A
    print b
    for i in range(n):
        for j in range(n):
            if i>j:
                M[i][j]=0
    for i in range(n,m):
        for j in range(n):
            M[i][j]=0
    print 'la matriz reducida es:'
    for i in range (m):
        print M[i][0:n]
    #solucion#
    print 'el vector b transformado es:'
    print b
    for j in range(n-1,-1,-1):
        suma=0
        for k in range(j+1,n):
            suma = suma + M[j][k]*x[k]
        x[j]=(b[j]-suma)*((M[j][j])**(-1))

    print 'la solucion es:' 
    print x
    #residuo al cuadrado#
    res=0
    for k in range(n+1,m):
        res=res+(b[k])**2
    print 'residuos al cuadrado'
    print res
def jacobi():
    M=[]
    for i in range (n):
        M.append([0]*(n))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    b=[]
    for s in range (n):
        b.append(0)
    for i in range(n):
        b[i]=A[i][n]
    sm=1.0
    tol = input('ingrese el TOL que desea usar:')
    print 'los cambios que van haciendo en la solucion del sistema:'
    while sm > tol:
        s1=0
        for i in range(n):
            su=b[i]
            for j in range(0,i):
                su=su-M[i][j]*x[j]
            for j in range (i+1,n):
                su=su-M[i][j]*x[j]
            y[i]=su*(M[i][i]**(-1))
            s1=max(s1,abs(y[i]))
        sm=0
        for i in range(n):
            sm=max(abs(x[i]-y[i])*(s1**(-1)),sm)
            x[i]=y[i]
        print x
    print 'la ultima linea es la solucion del sistema'

def GaussSeidel():
    M=[]
    for s in range (n):
        M.append([0]*(n))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    b=[]
    for s in range (n):
        b.append(0)
    for i in range(n):
        b[i]=A[i][n]
    sm=1.0
    tol = input('ingrese el TOL que desea usar:')
    print 'los cambios que van haciendo en la solucion del sistema:'
    while sm > tol:
        s1=sm=0
        for i in range(n):
            su=b[i]
            for j in range(0,n):
                su=su-M[i][j]*x[j]
            xi=x[i]+su*(M[i][i]**(-1))
            sm=max(abs(x[i]-xi),sm)
            x[i]=xi
            s1=max(s1,abs(x[i]))
        sm=sm*(s1**(-1))
        print x
    print 'la ultima linea es la solucion del sistema'

ventana = Tk()       
ventana.title('Metodos para la resolucion de sistemas')
boton1 = Button(ventana,text="Eliminacion de Gauss",relief=SOLID,command= gauss)
boton1.grid(row=1,column=1)
boton2 = Button(ventana,text="Metodo de Gauss-Jordan",relief=SOLID,command= gaussjordan)
boton2.grid(row=2,column=1)
boton3 = Button(ventana,text="Metodo de Crout LU1",relief=SOLID,command = croutLU1)
boton3.grid(row=3,column=1)
boton4 = Button(ventana,text="Metodo de Crout L1U",relief=SOLID, command= croutL1U)
boton4.grid(row=4,column=1)
boton5 = Button(ventana,text="Factorizacion LDLt",relief=SOLID,command=LDLT)
boton5.grid(row=5,column=1)
boton6 = Button(ventana,text="Factorizacion de Cholesky",relief=SOLID,command=cholesky)
boton6.grid(row=6,column=1)
boton7 = Button(ventana,text="Metodo de Aasen",relief=SOLID,command=aasen)
boton7.grid(row=7,column=1)
boton8 = Button(ventana,text="Metodo de Parlet-Reid",relief=SOLID,command=ParletReid)
boton8.grid(row=8,column=1)
boton9 = Button(ventana,text="Metodo de Gram-Schmidt",relief=SOLID,command=GS)
boton9.grid(row=9,column=1)
boton10 = Button(ventana,text="Metodo de Householder",relief=SOLID,command=Householder)
boton10.grid(row=10,column=1)
boton11 = Button(ventana,text="Metodo de Givens",relief=SOLID,command=Givens)
boton11.grid(row=11,column=1)
boton12 = Button(ventana,text="Metodo de Jacobi",relief=SOLID,command=jacobi)
boton12.grid(row=12,column=1)
boton13 = Button(ventana,text="Metodo de Gauss-Seidel",relief=SOLID,command=GaussSeidel)
boton13.grid(row=13,column=1)
ventana.mainloop()
sleep(10000)
