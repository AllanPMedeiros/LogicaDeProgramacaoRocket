print("Bem vindo ao calculo de média escolar")

nota1 = float(input("Digite a nota da primeira prova: "))
peso1 = float(input("Digite o peso da primeira nota: "))

nota2 = float(input("Digite a nota da segunda prova: "))
peso2 = float(input("Digite o peso da segunda nota: "))

resultado1 = nota1 * peso1
resultado2 = nota2 * peso2

valorResultado = resultado1 + resultado2

somaPeso = peso1 + peso2

resultadoFinal = valorResultado / somaPeso

if resultadoFinal >= 9.0:
    print("Parabens, passou com exelencia")
    print("Media Final: ", resultadoFinal)
elif resultadoFinal >= 7.0:  
    print("Passou, mais da pra melhorar heim")
    print("Media Final: ", resultadoFinal)
elif resultadoFinal >= 5.5:
    print("Bateu na trave, vamos de recuperação")
    print("Media Final: ", resultadoFinal)
else:
    print("Não consegiu, REPROVADO")
    print("Media Final: ", resultadoFinal)