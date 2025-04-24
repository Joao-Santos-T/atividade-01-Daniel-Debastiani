import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_base_sem_horas_extras(self):
        funcionario = Funcionario(
            nome="João", 
            matricula=1, 
            salario_hora=50, 
            horas_trabalhadas=200
        )
        self.assertEqual(funcionario.calcular_salario_base(), 50 * 200)

    def test_calcular_salario_base_com_limite(self):
        funcionario = Funcionario(
            nome="Ana", 
            matricula=2, 
            salario_hora=60, 
            horas_trabalhadas=250
        )
        self.assertEqual(funcionario.calcular_salario_base(), 60 * 220)  # Limite de 220h

    def test_calcular_horas_extras(self):
        funcionario = Funcionario(
            nome="Carlos", 
            matricula=3, 
            salario_hora=40, 
            horas_trabalhadas=230
        )
        horas_extras = 10
        valor_hora_extra = 40 * 1.5
        self.assertEqual(funcionario.calcular_horas_extras(), horas_extras * valor_hora_extra)

    def test_calcular_horas_extras_sem_excedente(self):
        funcionario = Funcionario(
            nome="Lucas", 
            matricula=4, 
            salario_hora=70, 
            horas_trabalhadas=200
        )
        self.assertEqual(funcionario.calcular_horas_extras(), 0.0)

    def test_calcular_comissao_ativa(self):
        funcionario = Funcionario(
            nome="Paula",
            matricula=5, 
            tem_comissao=True, 
            valor_comissao=100, 
            contratos_fechados=4
        )
        self.assertEqual(funcionario.calcular_comissao(), 400.0)

    def test_calcular_comissao_inativa(self):
        funcionario = Funcionario(
            nome="Pedro", 
            matricula=6, 
            tem_comissao=False, 
            valor_comissao=200, 
            contratos_fechados=3
        )
        self.assertEqual(funcionario.calcular_comissao(), 0.0)

    def test_calcular_custo_total(self):
        funcionario = Funcionario(
            nome="Roberta",
            matricula=7,
            salario_hora=50,
            horas_trabalhadas=230,
            custo_empregador=1000,
            tem_comissao=True,
            valor_comissao=150,
            contratos_fechados=2
        )
        salario_base = 50 * 220
        horas_extras = 10 * (50 * 1.5)
        comissao = 2 * 150
        total = salario_base + horas_extras + comissao + 1000
        self.assertEqual(funcionario.calcular_custo_total(), total)

    def test_valores_negativos_disparam_erro(self):
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=9, salario_hora=-100)

        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=9, horas_trabalhadas=-10)

        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=9, valor_comissao=-50)

        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=9, custo_empregador=-500)

if __name__ == "__main__":
    unittest.main()
