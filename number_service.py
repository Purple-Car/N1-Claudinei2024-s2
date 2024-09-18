#Isso aceita um input e retorna apenas quando for digitado um número, contido entre min e max (incluíndo os dois)
def quantity_input(min, max):
    while True:
        quantity = input(
            f"Defina o número de destinações (mínimo {min}, máximo {max}): "
        )

        try:
            quantity = int(quantity)

            if quantity < min:
                print(f"O programa demanda um valor acima de {min - 1}")
            elif quantity > max:
                print(f"O programa demanda um valor abaixo de {max + 1}!")
            else:
                return quantity

        except ValueError:
            print("O valor inserido não é um número, insira algo válido!")
            
#Isso cria um array preenchido por 0
def make_array(row, col, arr):
    for x in range(row):
        if(x > 0):
                arr.append([])
        
        for y in range(col):
            arr[x].append(0)
            
    return arr
            