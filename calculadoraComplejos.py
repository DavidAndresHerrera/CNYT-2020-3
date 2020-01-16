import math

a = [-1,-3**0.5]
b = [1,0]
ans = [0,0]
def main():

    h = 0
  
def sumar(a,b):
    
    ans[0] = a[0] + b[0]
    ans[1] = a[1] + b[1]
    
def restar(a,b):

    ans[0] = a[0] - b[0]
    ans[1] = a[1] - b[1]

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

def division(a,b):
    
    z1 = (a[1]**2) + (b[1]**2)
    z2 = (a[0]*a[1]) + (b[0]*b[1])
    z3 = (a[1]*b[0]) - (a[0]*b[1])

    ans[0] = z2/z1
    ans[1] = z3/z1

def modulo(a):
    
    ans[0] = ((a[0]**2)+(a[1]**2))**0.5
    ans[1] = 0

def conjugado(a):
    
    ans[0] = a[0]
    ans[1] = a[1]*-1

def polar_a_Cartesiano(a):

    x = a[0] * math.cos(math.radians(a[1]))
    y = a[0] * math.sin(math.radians(a[1]))

    ans[0] = x
    ans[1] = y
def cartesiana_a_Polar(a):

    r = ((a[0]**2)+a[1]**2)**(1/2)
    alpha = math.degrees(math.atan(a[1]/a[0]))
    if(a[0] < 0 and a[1] < 0):
        alpha += 180
    elif (a[1] < 0):
        alpha = 360 - alpha
    elif (a[0] < 0 ):
        alpha = 180 - alpha

    ans[0] = r
    ans[1] = alpha
    
def fase(a):

    ans[0] = math.degrees(math.atan(a[1]/a[0]))

    
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

    
