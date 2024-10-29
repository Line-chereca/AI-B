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
        operador = input("Digite a operação: ")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        result1 = soma(num1, num2)
        result2 = subtração(num1, num2)
        result3 = multiplicação(num1, num2)
        result4 = divisão(num1, num2)

        if operador == "soma":
            print("Resultado da soma:" + str(result1))

        elif operador == "sub":
            print("Resultado da subtração:" + str(result2))

         elif operador == "multi":
            print("Resultado da multiplicação:" + str(result3))
        
         elif operador == "div":
            print("Resultado da divisão:" + str(result4))
        
        else:
            print("Operação não reconhecida")

# Executa a calculadora
calculadora()
