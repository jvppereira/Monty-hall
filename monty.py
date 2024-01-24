import random

def monty_hall_simulacao(num_simulacoes):
    # Inicializa contadores
    vitorias_sem_mudar = 0
    vitorias_com_mudar = 0
    mudou = 0
    nmudou = 0

    for i in range(0,num_simulacoes):
        print(f"----------     Jogada numero: {i}   ----------")
        # Coloca o prêmio aleatoriamente atrás de uma das três portas
        porta_com_premio = random.randint(1, 3)

        # Jogador faz uma escolha inicial aleatória
        escolha_jogador = random.randint(1, 3)


        # --------- O apresentador abre uma das portas sem o prêmio ---------

        # aqui ele vai abrir uma porta que esta sem o premio obviamente. Portanto ele tira a porta com premio da lista antes de fazer isso. Agora ele vai ver se a escolha do jogador é uma das outras duas que sobraram na lista, se for ele tira tbm pois nao pode abrir a que o jogador escolheu obviamente, ai so sobre uma. agora se ele escolheu a que tem o premio a escolha das portas e aleatoria, pois ainda vao ter 2 .

        portas_disponiveis = [1, 2, 3]
        portas_disponiveis.remove(porta_com_premio)

        if escolha_jogador in portas_disponiveis:
            portas_disponiveis.remove(escolha_jogador)

        porta_aberta = random.choice(portas_disponiveis) #2/3 das vezes essa lista so tem uma porta... pq? pq 1/3 vezes o jogador escolhe a porta com o premio, ou seja, 2/3 a escolha do jogador ainda vai estar na lista, e como o apresentador nao pode abrir a porta dele, ela é removida(a que o jogador escolheu, e a com o premio ja tinha sido removida). ou seja, 2/3 das vezes essa escolha nao é de fato aleatoria pq so restou uma porta aqui

        # Jogador decide se quer mudar de porta
        mudar_porta = random.choice([True, False])

        # Atualiza a escolha do jogador se ele decidir mudar
        if mudar_porta:
            print("Mudou de porta")
            mudou = mudou + 1
            portas_disponiveis = [1, 2, 3]
            portas_disponiveis.remove(escolha_jogador)
            portas_disponiveis.remove(porta_aberta)
            escolha_jogador = portas_disponiveis[0]
        else:
            print("Nao mudou de porta")
            nmudou = nmudou + 1

        # Verifica se o jogador ganhou
        if escolha_jogador == porta_com_premio:
            if mudar_porta:
                vitorias_com_mudar += 1
                print("Ganhou!")
            else:
                vitorias_sem_mudar += 1
                print("Ganhou!")
        else:
            print("Perdeu!")
        
        print("")

    # Imprime os resultados
                
    r1 = (vitorias_sem_mudar/nmudou) 
    r2 = (vitorias_com_mudar/mudou) 

    print(f"Vitorias sem mudar de porta: {vitorias_sem_mudar}, em um total de {nmudou}. Taxa de acerto: {r1:.2%}")
    print(f"Vitorias mudando de porta: {vitorias_com_mudar}, em um total de {mudou}. Taxa de acerto: {r2:.2%}")

# Número de simulações
num_simulacoes = 100000

# Executa a simulação
monty_hall_simulacao(num_simulacoes)
