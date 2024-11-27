# core/views.py
from django.shortcuts import render

def calculadora(request):
    resultado = None

    if request.method == 'POST':
        numero1 = request.POST.get('numero1')
        numero2 = request.POST.get('numero2')
        operacao = request.POST.get('operacao')

        try:
            numero1 = float(numero1)
            numero2 = float(numero2)

            if operacao == 'soma':
                resultado = numero1 + numero2
            elif operacao == 'subtracao':
                resultado = numero1 - numero2
            elif operacao == 'multiplicacao':
                resultado = numero1 * numero2
            elif operacao == 'divisao':
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    resultado = "Erro: Divisão por zero não é permitida."
        except ValueError:
            resultado = "Erro: Insira valores numéricos válidos."

    return render(request, 'calculadora.html', {'resultado': resultado})
