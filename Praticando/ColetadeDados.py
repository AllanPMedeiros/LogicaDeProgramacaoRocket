import os

print("Formulário de coleta de dados")
print("------------------------------")

print("Responda algumas perguntas a seguir")
input("Aperte Enter para Continuar")
os.system('cls')

nome = input("Qual seu nome?: ")
idade = input("Qual sua idade?: ")
genero = input("Qual seu gênero?: ")
estado = input("Em qual estado você mora?: ")
cidade = input("E em qual cidade?: ")
gostoMusical = input("E o seu gosto musica, qual é?: ")
formacaoAcademica = input("Qual a sua formação academica?: ")
input("Enter para enviar as informações preenchidas")
os.system('cls')

print("Informações coletadas com sucesso!")
input("Enter")
os.system('cls')

print("Gerando visualização....⏳")
input("Enter")
os.system('cls')

print("Visulização Gerada✨")
print("-------------------")

print("Seu Nome: " + nome)
print("Sua Idade: " + idade + " anos ")
print("Seu Gênero: " + genero)
print("Seu Estado: " + estado)
print("Sua Cidade: " + cidade)
print("Seu(s) gosto(s) Musical(is): " + gostoMusical)
print("Sua Formação Acadêmica: " + formacaoAcademica)
input("Aperte Enter para finalizar a visualização dos seus dados")
os.system('cls')

print("Obrigado pelo tempo disponibilizado para o preenchimento, até a proxima!")


# Versão Antiga

# print("Essas são as suas informações: Seu nome é " + nome + " e sua idade é de "+ idade + " anos " 
# ", você é do gênero " + genero + 
# ", você reside no estado de " + estado + " na cidade de " + cidade + 
# ", seu gosto musical é " + gostoMusical +
#  " e você possui ensino susperior em " + formacaoAcademica + ".")
