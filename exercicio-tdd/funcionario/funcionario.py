"""
Sistema de gerenciamento de funcionários.
"""
from dataclasses import dataclass


@dataclass
class Funcionario:
    """Representação de um funcionário com foco em custos trabalhistas e comissões.
    
    Attributes:
        nome: Nome do funcionário
        matricula: Número de matrícula do funcionário
        salario_hora: Valor do salário por hora trabalhada
        horas_trabalhadas: Quantidade de horas trabalhadas no mês
        custo_empregador: Custo fixo mensal do empregador (INSS, FGTS, etc)
        tem_comissao: Indica se o funcionário recebe comissão
        valor_comissao: Valor da comissão por contrato fechado
        contratos_fechados: Número de contratos fechados no mês
    """

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def __post_init__(self):
        if self.salario_hora < 0 or self.horas_trabalhadas < 0 or self.valor_comissao < 0 or self.custo_empregador < 0:
            raise ValueError("Nenhum valor pode ser negativo.")

    def calcular_salario_base(self) -> float:
        """Calcula o salário base até o limite de 220h (sem considerar horas extras)."""
        horas_normais = min(self.horas_trabalhadas, 220)
        return self.salario_hora * horas_normais

    def calcular_horas_extras(self) -> float:
        """Calcula o valor das horas extras, com adicional de 50%."""
        horas_extras = max(self.horas_trabalhadas - 220, 0)
        valor_hora_extra = self.salario_hora * 1.5
        return horas_extras * valor_hora_extra

    def calcular_comissao(self) -> float:
        if self.tem_comissao:
            return self.valor_comissao * self.contratos_fechados
        return 0.0

    def calcular_custo_total(self) -> float:
        salario_base = self.calcular_salario_base()
        horas_extras = self.calcular_horas_extras()
        comissao = self.calcular_comissao()
        return salario_base + horas_extras + comissao + self.custo_empregador