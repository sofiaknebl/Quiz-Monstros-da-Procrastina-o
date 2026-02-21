import random
import datetime
import os

# Lista global para armazenar perguntas já respondidas
perguntas_respondidas = []

# ============================ UTILITÁRIOS ============================
def carregar_quiz(caminho="quiz.txt"):
    try:
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print("Arquivo quiz.txt não encontrado.")
        return {}

    perguntas_por_tema = {}

    for linha in conteudo.strip().split("\n"):
        partes = linha.strip().split("|")
        if len(partes) == 7:
            pergunta, tema, correta, alt_a, alt_b, alt_c, alt_d = [p.strip() for p in partes]

            letra_correta = correta.upper()

            if letra_correta not in ["A", "B", "C", "D"]:
                print(f"Resposta inválida na pergunta: {pergunta}")
                continue

            if tema not in perguntas_por_tema:
                perguntas_por_tema[tema] = []

            perguntas_por_tema[tema].append({
                "pergunta": pergunta,
                "correta": letra_correta,
                "alternativas": {
                    "A": alt_a,
                    "B": alt_b,
                    "C": alt_c,
                    "D": alt_d
                }
            })

    return perguntas_por_tema

def detectar_modo_lis(caminho="quiz.txt"):
    try:
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read().lower()
            palavras_chave = ["Isabela Cascais", "Laura Felício", "Sofia Knebl"]
            return any(palavra.lower() in conteudo for palavra in palavras_chave)
    except FileNotFoundError:
        print("Arquivo quiz.txt não encontrado.")
        return False

