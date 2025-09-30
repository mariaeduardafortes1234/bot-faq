# Mini Bot de Perguntas sobre Tênis

print("🤖: Olá! Eu sou o TeBot, seu assistente de Tênis.")
print("Digite 'sair' para encerrar a conversa.\n")

while True:
    pergunta = input("Você: ").strip().lower()

    if pergunta == "sair":
        print("TeBot: Até mais!👋")
        break

    # Respostas pré-definidas
    elif "jogar" in pergunta or "joga" in pergunta:
        print("🤖: Dois jogadores lançam uma bola, usando uma raquete, acima da rede que separa uma quadra")

    elif "objetivo" in pergunta:
        print("🤖: O jogador deve rebater a bola com a raquete para o lado do adversário para atingir mais pontos. O esporte exige raciocínio rápido e estrátegia dos competidores")

    elif "origem" in pergunta or "surgiu" in pergunta:
        print("🤖: Laços repetem código várias vezes. Exemplo:\nfor i in range(5):\n    print(i)")

    elif "while" in pergunta:
        print("🤖: O laço while repete enquanto a condição for verdadeira. Exemplo:\nwhile x < 5:\n    x += 1")

    elif "randint" in pergunta or "aleatório" in pergunta:
        print("🤖: Você pode gerar números aleatórios com a biblioteca random.\nExemplo:\nfrom random import randint\nnumero = randint(1, 10)")

    else:
        print("🤖: Hmmm... não entendi. Pergunte sobre variáveis, condicionais, laços ou randint.")
