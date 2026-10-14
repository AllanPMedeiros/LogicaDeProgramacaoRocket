print("DIAS DA SEMANA COM MATCH CASE AGRUPADO")

dia = input("Que dia é hoje?: ")

match dia:
    case "Segunda-Feira" | "Terça-Feira":
        print("Hoje é dia util, bora trabalhar e estudar")
    case "Quarta-Feira" | "Quinta-Feira":
        print("Hoje é dia util, bora trabalhar e estudar")
    case "Sexta-Feira":
        print("Sextouu, mais ainda é dia util, bora trabalhar")
    case "Sabado" | "Domingo":
        print("É fim de semana, bora descansar")
    case _: 
        print("Não existe esse dia da semana!")