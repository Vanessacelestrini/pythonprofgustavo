import json
from funcionarios import Funcionario

# Lista para armazenar os funcionários
funcionarios = []

# Função para carregar funcionários de um arquivo JSON
def carregar_dados(arquivo="funcionarios.json"):
    try:
        with open(arquivo, "r") as file:
            dados = json.load(file)
            for item in dados:
                funcionario = Funcionario(item["nome"], item["idade"], item["cargo"])
                funcionarios.append(funcionario)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum dado carregado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo. Nenhum dado carregado.")

# Função para salvar funcionários em um arquivo JSON
def salvar_dados(arquivo="funcionarios.json"):
    with open(arquivo, "w") as file:
        dados = [{"nome": f.nome, "idade": f.idade, "cargo": f.cargo} for f in funcionarios]
        json.dump(dados, file, indent=4)
    print("Dados salvos com sucesso!")

# Função para cadastrar um novo funcionário
def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    cargo = input("Digite o cargo do funcionário: ")
    funcionario = Funcionario(nome, idade, cargo)
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso!")

# Função para listar todos os funcionários
def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nLista de Funcionários:")
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. {funcionario}")

# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Cadastro de Funcionários ---")
        print("1. Cadastrar novo funcionário")
        print("2. Listar todos os funcionários")
        print("3. Salvar funcionários em arquivo")
        print("4. Carregar funcionários do arquivo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            salvar_dados()
        elif opcao == "4":
            carregar_dados()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
if __name__ == "__main__":
    carregar_dados()  # Carregar dados ao iniciar o programa
    menu()            # Exibir o menu principal