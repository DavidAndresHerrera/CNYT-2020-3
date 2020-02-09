import unittest
import calculadoraComplejos

class TestStringMethods(unittest.TestCase):
   
   def test_SumarComplejos(self):
      calculadoraComplejos.sumar([4,5],[4,6])
      self.assertEqual(calculadoraComplejos.ans,[8,11])
      
   def test_RestarComplejos(self):
      calculadoraComplejos.restar([3,-2],[4,6])
      
      self.assertEqual(calculadoraComplejos.ans,[-1,-8])
      
   def test_MultiplicarComplejos(self):
      calculadoraComplejos.multiplicacion([2,3],[4,5])
      self.assertEqual(calculadoraComplejos.ans,[-7,22])

   def test_DivisionComplejos(self):
      calculadoraComplejos.division([1,1],[-1,1])
      self.assertEqual(calculadoraComplejos.ans,[0,-1])
      
   def test_ModuloComplejos(self):
      calculadoraComplejos.modulo([3,5])
      self.assertEqual(calculadoraComplejos.ans,[34**0.5,0])

   def test_ConjugadoComplejos(self):
      calculadoraComplejos.conjugado([4,2])
      self.assertEqual(calculadoraComplejos.ans,[4,-2])

   def test_polar_a_cartesiano(self):
      self.assertEqual(calculadoraComplejos.polar_a_Cartesiano([2,120]),(-0.9999999999999996,1.7320508075688774))
      
   def test_cartesiana_a_Polar(self):
      self.assertEqual(calculadoraComplejos.cartesiana_a_Polar([1,(3**0.5)]),(2.0,59.99999999999999))

   def test_fase(david):
      david.assertEqual(calculadoraComplejos.fase([4,-3]),(-36.86989764584402))

   def test_adicion_Vectores(juan):
      juan.assertEqual(calculadoraComplejos.adicion_Vectores([(1,0),(2,0)],[(4,4),(6,6)]),([(5, 4), (8, 6)]))

   def test_inversa_Vectores(david):
      david.assertEqual(calculadoraComplejos.inversa_Vectores([(1,6),(-10,-6)]),([[-1,-6],[10,6]]))

   def test_multiplicacion_Escalar_Vectores(david):
      david.assertEqual(calculadoraComplejos.multiplicacion_Escalar_Vectores([2,1],[(1,1),(2,2)]),([(1,3),(2,6)]))

   def test_adicion_Matrices_Complejos(david):
      david.assertEqual(calculadoraComplejos.adicion_Matrices_Complejos([[(1,12)],[(-2,4)],[(-3,0)]],[[[3,0]], [[4,0]],[[54,6]]]),([[(4, 12)], [(2, 4)], [(51, 6)]]))

   def test_inversa_Matrices(david):
      david.assertEqual(calculadoraComplejos.inversa_Matrices([[(-1,-2),(2,-6),(-12,2)],[(0,-12),(3,-7),(67,12)]]),([[[1, 2], [-2, 6], [12, -2]], [[0, 12], [-3, 7], [-67, -12]]]))

   def test_multiplicacion_Escalar_Matrices(david):
      david.assertEqual(calculadoraComplejos.multiplicacion_Escalar_Matrices([2,1],[[(-1,-2),(2,-6),(-12,2)],[(0,-12),(3,-7),(67,12)]]),([[(0, -5), (10, -10), (-26, -8)], [(12, -24), (13, -11), (122, 91)]]))

   def test_vector_traspuesto(david):
      david.assertEqual(calculadoraComplejos.vector_traspuesto([(-1,-2),(2,-6),(-12,2)]),([[(-1,-2)],[(2,-6)],[(-12,2)]]))

   def test_matriz_Transpuesta(david):
      david.assertEqual(calculadoraComplejos.matriz_Transpuesta([[(-1,-2),(2,-6),(-12,2)],[(0,-12),(3,-7),(67,12)]]),([[(-1, -2), (0, -12)], [(2, -6), (3, -7)], [(-12, 2), (67, 12)]]))

   def test_vector_Conjugado(david):
      david.assertEqual(calculadoraComplejos.vector_Conjugado([(-1,-2),(2,-6),(-12,2)]),([(-1,2),(2,6),(-12,-2)]))

   def test_matriz_Conjugada(david):
      david.assertEqual(calculadoraComplejos.matriz_Conjugada([[(-1,-2),(2,-6),(-12,2)],[(0,-12),(3,-7),(67,12)]]),([[(-1,2),(2,6),(-12,-2)],[(0,12),(3,7),(67,-12)]]))

   def test_producto_Tensor_Vectores(david):
      david.assertEqual(calculadoraComplejos.producto_Tensor_Vectores([(1,6),(-10,-6)],[(-1,-2),(2,-6)]),([(11, -8), (38, 6), (-2, 26), (-56, 48)]))

   def test_producto_Tensor_Matrices(david):
      david.assertEqual(calculadoraComplejos.producto_Tensor_Matrices([[(1,0),(-10,0)],[(-1,0),(2,0)]],[[(0,0)],[(3,-7)]]),([[(0, 0), (0, 0)], [(3, -7), (-30, 70)], [(0, 0), (0, 0)], [(-3, 7), (6, -14)]]))

   def test_multi_matrices(david) :
      david.assertEqual(calculadoraComplejos.multi_matrices([[(1,1)],[(-3,0)]],[[(3,0),(4,0),(4,6)]]),(False))

   def test_trasa(david):
      david.assertEqual(calculadoraComplejos.trasa([[(-1,-2),(2,-6),(-12,2)],[(0,-12),(3,-7),(67,12)]]),(2, -9))

   def test_producto_interno(david):
      david.assertEqual(calculadoraComplejos.producto_interno([[(1,0),(-1,0)],[(2,0),(3,0)]],[[(1,0),(4,0)],[(0,0),(2,0)]]),(3,0))

   def test_distancia_Vectores(david):
      david.assertEqual(calculadoraComplejos.distancia_Vectores( [[1,0], [-2,0]],[[3,0], [4,0]]),(40**0.5))

   def test_hermitian_Matrix(david):
      david.assertEqual(calculadoraComplejos.hermitian_Matrix([[(3,0),(3,1)],[(3,-1),(2,0)]]),(True))

if __name__ == '__main__':
   unittest.main()

