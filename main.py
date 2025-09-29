import pygame
from src.display import display_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    grid : set = {(0,0)}
    coordinates : list = [0,0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_grid(grid, screen, coordinates)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()