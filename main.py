#################################################
#                                               #
#        Michael Theisen                        #
#        February 6th, 2024                     #
#        Conway's Game of Lifed Maze Game       #
#          with help from NeuralNine            #
#                                               # 
#################################################

import time 
import pygame
import numpy as np

COLOR_BG = (255, 255, 255) # Color for the background 
COLOR_GRID = (40, 40, 40) # Color for the grid lighter
COLOR_DIE_NEXT = (170, 170, 170) # color for the die next 
COLOR_ALIVE_NEXT = (40, 40, 40) # color for next alive block . 
#SIZE = 10

# update function has the drawing process and game logic
def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        # game rules
        if cells[row, col] == 1: # if the cell we are looking at has the state 1, (is alive) 
            # if it is alone or only has 1 neighbor, it dies. 
            if alive < 2 or alive > 3:
                if with_progress:
                        color = COLOR_DIE_NEXT
        # if it has 2 or 3 neighbors, it survives.         
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT    
        # if it has more it dies
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((1500, 800))

    cells = np.zeros((80, 150))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()

