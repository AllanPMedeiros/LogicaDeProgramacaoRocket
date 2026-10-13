print("Seja bem vindo usuário, eu sou o MegaBrain seu assistente virtual pessoal pronto para liberar todo o meu poder para ajudar")

prompt = input("Escolha uma opção: ")


match prompt:
    case 'Organizar meus arquivos e pastas':
        print("Perfeito, vou agora mesmo fazer isso")
    case 'Marcar reuniao com o time de vendas':
        print("Certo, enviando agora e-mails para todos do time de vendas sobre a reuniao")
    case 'Checar minha agenda de Hoje':
        print("Ok, hoje o senhor tem reunião com o financeiro e encontro com o dono da MegaTech")
    case _:
        print("Não Entendi senhor, me diga novamente o que quer que eu faça")