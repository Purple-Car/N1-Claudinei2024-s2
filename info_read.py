import json

def read_distances_array():
    with open('arrays.json', 'r') as file:
        data = json.load(file)
        return data['arr_posicoes']
    
def read_deliveries_array():
    with open('arrays.json', 'r') as file:
        data = json.load(file)
        return data['arr_entregas']