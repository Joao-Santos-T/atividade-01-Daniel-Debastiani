"""
Sistema de controle de estoque.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Produto:
    """Representação básica de um produto no estoque."""

    codigo: str
    nome: str
    preco: float
    quantidade: int = 0
    data_validade: Optional[datetime] = None
    estoque_minimo: int = 10
    estoque_maximo: int = 100  # Novo campo

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if self.quantidade < 0:
            raise ValueError("A quantidade inicial não pode ser negativa.")

    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona quantidade ao estoque do produto."""
        if quantidade <= 0:
            raise ValueError("A quantidade a ser adicionada deve ser positiva.")
        if self.quantidade + quantidade > self.estoque_maximo:
            raise ValueError("Não é possível adicionar: excede o estoque máximo.")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int) -> bool:
        """Remove quantidade do estoque do produto."""
        if quantidade <= 0:
            raise ValueError("A quantidade a ser removida deve ser positiva.")
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return True
        return False

    def verificar_estoque_baixo(self) -> bool:
        """Verifica se o estoque está abaixo do mínimo."""
        return self.quantidade < self.estoque_minimo

    def calcular_valor_total(self) -> float:
        """Calcula o valor total do produto em estoque."""
        return self.preco * self.quantidade

    def verificar_validade(self) -> bool:
        """Verifica se o produto está dentro da validade."""
        if self.data_validade is None:
            return True
        return datetime.now() <= self.data_validade