# ============================ MODO LIS (RPG) ============================
def modo_lis():
    print("\nEscolha seus pronomes:")
    print("1. Ela/dela")
    print("2. Ele/dele")
    print("3. Elu/delu")
    opcao_pronome = input("\nDigite o número da sua escolha: ").strip()
    pronome = {"1": "a", "2": "o", "3": "e"}.get(opcao_pronome, "e")

    nome = input(f"\nDigite seu nome, aventureir{pronome}: ").strip().title()
    data_jogo = datetime.datetime.now().strftime("%d/%m/%Y")

    print(f"\nBem-vind{pronome} ao Quiz: Monstros da Procrastinação, {nome}!")
    print(f"Data do jogo: {data_jogo}\n")

    print("-" * 180)
    print("\nElaborado por: Isabela Cascais, Laura Felício e Sofia Knebl — SEGMA1  — 2025/01\n")
    print("-" * 180)

    print("\nVocê caiu no Reino de Procrastinária...")
    print("Um mundo paralelo criado pelos seus próprios hábitos procrastinadores...")
    print("Para conquistar seu tão sonhado diploma de Segurança da Informação e escapar de Procrastinária, você precisa atravessar as ruínas do reino")
    print("Porém, esse caminho não será nada fácil...\nA cidade é protegida por cinco temidos Monstros — criaturas digitais — que testarão sua coragem, conhecimento e raciocínio.")
    print("Apenas ao derrotar cada um deles, você poderá alcançar o lendário Templo da Certificação e provar que está pronto para o mundo da Segurança Cibernética.\n")

    temas = {
        1: ("Comunicação e Expressão", "Sonequita", "uma fada sonolenta que lança bocejos mágicos"),
        2: ("Arquitetura e Organização de Computadores", "Scrollador Sombrio", "um feiticeiro que conjura feitiços de feed infinito"),
        3: ("Programação", "TikTokssauro", "um dinossauro ancestral que encanta com danças hipnóticas de 30 segundos"),
        4: ("Matemática Discreta", "Multitarefas", "um monstro com cem olhos e mil abas abertas"),
        5: ("Princípios de Segurança da Informação", "Doomscroll", "uma sombra digital que te prende nas notificações do caos")
    }

    perguntas_por_tema = carregar_quiz()
    monstros_derrotados = []

    while True:
        total_perguntas = 0
        total_acertos = 0
        resumo_total = []
        monstros_derrotados.clear()

        while True:
            print("\n=== Escolha sua próxima ruína para explorar ===")
            for i, (tema, monstro, _) in temas.items():
                print(f"{i}. {tema}")

            while True:
                try:
                    escolha = int(input("\nEscolha um tema para enfrentar o próximo monstro: "))
                    if escolha in temas:
                        tema_escolhido, nome_monstro, descricao_monstro = temas[escolha]
                        break
                    else:
                        print("Escolha inválida. Tente novamente.")
                except ValueError:
                    print("Digite apenas números.")

            perguntas = perguntas_por_tema.get(tema_escolhido, [])
            if not perguntas:
                print("Nenhuma pergunta disponível para esse tema.")
                continue

            perguntas_disponiveis = [p for p in perguntas if p not in perguntas_respondidas]
            total_disponivel = len(perguntas_disponiveis)
            if total_disponivel == 0:
                print("Todas as perguntas deste tema já foram respondidas. Escolha outro tema.")
                continue

            qtd = input(f"\nQuantas questões você quer responder ({total_disponivel} disponíveis, mínimo 5)? ").strip()
            while not qtd.isdigit() or int(qtd) < 5 or int(qtd) > total_disponivel:
                qtd = input(f"Digite um número válido de questões (mínimo 5, máximo {total_disponivel}): ").strip()
            qtd = int(qtd)

            selecionadas = random.sample(perguntas_disponiveis, qtd)
            perguntas_respondidas.extend(selecionadas)
            vidas_jogador = qtd
            vidas_monstro = qtd

            print(f"\nVocê se aproxima das ruínas de {tema_escolhido}...")
            print(f"✨ Surge das sombras: {nome_monstro}, {descricao_monstro}!")
            print(f"🏰 Vidas — {nome}: {vidas_jogador} | {nome_monstro}: {vidas_monstro}\n")

            for i, pergunta in enumerate(selecionadas, start=1):
                print(f"⚔️ Pergunta {i}: {pergunta['pergunta']}")
                for letra, alt in pergunta['alternativas'].items():
                    print(f"{letra}) {alt}")
                resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
                while resposta not in ["A", "B", "C", "D"]:
                    resposta = input("Resposta inválida. Use A, B, C ou D: ").strip().upper()

                correta = pergunta['correta']
                acertou = resposta == correta

                if acertou:
                    vidas_monstro -= 1
                    total_acertos += 1
                    print(f"💥 Acertou! {nome_monstro} perdeu 1 ponto de vida!")
                else:
                    vidas_jogador -= 1
                    print(f"😖 Errou! {nome_monstro} atingiu você com seu poder!")

                print(f"❤️ Vidas restantes — {nome}: {vidas_jogador} | {nome_monstro}: {vidas_monstro}\n")
                resumo_total.append({
                    "pergunta": pergunta["pergunta"],
                    "resposta_jogador": resposta,
                    "correta": correta,
                    "alternativas": pergunta["alternativas"]
                })

            total_perguntas += qtd

            if vidas_jogador > vidas_monstro:
                print(f"🏆 {nome_monstro} foi derrotado! Sua presença desvanece nas ruínas...\n")
                monstros_derrotados.append(nome_monstro)
            elif vidas_monstro > vidas_jogador:
                print(f"💀 {nome_monstro} te venceu nesta batalha...\n")
            else:
                print(f"⚖️ Empate! {nome_monstro} desaparece entre as sombras...\n")

            continuar = input("Deseja continuar sua jornada e explorar outra ruína? (s/n): ").strip().lower()
            if continuar in ['s', 'sim']:
                continue
            else:
                break

        print("\n=== RESUMO DA AVENTURA ===")
        for i, r in enumerate(resumo_total, start=1):
            print(f"\n{i}) {r['pergunta']}")
            print(f"   Sua resposta: {r['resposta_jogador']}) {r['alternativas'].get(r['resposta_jogador'], 'Opção inválida')}")
            print(f"   Resposta certa: {r['correta']}) {r['alternativas'].get(r['correta'], 'Opção inválida')}\n")

        print(f"Total de acertos: {total_acertos} de {total_perguntas}")
        percentual = (total_acertos / total_perguntas) * 100 if total_perguntas > 0 else 0

        if percentual > 50:
            print(f"\n🌟 Excelente esforço, {nome}! Com {int(percentual)}% de acertos, mostraste grande determinação contra as forças da procrastinação!")
        else:
            print(f"\n💀 Oh não, {nome}... Com {int(percentual)}% de acertos, tua jornada foi interrompida pelas forças procrastinadoras...")

        if percentual >= 80 and len(monstros_derrotados) >= 3:
            print(f"\n🎓 Bravo, {nome}! Após vencer {len(monstros_derrotados)} monstros e acertar {int(percentual)}% das questões, conquistaste o Certificado da Coragem Digital!")
            
        elif percentual >= 80 and len(monstros_derrotados) == 1:
            print(f"\n🎖️ Ótimo desempenho, {nome}! Com {int(percentual)}% de acertos, venceste um monstro, mas precisas derrotar mais dois para alcançar o certificado!")

        repetir = input("\nDeseja iniciar uma nova aventura? (s/n): ").strip().lower()
        if repetir in ['s', 'sim']:
            continue
        else:
            print(f"\nAté a próxima jornada, valoros{pronome} {nome}! Que os ventos da sabedoria guiem teus passos.")
            break

