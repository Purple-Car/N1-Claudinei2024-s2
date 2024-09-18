import string

# Define color codes
RESET = "\033[0m"
BLACK = "\033[30m"
WHITE = "\033[37m"

# Background colors
BG_BLACK = "\033[40m"
BG_WHITE = "\033[47m"

def draw_distances_array(arr, posx, posy):
    for x in range(len(arr)+1):
        print("")
        for y in range(len(arr[0])+1):
            if x == 0:
                if y == 0 :
                    print("   ", end=" ")
                    
                else:
                    print(f"  {chr(ord('A') + y-1)}", end=" ")
                
            else:
                if y == 0 :
                    print(f"  {chr(ord('A') + x-1)}", end=" ")
                    
                else:
                    if x-1 == posx and y-1 == posy:
                        print(f"{BLACK}{BG_WHITE}{arr[x-1][y-1]:3}{RESET}", end=" ")
                    
                    else:
                        print(f"{arr[x-1][y-1]:3}", end=" ")