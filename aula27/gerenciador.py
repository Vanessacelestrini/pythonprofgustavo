# arquivo: gerenciador.py
import json
from funcionarios import Funcionario

# Função para carregar os funcionários do arquivo JSON
def carregar_funcionarios():
    try:
        with open('funcionarios.json', 'r') as file:
            dados = json.load(file)
            funcionarios = [Funcionario(f['nome'], f['idade'], f['cargo']) for f in dados]
            return funcionarios
    except FileNotFoundError:
        return []  # Se o arquivo não for encontrado, retorna uma lista vazia.

# Função para salvar os funcionários no arquivo JSON
def salvar_funcionarios(funcionarios):
    dados = []
    for f in funcionarios:
        dados.append({
            'nome': f.nome,
            'idade': f.idade,
            'cargo': f.cargo
        })
    with open('funcionarios.json', 'w') as file:
        json.dump(dados, file, indent=4)

# Função para cadastrar um novo funcionário
def cadastrar_funcionario(funcionarios):
    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    cargo = input("Digite o cargo do funcionário: ")
    novo_funcionario = Funcionario(nome, idade, cargo)
    funcionarios.append(novo_funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso!")

# Função para listar todos os funcionários cadastrados
def listar_funcionarios(funcionarios):
    if funcionarios:
        print("\nLista de Funcionários Cadastrados:")
        for funcionario in funcionarios:
            print(funcionario)
    else:
        print("Não há funcionários cadastrados.")

# Função principal que exibe o menu e chama as funções necessárias
def main():
    funcionarios = carregar_funcionarios()  # Carrega os funcionários já cadastrados

    while True:
        print("\nMenu:")
        print("1. Cadastrar um novo funcionário")
        print("2. Listar todos os funcionários")
        print("3. Salvar funcionários em um arquivo JSON")
        print("4. Carregar funcionários do arquivo JSON")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario(funcionarios)
        elif opcao == '2':
            listar_funcionarios(funcionarios)
        elif opcao == '3':
            salvar_funcionarios(funcionarios)
            print("Funcionários salvos com sucesso!")
        elif opcao == '4':
            funcionarios = carregar_funcionarios()
            print("Funcionários carregados com sucesso!")
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
