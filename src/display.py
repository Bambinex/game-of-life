import pygame

def display_grid(grid: set,
                  screen: pygame.surface.Surface, 
                  coords: list) -> None:
    
    for i in range(screen.get_width() // 20):
        for j in range(screen.get_height() // 20):
            if tuple((coords[0] + i, coords[1] + j)) in grid:
                pygame.draw.rect(screen, 
                                 "white", 
                                 pygame.Rect((coords[0] + i)*20, (coords[1] + j)*20, 20, 20))
            else:
                pygame.draw.rect(screen, 
                                 "black", 
                                 pygame.Rect((coords[0] + i)*20, (coords[1] + j)*20, 20, 20))
    
    for i in range(screen.get_width() // 20):
        pygame.draw.line(screen, "white", (i*20, 0), (i*20, screen.get_width()))
    
    for i in range(screen.get_height() // 20):
        pygame.draw.line(screen, "white", (0, i*20), (screen.get_width(), i*20))
    
    pygame.display.flip()