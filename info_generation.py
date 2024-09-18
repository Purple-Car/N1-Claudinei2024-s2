from number_service import *
from interface_service import *

def main():
    arr_posicoes = [[]]
    arr_entregas = [[]]
    
    while True:
        numb_dest = quantity_input(2, 9)
        
        arr_posicoes = make_array(numb_dest, numb_dest, arr_posicoes)
        arr_entregas = make_array(numb_dest, 3, arr_entregas)
        
        draw_distances_array(arr_posicoes, 0, 0)
                
        print(arr_posicoes)
        print(arr_entregas)
        break
            
if __name__ == "__main__":
    main()