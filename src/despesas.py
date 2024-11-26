import numpy as np

class despesa:
    valor = 0.0
    nome = ""
    data = ""
    descricao = ""

    def __init__(self, nome : str, valor : float, data : str, descricao : str):
        self.valor = valor
        self.nome = nome
        self.data = data
        self.descricao = descricao
