import pygame, random, time
pygame.init()
gamee = []
timee = []
def landing():
    win = pygame.display.set_mode((800, 600))
    x, y = 0, 0
    game = "running"
    run = True
    clock = pygame.time.Clock()
    obstacles = []
    font = pygame.font.SysFont(None, 48)

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and x < 790:
            x += 10
        if keys[pygame.K_LEFT] and x > 0:
            x -= 10
        if keys[pygame.K_UP] and y > 0:
            y -= 10
        if keys[pygame.K_DOWN] and y < 590:
            y += 10

        if keys[pygame.K_RETURN]:
            n1, n2, n3, n4 = random.randint(-10, 800), random.randint(-10, 600), random.randint(100, 800), random.randint(100, 800)
            obstacles = [pygame.Rect(n1, n2, n3, n4)]

        map_img = pygame.image.load("map.png")
        map_img = pygame.transform.scale(map_img, (800, 600))
        win.blit(map_img, (0, 0))

        player_rect = pygame.Rect(x, y, 10, 10)
        pygame.draw.rect(win, (0, 255, 0), player_rect)

        for obs in obstacles:
            pygame.draw.rect(win, (255, 165, 0), obs)
            if player_rect.colliderect(obs):
                game = "lost"
                text_surface = font.render("Player Eliminated!", True, (255, 255, 0))
                win.blit(text_surface, (250, 300))
                run = False
            else:
                gamee.append("win")
                text_surface = font.render("You won!", True, (255, 0, 255))
                win.blit(text_surface, (300, 300))
                run = False

        pygame.display.update()
        clock.tick(60)
        if run == False:
            time.sleep(2)

    print(game)
def shoot():
    font = pygame.font.SysFont(None, 36)
    win = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
  
    tart_ticks = pygame.time.get_ticks()  
    enemy_img = pygame.image.load("enemy.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (20, 30))

    x, y = 400, 300
    dx, dy = 5, 4
    radius = 5
    health = 25

    run = True
    for i in range(20):
        enemy_x = random.randint(0, 800 - 80)
        enemy_y = random.randint(0, 600 - 120)
        while run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False

            map_img = pygame.image.load("background.png")
            map_img = pygame.transform.scale(map_img, (800, 600))
            win.blit(map_img, (0, 0))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and x < 790:
                x += 20
            if keys[pygame.K_LEFT] and x > 0:
                x -= 20
            if keys[pygame.K_UP] and y > 0:
                y -= 20
            if keys[pygame.K_DOWN] and y < 590:
                y += 20
            win.blit(enemy_img, (enemy_x, enemy_y))
            enemy_rect = enemy_img.get_rect(topleft=(enemy_x, enemy_y))
            circle_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

            if enemy_rect.colliderect(circle_rect) and keys[pygame.K_x]:
                if i+1 == 20:
                    timee.append(elapsed_time)
                if i + 1 == 1:
                    print("First kill!")
                    break
                else:
                    print(f"{i+1} players down!")
                break

            pygame.draw.circle(win, (255, 255, 0), (x, y), radius)
            elapsed_time = (pygame.time.get_ticks() - tart_ticks) // 1000
            probab = [False]*50 + [True]
            if random.choice(probab):
                health -= 1
            timer_surface = font.render(f"Time: {elapsed_time}, Health: {health}", True, (255, 255, 255))
            win.blit(timer_surface, (10, 10))
            if health == 0:
                gamee.append("lost game 2")
                break

            pygame.display.update()
            clock.tick(60)

    pygame.quit()
print("welcome to the \'ULTIMATE BATTLE LITE\' game!\nFor the first level, move your green coloured box situated at top lef using arrow keys.\nSelect a place to stay and press enter after that.\nIf you are out of the yellow zone, congrats! You can move to the next game!")
masti = input("Press \'enter\' to continue: ")
landing()
if "win" in gamee:
    print("Congrats, you have won the level one... Now time for the final level! Find the enemy on the screen and locate the green dot on them using arrows.\nAfter that, press \'x\' to shoot! Kill 20 such players...")
    masti = input("Press \'enter\' to continue: ")
    shoot()
if timee[0] <=60:
    print("Since you took less than 60 seconds, you won!")
elif "lost game 2" in gamee:
    print("Health gone! You lost...")
else:
    print("You took too much time, you lost! Better luck next time...")
