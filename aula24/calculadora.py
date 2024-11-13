def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"

def restodiv(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Erro: Não é possível calcular o resto da divisão por zero!"

def numeros():
    while True:
        try:
            a = int(input('Qual o primeiro número?\n'))
            b = int(input('Qual o segundo número?\n'))
            return a, b
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def calculadora():
    while True:
        print('Tipos de operação: \n\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 5. Resto de divisão\n')
        operacao = input('Qual operação deseja realizar? 1/2/3/4/5\n')

        if operacao in ['1', '2', '3', '4', '5']:
            a, b = numeros()  # Obtém os números de entrada do usuário
            if operacao == '1':        
                print(f'O resultado da soma de {a} e {b} é {somar(a, b)}')
            elif operacao == '2':        
                print(f'O resultado da subtração de {a} e {b} é {subtrair(a, b)}')
            elif operacao == '3':
                print(f'O resultado da multiplicação de {a} e {b} é {multiplicar(a, b)}')
            elif operacao == '4':    
                print(f'O resultado da divisão de {a} e {b} é {dividir(a, b)}')
            elif operacao == '5':
                print(f'O resultado do resto de divisão de {a} e {b} é {restodiv(a, b)}')
            break  # Sai do loop após uma operação válida
        else:
            print('\n-->Operação inválida, tente novamente<--\n')

# Chama a função para iniciar a calculadora
calculadora()
