import calculadoraComplejos as cal
##import matplotlib.pyplot as plt
def main():
   print()
def canicas(l,v,r):
   for i in range(r):
      v = cal.multi_matrices(l,v)
   return v
def probabilistico_mas_de_dos_rendijas(l,v,r,target):
   if len(l) != target:
      print("Hay un error entre el taget y la matriz")
   else:
      for i in range(r):
         v = cal.multi_matrices(l,v)
   return v
def  cuantico_de_rendijas(l,v,r,target):
   if len(l) != target:
      print("Hay un error entre el taget y la matriz")
   else:
      for i in range(r):
         v = cal.multi_matrices(l,v)
   return v

##def graficar(datos):
##   fig  = plt.figure()
##   ax1 = fig.add_subplot(111)
##   xx = range(1,len(datos)+1)
##
##   ax1.bar(xx,datos, width=0.5, color=(0,1,0), align='center')
##   ax1.set_xticks(xx)
##   ax1.set_ylabel('Porcentaje')
##   plt.show
   
main()
