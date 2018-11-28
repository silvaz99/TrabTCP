from unittest import TestCase


class Test_InicializaEstrutura(TestCase):
    """docstring for Test_InicializaEstrutura."""
    def setUp(self):
        TestCase.setUp(self)
        self.InitEstrutura = InicializaEstruturas('AbcdeF')

    def test_Texto(self):
        texto = self.InitEstrutura.geraTXT('AbcdeF')
        self.assertEqual(self.InitEstrutura.txt, texto)
