# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtração(x, y):
    return x - y
#Função principal
def calculadora() :
        operador = input("Digite a operação: ")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        result1 = soma(num1, num2)
        result2 = subtração(num1, num2)

        if operador == "soma":
            print("Resultado da soma:" + str(result1))

        elif operador == "sub":
            print("Resultado da subtração:" + str(result2))

# Executa a calculadora
calculadora()
