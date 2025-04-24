"""
Sistema de gerenciamento de notas escolares.
"""
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Aluno:
    """Representação de um aluno no sistema de notas.
    
    Attributes:
        nome: Nome do aluno
        matricula: Número de matrícula do aluno
        notas: Dicionário com as notas por disciplina
        faltas: Dicionário com o número de faltas por disciplina
    """

    nome: str
    matricula: str
    notas: Dict[str, List[float]] = None  # Disciplina -> Lista de notas
    faltas: Dict[str, int] = None  # Disciplina -> Número de faltas

    def __post_init__(self):
        """Inicializa os dicionários se não forem fornecidos."""
        if self.notas is None:
            self.notas = {}
        if self.faltas is None:
            self.faltas = {}

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)

    def calcular_media(self, disciplina: str) -> float:
        if disciplina not in self.notas or not self.notas[disciplina]:
            return 0.0
        return sum(self.notas[disciplina]) / len(self.notas[disciplina])

    def verificar_aprovacao(self, disciplina: str) -> bool:
        media = self.calcular_media(disciplina)
        return media >= 6.0

    def registrar_falta(self, disciplina: str) -> None:
        if disciplina not in self.faltas:
            self.faltas[disciplina] = 0
        self.faltas[disciplina] += 1

    def calcular_frequencia(self, disciplina: str, total_aulas: int) -> float:
        if total_aulas == 0:
            return 100.0
        faltas = self.faltas.get(disciplina, 0)
        return ((total_aulas - faltas) / total_aulas) * 100