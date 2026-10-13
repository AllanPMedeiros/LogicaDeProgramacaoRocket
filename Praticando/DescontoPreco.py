print("Bem vindo a nossa lojinha!")

print("Para compras acima de R$500 temos 15% de desconto, para compras de 200 a 500 reais temos 10% de desconto e para compras abaixo de 200 reais não temos desconto")

valorCompra = float(input("Digite o valor da compra para vermos se tem desconto: "))

if valorCompra > 500:
    desconto = 0.15
    print("Desconto maximo")
elif valorCompra >= 200: 
    desconto = 0.10
    print("Desconto medio")
else:
    desconto = 0
    print("NÃO TEM DESCONTOOO")

precoFinal = valorCompra - (valorCompra * desconto)



print("O preço final do produto com desconto é de: ", precoFinal,"R$")