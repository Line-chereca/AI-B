# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtração(x, y):
    return x - y

# Função para multiplicação
def multiplicação(x, y):
    return x * y

# Função para divisão
def divisão(x, y):
    return x / y

#Função principal
def calculadora() :
    lista_contas = []
    while True:
        operador = input("Digite a operação: ")
        if operador != "Hist":
         while True:
            try:
                num1 = int(input("Digite o primeiro número: "))
            except ValueError:
                print("Seu burro")
                continue
            else:
                print("Bem da caro")
                break
         while True:
            try:
                num2 = int(input("Digite o segundo número: "))
            except ValueError:
                print("Seu burro")
                continue
            else:
                print("Bem da caro")
                break
