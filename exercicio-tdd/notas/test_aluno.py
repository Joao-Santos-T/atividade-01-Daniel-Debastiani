"""
Testes da classe Aluno.
"""
import unittest

from aluno import Aluno


class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno(nome="Carlos", matricula="202501")

    def test_adicionar_nota(self):
        self.aluno.adicionar_nota("Matemática", 8.0)
        self.aluno.adicionar_nota("Matemática", 6.0)
        self.assertEqual(self.aluno.notas["Matemática"], [8.0, 6.0])

    def test_calcular_media(self):
        self.aluno.adicionar_nota("História", 7.0)
        self.aluno.adicionar_nota("História", 5.0)
        self.assertAlmostEqual(self.aluno.calcular_media("História"), 6.0)

    def test_verificar_aprovacao(self):
        self.aluno.adicionar_nota("Geografia", 7.0)
        self.aluno.adicionar_nota("Geografia", 6.0)
        self.assertTrue(self.aluno.verificar_aprovacao("Geografia"))

        self.aluno.adicionar_nota("Física", 5.0)
        self.aluno.adicionar_nota("Física", 4.0)
        self.assertFalse(self.aluno.verificar_aprovacao("Física"))

    def test_registrar_falta(self):
        self.aluno.registrar_falta("Biologia")
        self.aluno.registrar_falta("Biologia")
        self.assertEqual(self.aluno.faltas["Biologia"], 2)

    def test_calcular_frequencia(self):
        self.aluno.registrar_falta("Química")
        self.aluno.registrar_falta("Química")
        self.assertAlmostEqual(self.aluno.calcular_frequencia("Química", 10), 80.0)

        self.assertAlmostEqual(self.aluno.calcular_frequencia("Inglês", 10), 100.0)  # disciplina sem falta
        self.assertEqual(self.aluno.calcular_frequencia("Qualquer", 0), 100.0)  # total_aulas zero


if __name__ == "__main__":
    unittest.main() 