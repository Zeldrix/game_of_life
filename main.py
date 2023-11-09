import pygame
import random

pygame.init()
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
grid_case = 10
grid_size = int(screen_size/grid_case)
clock = pygame.time.Clock()
running = True

next_cases = [[] for _ in range(grid_size)]

cases = [[] for _ in range(grid_size)]
for x in range(grid_size):
    next_cases[x] = [None] * grid_size
    cases[x] = [None] * grid_size
    for y in range(0, grid_size):
        cases[x][y] = random.randint(0, 1)



print(cases)

def cellNextState(x, y, cells):
    e = cells[x][y]
    s = 0
    # Check borders
    if x <= 0:
        x_min = x
    else:
        x_min = x - 1
    if x >= grid_size-1:
        x_max = x
    else:
        x_max = x + 1

    if y <= 0:
        y_min = y
    else:
        y_min = y - 1
    if y >= grid_size-1:
        y_max = y
    else:
        y_max = y + 1

    for x_check in range(x_min, x_max+1):
        for y_check in range(y_min, y_max+1):
            if cells[x_check][y_check] == 1 and not(x_check == x and y_check == y):
                s += 1

    if s == 3:
        e = 1
    elif s < 2 or s > 3:
        e = 0

    #print(x, y, s, e)
    #print('x:', x, x_min, x_max)
    #print('y:', y, y_min, y_max)
    #print('s:', s, 'e:', e)
    return e


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            if cases[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 0),
                                 pygame.Rect(x * grid_case, y * grid_case, grid_case, grid_case))
            else:
                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(x * grid_case, y * grid_case, grid_case, grid_case))
            pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(x*grid_case, y*grid_case, grid_case, grid_case), 1)
            next_cases[x][y] = cellNextState(x, y, cases)

    for x in range(0, grid_size):
        for y in range(0, grid_size):
            cases[x][y] = next_cases[x][y]
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(3)  # limits FPS to 60

pygame.quit()