from board import Board
#from ball import Ball
import pygame

def main():
    board = Board()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        board.draw()

    pygame.quit()

if __name__ == "__main__":
    main()