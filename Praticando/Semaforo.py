print("Dia a dia do transito")

corSemaforo = input("Em qual cor o semaforo está?: ")


match corSemaforo:
    case "Verde" | "verde":
        print("Se está verde entao pode seguir em frente!")
    case "Amarelo" | "amarelo":
        print("Se está amarelo então tenha atencão redobrada")
    case "Vermelho" | "vermelho":
        print("Pare imediatamente e espere o sinal ficar verde para prosseguir!")
    case _: 
        print("????? essa cor não existe no semaforo")
    