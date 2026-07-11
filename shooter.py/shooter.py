import pygame, random
pygame.init()

win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.image.load("player.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))
enemy_img = pygame.image.load("emeny.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

projectiles = []
enemies = []
enemy_projectiles = []
score = 0
health = 20
font = pygame.font.SysFont(None, 36)
j = 8
y = 2
run = True
map_img = pygame.image.load("bg.png")
map_img = pygame.transform.scale(map_img, (800, 600))
while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_x:
            proj_rect = pygame.Rect(player_x + player.get_width()//2 - 2, player_y, 5, 30)
            projectiles.append(proj_rect)
    win.blit(map_img, (0, 0))


    mouse_x, mouse_y = pygame.mouse.get_pos()
    player_x = mouse_x - player.get_width()//2
    player_y = mouse_y - player.get_height()//2
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    win.blit(player, (player_x, player_y))

    if random.randint(0, 50) == 1:
        x = random.randint(0, 750)
        enemies.append(pygame.Rect(x, 0, 50, 50))

    for proj in projectiles[:]:
        proj.y -= j
        if proj.y + proj.height < 0:
            projectiles.remove(proj)
        else:
            pygame.draw.rect(win, (0, 255, 0), proj)

    for enemy_rect in enemies[:]:
        enemy_rect.y += y
        if enemy_rect.y > 600:
            enemies.remove(enemy_rect)
        else:
            win.blit(enemy_img, (enemy_rect.x, enemy_rect.y))

    # Random bullets from top edge
    if random.randint(0, 20) == 1:
        bullet_x = random.randint(0, 795)
        bullet = pygame.Rect(bullet_x, 0, 5, 15)
        enemy_projectiles.append(bullet)

    for bullet in enemy_projectiles[:]:
        bullet.y += 12
        if bullet.y > 600:
            enemy_projectiles.remove(bullet)
        else:
            pygame.draw.rect(win, (255, 0, 0), bullet)
            if bullet.colliderect(player_rect):
                enemy_projectiles.remove(bullet)
                health -= 1
                if health <= 0:
                    run = False

    for proj in projectiles[:]:
        for enemy_rect in enemies[:]:
            if proj.colliderect(enemy_rect):
                projectiles.remove(proj)
                enemies.remove(enemy_rect)
                score += 1
                break

    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    health_surface = font.render(f"Health: {health}", True, (255, 0, 0))
    win.blit(score_surface, (10, 10))
    win.blit(health_surface, (10, 40))
    
    pygame.display.update()
    y += 0.0009
print(f"Your score: {score}")
