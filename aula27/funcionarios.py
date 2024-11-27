# arquivo: funcionarios.py

class Funcionario:
    def __init__(self, nome, idade, cargo):
        """
        Inicializa o funcionário com o nome, idade e cargo.
        """
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def __str__(self):
        """
        Retorna as informações do funcionário em formato de string.
        """
        return f"Nome: {self.nome} | Idade: {self.idade} | Cargo: {self.cargo}"
