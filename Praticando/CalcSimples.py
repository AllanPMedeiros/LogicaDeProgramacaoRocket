print("Bem vindo a calculadora mágica!!")

num1 = float(input("Digite o primeriro numero: "))
num2 = float(input("Digite o segundo numero: "))

operacao = input("Escolha um operador para realizar sua conta como +,-,*,/ ou % para resto de divisão: ")

resultadoFinal = num1 + num2

match operacao:
    case "+":
        resultadoFinal = num1 + num2
        print("Você escolheu SOMA e seu resultado é: ",resultadoFinal)
    case "-":
        resultadoFinal = num1 - num2
        print("Você escolheu MENOS e seu resultado é: ",resultadoFinal)
    case "*":
        resultadoFinal = num1 * num2
        print("Você escolheu MULTIPLICAÇÃO e seu resultado é: ",resultadoFinal)
    case "/":
        resultadoFinal = num1 / num2
        print("Você escolheu DIVISÃO e seu resultado é: ",resultadoFinal)
    case "%":
        resultadoFinal = num1 % num2
        print("O resto da DIVISÃO é :",resultadoFinal)
    case _:
        print("Essa Operação ainda não existe!!")
    
        
