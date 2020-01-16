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
if __name__ == '__main__':
   unittest.main()

