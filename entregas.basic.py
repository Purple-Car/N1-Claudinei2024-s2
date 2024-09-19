import itertools

def get_user_input():
    """
    Função para obter entradas do usuário diretamente no console.
    """
    # Destinos fixos para este exemplo
    destinations = ['A', 'B', 'C', 'D']

    # Matriz de conexões fixa para este exemplo
    print("Digite a matriz de conexões (4 linhas de números separados por vírgula):")
    matrix = []
    for _ in range(4):
        row = list(map(int, input().strip().split(', ')))
        matrix.append(row)

    # Entregas fixas para este exemplo
    deliveries = []
    print("Digite as entregas (horário de saída, destino e bônus separados por vírgula):")
    deliveries.append((0, 'B', 1))
    deliveries.append((5, 'C', 10))
    deliveries.append((10, 'D', 8))

    return destinations, matrix, deliveries

def calculate_route_time(matrix, route):
    """
    Função para calcular o tempo total necessário para percorrer uma rota entre destinos.
    """
    total_time = 0
    for i in range(len(route) - 1):
        total_time += matrix[route[i]][route[i + 1]]
    return total_time

def calculate_profit(matrix, destinations, deliveries, sequence):
    """
    Função para calcular o lucro total baseado na sequência de entregas.
    """
    total_profit = 0
    current_time = 0
    for delivery in sequence:
        start_time, destination, bonus = delivery
        destination_index = destinations.index(destination)
        if current_time <= start_time:
            # Calcula o tempo para entregar e retornar ao ponto de partida
            route = [0, destination_index, 0]  # A = 0, D = destination_index, A = 0
            delivery_time = calculate_route_time(matrix, route)
            if current_time + delivery_time <= start_time:
                total_profit += bonus
                current_time = start_time + delivery_time
            else:
                # Se não for possível entregar a tempo, ignore a entrega
                break
    return total_profit

def find_best_sequence(destinations, matrix, deliveries):
    """
    Função para encontrar a melhor sequência de entregas e o lucro máximo.
    """
    max_profit = 0
    best_sequence = None
    for sequence in itertools.permutations(deliveries):
        profit = calculate_profit(matrix, destinations, deliveries, sequence)
        if profit > max_profit:
            max_profit = profit
            best_sequence = sequence
    return best_sequence, max_profit

def display_results(sequence, profit):
    """
    Função para exibir a sequência de entregas e o lucro total.
    """
    if sequence:
        print("Melhor sequência de entregas:")
        for delivery in sequence:
            print(f"Saída: {delivery[0]}, Destino: {delivery[1]}, Bônus: {delivery[2]}")
        print(f"Lucro total: {profit}")
    else:
        print("Nenhuma entrega possível.")

# Código principal
destinations, matrix, deliveries = get_user_input()
print(destinations)
print(matrix)
print(deliveries)
best_sequence, max_profit = find_best_sequence(destinations, matrix, deliveries)
display_results(best_sequence, max_profit)
 