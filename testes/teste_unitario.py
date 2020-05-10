import unittest
from funcoes import soma
from funcoes import media
from funcoes import mediana


class FuncoesTesteUnitario(unittest.TestCase):
    def setUp(self):
        print(f"SETUP[{self._testMethodName}] -> configurando...")

    def tearDown(self):
        print(f"TEAR_DOWN[{self._testMethodName}] -> finalizando...")

    def teste_soma(self):
        """Testando soma([1, 2, 3])"""
        self.assertEqual(soma([1, 2, 3]), 6)

    def teste_soma_tipo_invalido(self):
        """Testando soma(True) esperando TypeError"""
        try:
            soma(True)
        except TypeError:
            pass
        except Exception:
            self.fail("uma exceção diferente da esperada foi lançada")
        else:
            self.fail("nenhuma exceção foi lançada")

    def teste_soma_lista_invalido(self):
        """Testando soma([]) esperando ValueError"""
        try:
            soma([])
        except ValueError:
            pass
        except Exception:
            self.fail("uma exceção diferente da esperada foi lançada")
        else:
            self.fail("nenhuma exceção foi lançada")


if __name__ == "__main__":
    unittest.main()
