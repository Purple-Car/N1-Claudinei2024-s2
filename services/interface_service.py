import sys
import os
import msvcrt

# Cores Texto
RESET = "\033[0m"
BLACK = "\033[30m"
WHITE = "\033[97m"
GREY = "\033[90m"

# Cores Fundo
BG_BLACK = "\033[40m"
BG_WHITE = "\033[47m"

def draw_deliveries_array(arr, posx, posy):
    move_cursor(0, 2)
    for x in range(len(arr)):
        print("")
        print("  ", end="")
        for y in range(len(arr[0])):
            #is cursor position
            if x == posx and y == posy:
                print(f"{BLACK}{BG_WHITE}{str(arr[x][y]):2}{RESET}", end=" ")
            #not cursor position
            else:
                print(f"{str(arr[x][y]):2}", end=" ")
    
def draw_distances_array(arr, posx, posy):
    move_cursor(0, 2)
    for x in range(len(arr)+1):
        print("")
        for y in range(len(arr[0])+1):
            #if first row
            if x == 0:
                #and first column
                if y == 0 :
                    print("   ", end=" ")
                #other columns
                else:
                    print(f"  {chr(ord('A') + y-1)}", end=" ")
            #other rows
            else:
                #and first column
                if y == 0 :
                    print(f"  {chr(ord('A') + x-1)}", end=" ")
                #other columns
                else:
                    #is cursor position
                    if x-1 == posx and y-1 == posy:
                        print(f"{BLACK}{BG_WHITE}{arr[x-1][y-1]:3}{RESET}", end=" ")
                    #not cursor position
                    else:
                        #position overlap
                        if x == y:
                            print(f"{GREY}{arr[x-1][y-1]:3}{RESET}", end=" ")
                        #not position overlap
                        
                        else:
                            print(f"{arr[x-1][y-1]:3}", end=" ")
     
#Pequenas funções, auto-descritivas
                   
def move_cursor(x, y):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()
    
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')
        
def clear_line():
    sys.stdout.write("\033[2K")
    sys.stdout.flush()
        
def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()    

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
    
def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()