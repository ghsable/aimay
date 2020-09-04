# content of tests.py
#def f():
#    return 3

#def test_function():
#    assert f() == 3
import unittest
import main
 
class TestMain(unittest.TestCase):
 
  def test_f(self):
    self.assertEqual(3, main.f())
  
  def test_callback(self):
    self.assertEqual('OK', main.callback())

if __name__ == "__main__":
    unittest.main()
