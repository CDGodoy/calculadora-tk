import unittest
import tkinter as tk
from app.calculadora import Calculadora

class TestCalculadoraEnter(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.calculadora = Calculadora(self.root)
        self.entry = self.calculadora._entrada
        self.result_button = self.calculadora._BTN_RESULT

    def test_insert_number(self):
        # Simule a inserção de uma expressão no campo de entrada
        self.root.event_generate(1)

        # Verifique se o resultado é exibido no campo de entrada
        self.assertEqual(self.entry.get(), "1")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
