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
        
        # As diferentes contas e os seus resultados
        result1 = soma(num1, num2)
        result2 = subtração(num1, num2)
        result3 = multiplicação(num1, num2)
        result4 = divisão(num1, num2)

       
        # Se for soma então vai adicionar o num1 ao num2
        if operador == "soma":
            print("Resultado da soma:" + str(result1))
            conta= str(num1) + "+" + str(num2) + "=" + str(result1)
            lista_contas.append(conta)
            print(conta)
            
        # Se for subtração então vai retirar o num2 ao num1
        elif operador == "sub":
            print("Resultado da subtração:" + str(result2))
            conta= str(num1) + "-" + str(num2) + "=" + str(result2)
            lista_contas.append(conta)
            print(conta)

        # Se for multiplicação então vai fazer o num1 vezes o num2
        elif operador == "multi":
            print("Resultado da multiplicação:" + str(result3))
            conta = str(num1) + "x" + str(num2) + "=" + str(result3)
            lista_contas.append(conta)
            print(conta)

        # Se for divisão então vai dividir o num2 pelo num1
        elif operador == "div":
            print("Resultado da divisão:" + str(result4))
            conta = str(num1) + "/" + str(num2) + "=" + str(result4)
            lista_contas.append(conta)
            print(conta)
