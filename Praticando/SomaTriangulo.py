print("Descubra se o triangulo é valido ou não!")

ladoA = float(input("Digite o valor do lado A em CM: "))

ladoB = float(input("Digite o valor do lado B em CM: "))

ladoC = float (input("Digite o valor do lado C em CM: "))

perimetro = ladoA + ladoB + ladoC

if ladoA and ladoB > ladoC:
    print("Seu triangulo é valido,e é isoceles")
elif ladoA and ladoB == ladoC:
    print("Seu triangulo é valido e é equilátero")
elif ladoA != ladoB != ladoC:
    print("Seu triangulo é valido e é escaleno")
else:
    print("Seu triangulo não é valido!")