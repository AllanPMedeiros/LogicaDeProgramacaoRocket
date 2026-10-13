print("Bem vindo ao indicador de dias da semana")

numeroDia = int(input("Digite um numero: "))

match numeroDia:
    case 1:
        print("Hoje é Domingo")
    case 2:
        print("Hoje é Segunda-Feira braba")
    case 3: 
        print("Hoje é Terça-Feira")
    case 4:
        print("Hoje é Quarta Feira")
    case 5:
        print("Hoje é Quinta Feira, quintouuu")
    case 6:
        print("Hoje é Sexta Feira, Sextouuuuuu daleee")
    case 7:
        print("Sabadouuuu hj é sabado")
    case _:
        print("Esse dia da semana não existe")