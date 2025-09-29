def update(grid: set):
    updated = set()

    for coords in grid:
        alive = 0

        for neighbour in [
              (coords[0] + 1, coords[1] + 1),
              (coords[0] + 1, coords[1]),
              (coords[0] + 1, coords[1] - 1),
              (coords[0], coords[1] + 1),
              (coords[0], coords[1] - 1),
              (coords[0] - 1, coords[1] + 1),
              (coords[0] - 1, coords[1]),
              (coords[0] - 1, coords[1] - 1)
            ]:
            if neighbour in grid:
                alive += 1
            else:
                a2 = 0
                for n2 in [(neighbour[0] + 1, neighbour[1] + 1),
                           (neighbour[0] + 1, neighbour[1]),
                           (neighbour[0] + 1, neighbour[1] - 1),
                           (neighbour[0], neighbour[1] - 1),
                           (neighbour[0], neighbour[1] + 1),
                           (neighbour[0] - 1, neighbour[1] + 1),
                           (neighbour[0] - 1, neighbour[1]),
                           (neighbour[0] - 1, neighbour[1] - 1)
                ]:
                    if n2 in grid:
                        a2 += 1
                
                if a2 == 3:
                    updated.add(neighbour)

        if alive == 2 or alive == 3:
            updated.add(coords)
    
    return updated