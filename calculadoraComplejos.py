a = [4,2]
b = [1,0]
ans = [0,0]
def main():
    
    conjugado(a)
    prettyPrinting(ans)


    
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

def conjugado(a):
    
    ans[0] = a[0]
    ans[1] = a[1]*-1
    
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

    
