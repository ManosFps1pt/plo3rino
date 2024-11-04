import pygame

pygame.init()

V2 = pygame.math.Vector2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WIDTH = 3.5
HEIGHT = 3.5
MULT = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

drawing_size = V2(WIDTH * MULT, HEIGHT * MULT)
drawing_pos = V2(SCREEN_WIDTH // 2 - drawing_size.x // 2, SCREEN_HEIGHT // 2 - drawing_size.y // 2)
drawing_rect = pygame.Rect(drawing_pos, drawing_size)

pixel_list: list[pygame.Rect] = []
run = True
last_click = None
while run:
    clock.tick()
    screen.fill("#000015")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pressed()[0]:
        ...

    pygame.draw.rect(screen, "#000000", drawing_rect)

    pygame.display.update()
