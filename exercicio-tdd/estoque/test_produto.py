"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.produto = Produto(
            codigo="001",
            nome="Sabonete",
            preco=5.50,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=30),  # válido
            estoque_minimo=10,
            estoque_maximo=100  # Definindo estoque máximo
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.nome, "Sabonete")
        self.assertEqual(self.produto.quantidade, 20)
        self.assertGreater(self.produto.data_validade, datetime.now())

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente e respeitando o estoque máximo."""
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

        # Tentando adicionar mais do que o estoque máximo
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(90)  # Excederá o limite de 100

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        sucesso = self.produto.remover_estoque(5)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 15)

        falha = self.produto.remover_estoque(100)  # não tem estoque suficiente
        self.assertFalse(falha)

        # Testando remoção de quantidade negativa
        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-5)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.assertFalse(self.produto.verificar_estoque_baixo())
        self.produto.remover_estoque(15)
        self.assertTrue(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.assertEqual(self.produto.calcular_valor_total(), 5.50 * 20)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto.verificar_validade())

        produto_vencido = Produto(
            codigo="002",
            nome="Desinfetante",
            preco=8.0,
            quantidade=5,
            data_validade=datetime.now() - timedelta(days=1)  # produto vencido
        )
        self.assertFalse(produto_vencido.verificar_validade())

    def test_valor_negativo(self):
        """Verifica se o preço e a quantidade negativa geram erro."""
        with self.assertRaises(ValueError):
            Produto(codigo="003", nome="Shampoo", preco=-5.0, quantidade=20)

        with self.assertRaises(ValueError):
            Produto(codigo="004", nome="Condicionador", preco=5.0, quantidade=-10)

    def test_adicionar_estoque_negativo(self):
        """Verifica se a tentativa de adicionar quantidade negativa gera erro."""
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)


if __name__ == "__main__":
    unittest.main() 
