import math

c = [[(1,0),(0,0)],[(0,0),(0,0)]]
b = [[(0,0),(1,0)],[(1,0),(0,0)]]
a =  [[(1/(2**0.5),0),(1/(2**0.5),0)],[(1/(2**0.5),0),(-(1/(2**0.5)),0)]]
ans = [0,0]
matrizTotal = []
def main():



    m1 = producto_Tensor_Matrices(a,a)
    m2 = producto_Tensor_Matrices(a,b)

    multi1 = multi_matrices(m2,m1)

    multi2 = multi_matrices(multi1,c)

    print(multi2)
    
def sumar(a,b):
    
    ans[0] = a[0] + b[0]
    ans[1] = a[1] + b[1]

    return ans[0], ans[1]
    
def restar(a,b):

    ans[0] = a[0] - b[0]
    ans[1] = a[1] - b[1]

    return ans[0], ans[1]

def multiplicacion(a,b):

    resE = 0
    resI = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if(i == j):
                if j == len(b)-1:
                    resE = resE +  (a[i]*b[j]*-1)
                else:

                    resE = resE + (a[i]*b[j])
            else:
                resI = resI +(a[i]*b[j])                       
    ans[0] = resE
    ans[1] = resI

    return ans[0], ans[1]

def division(a,b):
    
    z1 = (a[0]*b[0]) + (a[1]*b[1])
    z3 = (b[0]**2) + (b[1]**2)
    z2 = (a[1]*b[0]) - (a[0]*b[1])

    ans[0] = z1/z3
    ans[1] = z2/z3

    return ans[0], ans[1]

def modulo(a):
    
    ans[0] = ((a[0]**2)+(a[1]**2))**0.5
    ans[1] = 0

    return ans[0]

def conjugado(a):
    
    ans[0] = a[0]
    ans[1] = a[1]*-1

    return ans[0], ans[1]

def polar_a_Cartesiano(a):

    x = a[0] * math.cos(math.radians(a[1]))
    y = a[0] * math.sin(math.radians(a[1]))

    ans[0] = x
    ans[1] = y

    return ans[0], ans[1]

def cartesiana_a_Polar(a):

    r = ((a[0]**2)+a[1]**2)**(1/2)
    alpha = math.degrees(math.atan(a[1]/a[0]))
    if(a[0] < 0 and a[1] < 0):
        alpha += 180
    elif (a[1] < 0):
        alpha = 360 - alpha
    elif (a[0] < 0 ):
        almtriz_Transpuestapha = 180 - alpha

    ans[0] = r
    ans[1] = alpha

    return ans[0], ans[1]
    
def fase(a):

    ans[0] = math.degrees(math.atan(a[1]/a[0]))

    return ans[0]


def adicion_Vectores(a,b):
    ans2 = []
    if (len(a) == len(b)):
        for i in range(len(a)):
            operar = sumar(a[i],b[i])
            ans2.append(operar)
    else:
        print("no se puede")
    matrizTotal = ans2
    
    return ans2
def inversa_Vectores(a):
    ans2 = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[i])):
            temp.append(a[i][j] * -1)
        ans2.append(temp)
    matrizTotal = ans2

    return ans2        

def multiplicacion_Escalar_Vectores(a,b):
    ans2 = []
    for i in range(len(b)):
        print(b[i])
        ans2.append(multiplicacion(a,b[i]))
    matrizTotal = ans2
    ##print(ans2)
    return ans2

def adicion_Matrices_Complejos(a,b):
    ans2 = []
    if (len(a) == len(b)):
        if(todasIguales(a,b)):
            for i in range(len(a)):
                ans2.append(adicion_Vectores(a[i],b[i]))
            matrizTotal = ans2conjugado
        else:
            print("no se puede")
    else:
        print("no se puede")
    
def inversa_Matrices(a):
    ans2 =[]
    for i in range(len(a)):
        ans2.append(inversa_Vectores(a[i]))
    matrizTotal = ans2
    #print(ans2)
    return ans2

def multiplicacion_Escalar_Matrices(a,b):
    ans2 = []
    for i in range(len(b)):
        ans2.append(multiplicacion_Escalar_Vectores(a,b[i]))
    matrizTotal = ans2

    
    
    return ans2

def mtriz_Transpuesta(a):
    matrizT = []
    for i in range(len(a[0])):
        temp = []
        for j in range(len(a)):
            
            temp.append(a[j][i])
        matrizT.append(temp)
    #print(matrizT)
    
    return matrizT

def matriz_Conjugada(a):
    for i in range(len(a)):
        a[i] = conjugado(a[i])

    #print(a)
    return a

def producto_Tensor_Vectores(a,b):
    temp = []
    for i in range(len(a)):
        for j in range(len(b)):
            temp.append(multiplicacion(a[i],b[j]))
        
    ##print(temp)

    return temp
            
def producto_Tensor_Matrices(a,b):
    temp = []
    for i in range(len(a)):
        for j in range(len(b)):
            temp.append(producto_Tensor_Vectores(a[i],b[j]))
   # print(temp)

    return temp


def multi_matrices(a,b):
    temp = []
    for i in range(len(a)):
        temp2 = []
        for j in range(len(b[0])):
            cont = (0,0)
            for k in range(len(b)):
                oper = multiplicacion(a[i][k],b[k][j])
                cont = sumar(oper,cont) 
    
            temp2.append(cont)
        temp.append(temp2)
        
    

    return temp

def todasIguales(a,b):
    for i in range(len(a)):
            if len(a[i]) != len(b[i]):
                return False
    return True
def prettyPrinting(ans):
    if (ans[0] == 0 and ans[1] == 1): print("i")
    elif ans[0] == 0 :
        print(str(ans[1])+"i")
    elif ans[1] == 0:
        print(ans[0])
    elif ans[1] >= 0 :
        print( str(ans[0])+" + "+str(ans[1])+"i" )
    else:
        print( str(ans[0])+" "+str(ans[1])+"i" )
        
main()

    
