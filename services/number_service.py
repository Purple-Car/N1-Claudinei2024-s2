from .interface_service import *

# Cores Texto
RESET = "\033[0m"
BRIGHT_RED = "\033[91m"

#Isso aceita um input e retorna apenas quando for digitado um número, contido entre min e max (incluíndo os dois)
def quantity_input(min, max, txt):
    show_cursor()
    
    while True:
        move_cursor(0, 0)
        clear_line()
        
        quantity = input(
            f"{txt} (mínimo {min}, máximo {max}): "
        )

        try:
            quantity = int(quantity)

            if quantity < min:
                clear_line()
                print(f"O programa demanda um valor acima de {min - 1}")
            elif quantity > max:
                clear_line()
                print(f"O programa demanda um valor abaixo de {max + 1}!")
            else:
                return quantity

        except ValueError:
            clear_line()
            print(f"{BRIGHT_RED}O valor inserido não é um número, insira algo válido!{RESET}")
            
#Isso cria um array preenchido por 0
def make_array(row, col, arr):
    for x in range(row):
        if(x > 0):
                arr.append([])
        
        for y in range(col):
            arr[x].append(0)
            
    return arr
            
#Isso popula o array de entregas com as letras na posição 1 de cada fileira
def fill_destinations(row, arr):
    for x in range(row):
        arr[x][1] = chr(ord('B') + x)