# ============================ MODO PADRÃO ============================
def modo_padrao():
    data_jogo = datetime.datetime.now().strftime("%d/%m/%Y")
    nome = input("\nDigite seu nome: ").strip().title()

    print("\nEscolha seus pronomes:")
    print("1. Ela/dela")
    print("2. Ele/dele")
    print("3. Elu/delu")
    opcao_pronome = input("\nDigite o número da sua escolha: ").strip()
    pronome = {"1": "a", "2": "o", "3": "e"}.get(opcao_pronome, "e")

    print(f"\nBem-vind{pronome} ao Quiz, {nome}!")
    print(f"Data do jogo: {data_jogo}\n")

    perguntas_por_tema = carregar_quiz()
    if not perguntas_por_tema:
        return

    print("\nTemas disponíveis:\n")
    for i, tema in enumerate(perguntas_por_tema.keys(), start=1):
        print(f"{i} - {tema}")

    tema_escolhido = input("\nEscolha o tema digitando o nome exatamente como aparece: ").strip()
    while tema_escolhido not in perguntas_por_tema:
        tema_escolhido = input("Tema inválido. Digite novamente: ").strip()

    perguntas_disponiveis = perguntas_por_tema[tema_escolhido]
    total_disponivel = len(perguntas_disponiveis)

    qtd = input(f"Quantas questões você quer responder ({total_disponivel} disponíveis)? ").strip()
    while not qtd.isdigit() or int(qtd) < 5 or int(qtd) > total_disponivel:
        qtd = input(f"Digite um número válido de questões (mínimo 5, máximo {total_disponivel}): ").strip()
    qtd = int(qtd)

    sorteadas = random.sample(perguntas_disponiveis, qtd)
    respondidas = []
    acertos = 0
    erros = 0

    for i, pergunta in enumerate(sorteadas, start=1):
        print(f"\nPergunta {i}: {pergunta['pergunta']}")
        for letra, texto in pergunta['alternativas'].items():
            print(f"{letra}) {texto}")

        resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
        while resposta not in ["A", "B", "C", "D"]:
            resposta = input("Resposta inválida. Use A, B, C ou D: ").strip().upper()

        correta = pergunta["correta"]
        acertou = (resposta == correta)

        if acertou:
            print("✅ Correto!\n")
            acertos += 1
        else:
            print(f"❌ Errado. A resposta certa era {correta}) {pergunta['alternativas'][correta]}\n")
            erros += 1

        respondidas.append({
            "pergunta": pergunta["pergunta"],
            "resposta_jogador": resposta,
            "correta": correta,
            "alternativas": pergunta["alternativas"]
        })

    print("\n===== RESUMO DO JOGO =====")
    for i, r in enumerate(respondidas, start=1):
        print(f"\n{i}) {r['pergunta']}")
        print(f"   Sua resposta: {r['resposta_jogador']}) {r['alternativas'][r['resposta_jogador']]}")
        print(f"   Resposta certa: {r['correta']}) {r['alternativas'][r['correta']]}")
    print(f"\nTotal de acertos: {acertos}")
    print(f"Total de erros: {erros}")

# ============================ EXECUÇÃO ============================
if __name__ == "__main__":
    if detectar_modo_lis():
        print("Liberando os Monstrinhos...")
        modo_lis()
    else:
        modo_padrao()
