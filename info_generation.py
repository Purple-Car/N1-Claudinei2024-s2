from number_service import *
from interface_service import *
import keyboard # type: ignore

def main():
    arr_posicoes = [[]]
    arr_entregas = [[]]
    
    clear_terminal()
    
    while True:
        numb_dest = quantity_input(2, 9, "Defina o número de destinações")
        
        arr_posicoes = make_array(numb_dest, numb_dest, arr_posicoes)
        arr_entregas = make_array(numb_dest, 3, arr_entregas)
        
        #draw_distances_array(arr_posicoes, 0, 0)
        map_define(arr_posicoes)
                
        #print(arr_posicoes)
        #print(arr_entregas)
        break
            
def map_define(arr_posicoes):
    pos_x, pos_y = 0, 0
        
    while True:
        hide_cursor()
        draw_distances_array(arr_posicoes, pos_y, pos_x)
        #print(f"\n{pos_x}, {pos_y}")
        print(f"\n\nEscolha uma posição na matriz usando as setas!")
        print("Pressione ENTER para selecionar ou ESC para continuar.")
        
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed('up'):
                pos_y = ( pos_y - 1 ) % len(arr_posicoes)
            elif keyboard.is_pressed('down'):
                pos_y = ( pos_y + 1 ) % len(arr_posicoes)
            elif keyboard.is_pressed('left'):
                pos_x = ( pos_x - 1 ) % len(arr_posicoes)
            elif keyboard.is_pressed('right'):
                pos_x = ( pos_x + 1 ) % len(arr_posicoes)
            elif keyboard.is_pressed('enter'):
                quantity_input(0, 999, "Insira a distância entre essas duas destinações")
            elif keyboard.is_pressed('esc'):
                break
            
        move_cursor(0, 0)
        clear_line()
        move_cursor(0, 1)
        clear_line()
        move_cursor(0, 2)
    
if __name__ == "__main__":
    main()