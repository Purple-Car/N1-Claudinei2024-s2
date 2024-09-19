from services.number_service import *
from services.interface_service import *
import keyboard # type: ignore #pip install keyboard [!]
import json

#Roda a lógica principal do programa
def main():
    arr_posicoes = [[]]
    arr_entregas = [[]]
    
    clear_terminal()
    
    numb_dest = quantity_input(2, 9, "Defina o número de destinações")
        
    arr_posicoes = make_array(numb_dest, numb_dest, arr_posicoes)
    arr_entregas = make_array(numb_dest - 1, 3, arr_entregas)
        
    fill_destinations(len(arr_entregas), arr_entregas)
        
    map_define(arr_posicoes)
    clear_terminal()
    del_define(arr_entregas)
    
    save_json(arr_posicoes, arr_entregas)
          
    print("Salvo os seguintes arrays para 'entregas.json'")      
    print(arr_posicoes)
    print(arr_entregas)
    
#Salva os arrays em um JSON
def save_json(arr_posicoes, arr_entregas):
    with open('entregas.json', 'w') as file:
        json.dump({'arr_posicoes': arr_posicoes, 'arr_entregas': arr_entregas}, file, indent=4)
         
#Roda a lógica da interface de definição das horas de partida e valor das entregas
def del_define(arr_entregas):
    pos_x, pos_y = 0, 0
    
    while True:
        hide_cursor()
        draw_deliveries_array(arr_entregas, pos_y, pos_x)
        #print(f"\n{pos_x}, {pos_y}")
        print(f"\n\nEscolha uma posição na matriz usando as setas!")
        print("Pressione ENTER para selecionar ou ESC para continuar.")
        
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed('up'):
                pos_y = ( pos_y - 1 ) % len(arr_entregas)
            elif keyboard.is_pressed('down'):
                pos_y = ( pos_y + 1 ) % len(arr_entregas)
            elif keyboard.is_pressed('left'):
                pos_x = ( pos_x - 2 ) % 4
            elif keyboard.is_pressed('right'):
                pos_x = ( pos_x + 2 ) % 4
            elif keyboard.is_pressed('enter') and pos_x != 1:
                flush_input()
                arr_entregas[pos_y][pos_x] = quantity_input(0, 99, "Insira o valor desejado")
            elif keyboard.is_pressed('esc'):
                break
        
        move_cursor(0, 1)
        clear_line()
        move_cursor(0, 2)
        clear_line()
       
#Roda a lógica da interface de definição das distâncias entre os pontos de entrega
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
            elif keyboard.is_pressed('enter') and pos_x != pos_y:
                flush_input()
                numb = quantity_input(0, 999, "Insira a distância entre essas duas destinações")
                arr_posicoes[pos_y][pos_x], arr_posicoes[pos_x][pos_y] = numb, numb
            elif keyboard.is_pressed('esc'):
                break
            
        move_cursor(0, 1)
        clear_line()
        move_cursor(0, 2)
        clear_line()
    
if __name__ == "__main__":
    main()