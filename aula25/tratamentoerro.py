def cadastrar_usuario():
    while True:
        try:
            nome = input('Digite seu nome:\n')
            if not nome.isalpha(): # adicionar validação de nome e sobrenome
                raise ValueError('O nome deve conter apenas letras')
        
            idade = int(input('Digite sua idade:\n'))
            if idade < 0 or idade > 120:
                raise ValueError('Digite uma idade entre 0 e 120')
            
            email = input('Digite o seu email:\n')
            if '@' not in email or '.' not in email.split('@')[-1]:
            #if '.' not in email.split('@')[-1] or '@' not in email or '.':  ->ERRADO<-
                raise ValueError('Email inválido. Certifique-se de que está no formato correto.')
            
            senha = input('Digite sua senha:\n')
            if not any(char.isupper() for char in senha) or not any(char.islower() for char in senha):
                raise ValueError('A senha deve conter no mínimo uma letra maiúscula e uma minúscula.')
            
            confirmacaosenha = input('Confirme sua senha:\n')
            if not confirmacaosenha == senha:
                raise ValueError('A senha deve ser igual a anterior.')
            
            senhacript = '*' * len(senha) 
            
            print("\nCadastro realizado com sucesso!")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Email: {email}")
            print(f"Senha: {senhacript}")
            break

        except ValueError as e:
            print(f"Erro: {e}")
            print("Tente novamente.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            print("Tente novamente.\n")

        finally:
            print('Obrigado por usar nosso sistema')

cadastrar_usuario()


        

