import itertools
from info_read import read_distances_array, read_deliveries_array

def get_data_from_json():
    """
    Function to retrieve the destinations, matrix, and deliveries from the JSON file.
    """
    # Ler matrix e deliveries do JSON
    matrix = read_distances_array()
    deliveries = read_deliveries_array()

    # Gerar destinations dinâmicamente baseado no tamanho da matrix
    matrix_size = len(matrix)
    destinations = [chr(65 + i) for i in range(matrix_size)]  # 'A', 'B', 'C', ...

    return destinations, matrix, deliveries

def calculate_route_time(matrix, route):
    """
    Function to calculate the total time required to travel a route between destinations.
    """
    total_time = 0
    for i in range(len(route) - 1):
        total_time += matrix[route[i]][route[i + 1]]
    return total_time

def calculate_profit(matrix, destinations, deliveries, sequence):
    """
    Function to calculate the total profit based on the sequence of deliveries.
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
    Function to find the best delivery sequence and the maximum profit.
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
    Function to display the delivery sequence and the total profit.
    """
    if sequence:
        print("Melhor sequência de entregas:")
        for delivery in sequence:
            print(f"Saída: {delivery[0]}, Destino: {delivery[1]}, Bônus: {delivery[2]}")
        print(f"Lucro total: {profit}")
    else:
        print("Nenhuma entrega possível.")

# Código principal
destinations, matrix, deliveries = get_data_from_json()
#print(destinations)
#print(matrix)
#print(deliveries)
best_sequence, max_profit = find_best_sequence(destinations, matrix, deliveries)
display_results(best_sequence, max_profit)