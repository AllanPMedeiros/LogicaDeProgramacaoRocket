print("Notas em conceito usando guarda de if")

nota = float(input("Digite sua nota: "))

match nota:
    case nota if nota >= 9.0:
        print("Excelente!! mais aura mais estudo")
    case nota if nota >= 7.0: 
        print("Mandou bem, mais da para melhorar")
    case nota if nota >=5.0:
        print("Recuperação")
    case nota if nota <= 4.9:
        print("Perdeu tudoo, recomece no proximo ano")
    case _:
        print("???????")
    