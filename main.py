import pygame
from src.rules import update
from src.display import display_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    grid : set = {(5,5), (5,6), (5,7)}
    coordinates : list = [0,0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_grid(grid, screen, coordinates)
        grid = update(grid)

        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()