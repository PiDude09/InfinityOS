import pygame; from sys import exit; import os; import subprocess

y_offset = 0
x_offset = 0


pygame.init()
screen = pygame.display.set_mode((1920,1080)) # Halfway is 960,540
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()

games = os.listdir('games')
games.sort()

while True:
    x_pos = 250
    os.chdir(f"C:/Users/Daniel/infinityos")
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    game_surf = []
    game_rect = []

    for x in games:
        game_surf.append(pygame.transform.rotozoom((pygame.image.load(f'games/{x}/splashscreen.png').convert_alpha()), 0, 0.2))
    for x in game_surf:
        game_rect.append(x.get_rect(center = (x_pos,540)))
        x_pos += 500

    for x in game_surf:
        game_rect_index = 0
        screen.blit(x, game_rect[game_rect_index])
        
        #if game_rect_index >= len(game_rect):
            #game_rect_index = 0
        game_rect_index += 1

    for x in game_rect:
        mouse_pos = pygame.mouse.get_pos()
        if x.collidepoint(mouse_pos):
            if not pygame.mouse.get_pressed() == (True,False,False):
                pygame.draw.rect(screen,(102, 204, 255),x,width=4)
            elif pygame.mouse.get_pressed() == (True,False,False):
                games_index = game_rect.index(x)
                try:
                    os.chdir(f"games/{games[games_index]}")
                except: None
                for z in games:
                    try: os.listdir().index("main.py")
                    except: None
                    else: subprocess.call(["python", "main.py"])

    print(game_rect, game_surf, games)

    pygame.display.update()
    clock.tick(60)