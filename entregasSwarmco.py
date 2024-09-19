import random
from info_read import read_distances_array, read_deliveries_array

numero_formigas = 10
numero_iteracoes = 100
alfa = 1
beta = 2
taxa_evaporacao = 0.5
deposito_feromonio = 100
limite_tempo = 30

feromonios = {}

def carregar_dados_json():
    matriz_conexoes = read_distances_array()
    destinos = [chr(65 + i) for i in range(len(matriz_conexoes))]
    
    conexoes = {}
    for i, origem in enumerate(destinos):
        conexoes[origem] = {}
        for j, destino in enumerate(destinos):
            if matriz_conexoes[i][j] != 0:
                conexoes[origem][destino] = matriz_conexoes[i][j]
                feromonios[(origem, destino)] = 1

    entregas = []
    entregas_json = read_deliveries_array()
    for entrega in entregas_json:
        entregas.append({
            'inicio': entrega[0],
            'destino': entrega[1],
            'bonus': entrega[2]
        })

    return conexoes, entregas

def calcular_distancia(rota, conexoes):
    distancia = 0
    for i in range(len(rota) - 1):
        inicio = rota[i]
        fim = rota[i + 1]
        if fim in conexoes[inicio]:
            distancia += conexoes[inicio][fim]

    distancia += conexoes[rota[-1]]['A']
    return distancia

def calcular_bonus_total(rota, conexoes, entregas, limite_tempo):
    bonus_total = 0
    tempo_atual = 0
    for i in range(len(rota) - 1):
        inicio = rota[i]
        fim = rota[i + 1]
        if fim in conexoes[inicio]:
            tempo_atual += conexoes[inicio][fim]
        if tempo_atual <= limite_tempo:
            for entrega in entregas:
                if entrega['destino'] == fim and tempo_atual >= entrega['inicio']:
                    bonus_total += entrega['bonus']
                    break
    return bonus_total if tempo_atual <= limite_tempo else 0

def escolher_proximo_no(no_atual, visitados, feromonios, conexoes, limite_tempo, rota):
    nos_disponiveis = [no for no in conexoes[no_atual] if no not in visitados]
    probabilidades = []
    probabilidade_total = 0

    for proximo_no in nos_disponiveis:
        feromonio = feromonios.get((no_atual, proximo_no), 1)
        heuristica = 1 / (conexoes[no_atual][proximo_no] + 1)
        tempo_para_proximo_no = conexoes[no_atual][proximo_no]

        tempo_total = sum(conexoes[rota[i]][rota[i + 1]] for i in range(len(rota) - 1)) + tempo_para_proximo_no

        if tempo_total + conexoes[proximo_no].get('A', 0) <= limite_tempo:
            prob = (feromonio ** alfa) * (heuristica ** beta)
            probabilidades.append(prob)
            probabilidade_total += prob
        else:
            probabilidades.append(0)

    if probabilidade_total > 0:
        probabilidades = [p / probabilidade_total for p in probabilidades]
        return random.choices(nos_disponiveis, weights=probabilidades)[0]
    else:
        return None

def atualizar_feromonios(rotas, bonus_totais, feromonios, conexoes):
    for rota, bonus in zip(rotas, bonus_totais):
        distancia_rota = calcular_distancia(rota, conexoes)
        for i in range(len(rota) - 1):
            aresta = (rota[i], rota[i + 1])
            feromonios[aresta] = (1 - taxa_evaporacao) * feromonios.get(aresta, 1) + deposito_feromonio * bonus / distancia_rota
            if calcular_distancia(rota, conexoes) <= limite_tempo:
                feromonios[aresta] *= 1.5

def aco(conexoes, entregas):
    melhor_rota = None
    melhor_bonus = 0

    for _ in range(numero_iteracoes):
        rotas = []
        bonus_totais = []

        for _ in range(numero_formigas):
            rota = ['A']
            visitados = set(rota)
            no_atual = 'A'

            while len(visitados) < len(conexoes):
                proximo_no = escolher_proximo_no(no_atual, visitados, feromonios, conexoes, limite_tempo, rota)
                if proximo_no is None:
                    break
                rota.append(proximo_no)
                visitados.add(proximo_no)
                no_atual = proximo_no

            if len(rota) > 1:
                rotas.append(rota)
                bonus_total = calcular_bonus_total(rota, conexoes, entregas, limite_tempo)
                bonus_totais.append(bonus_total)

                if bonus_total > melhor_bonus:
                    melhor_bonus = bonus_total
                    melhor_rota = rota

        atualizar_feromonios(rotas, bonus_totais, feromonios, conexoes)

    return melhor_rota, melhor_bonus

conexoes, entregas = carregar_dados_json()
melhor_rota, melhor_bonus = aco(conexoes, entregas)

print(f'Melhor rota: {melhor_rota} com bônus total: {melhor_bonus}')
