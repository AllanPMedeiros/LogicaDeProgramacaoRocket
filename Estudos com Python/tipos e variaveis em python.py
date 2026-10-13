# Tipos de dados: Numericos, Textos, Boleanos (lÓGICOS) e etc..

# Tipos de dados primitivos em python: int, str, float, bool

soma = 15 + 3.14
texto = "Logica de programacao com python"
o_texto_e_verdadeiro = True
print(soma)
print(o_texto_e_verdadeiro)
print(texto)

print(type(15))
print(type(3.14))
print(type(texto))
print(type(o_texto_e_verdadeiro))

#print(soma + texto) # Exemplo do que acontece quando se tenta combinar um tipo de texto com um tipo numeerico em python:
# Traceback (most recent call last):
#   File "c:\Users\allan\onedrive\documentos\L�gicaDePrograma��oRocket\tipos e variaveis em pyton.py", line 15, in <module>
#     print(soma + texto)
#           ~~~~~^~~~~~~
# TypeError: unsupported operand type(s) for +: 'float' and 'str'