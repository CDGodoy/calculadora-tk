import unittest
import tkinter as tk
from app.calculadora import Calculadora

class TestCalculadoraEnter(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.calculadora = Calculadora(self.root)
        self.entry = self.calculadora._entrada
        self.result_button = self.calculadora._BTN_RESULT

    def insert_expression(self):
        # Simule a inserção de uma expressão no campo de entrada
        self.root.event_generate(1)
        self.root.event_generate(0)
        self.root.event_generate('+')
        self.root.event_generate(2)
        self.root.event_generate(0)

        # Verifique se o resultado é exibido no campo de entrada
        self.assertEqual(self.entry.get(), "10+20")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
