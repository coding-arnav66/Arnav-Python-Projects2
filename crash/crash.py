import pygame, random
n = 0
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
y = 300
left_lane_x = 290
right_lane_x = 430
merc_x = random.choice([left_lane_x, right_lane_x])
merc_y = 230
font = pygame.font.SysFont(None, 36)
running = True
map_img = pygame.image.load("myCar.png.png")
map_img = pygame.transform.scale(map_img, (250, 230))
merc = pygame.image.load("mmerc.png")
merc = pygame.transform.scale(merc, (100, 100))
bush_img = pygame.image.load("bush.png")
bush_img = pygame.transform.scale(bush_img, (150, 160))
treeimg = pygame.image.load("myTree.png")
treeimg = pygame.transform.scale(treeimg, (120, 300))
coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (50, 50))
grass = pygame.image.load("ghaas.png")
grass = pygame.transform.scale(grass, (100, 100 ))
myCar = (200, 400)
speed = 6
xfortree1, xfortree2 = -8, 630
xforbush1, xforbush2 = 50, 630
y31, y32 = 250, 400
y21, y22 = 70, 130
health = 250
coins = 0
coin_x = random.choice([left_lane_x, right_lane_x])
coin_y = 350
n1 = 510
n2 = 310
n3 = 110
n4 = 310
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (0, 200, 0), (0, 300, 800, 300))
    pygame.draw.polygon(screen, (50, 50, 50), [(300, 300), (500, 300), (650, 600), (150, 600)])

    if y <= 700:
        pygame.draw.rect(screen, (255, 255, 255), (395, y, 10, 100))
        y += 50
    else:
        y = 300

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        myCar = (370, 400)
    if keys[pygame.K_LEFT]:
        myCar = (200, 400)

    if y21 <= 850 and y22 <= 850 and y31 <= 900 and y32 <= 900:
        y21 += 5; y22 += 5; y31 += 10; y32 += 10
        xforbush1 -= 5; xforbush2 += 5
        xfortree1 -= 5; xfortree2 += 5
    else:
        xfortree1, xfortree2 = -8, 630
        xforbush1, xforbush2 = 50, 630
        y31, y32 = 250, 400
        y21, y22 = 70, 130

    merc_y += speed
    coin_y += speed
    if merc_y > 600:
        merc_y = 230
        merc_x = random.choice([left_lane_x, right_lane_x])
    if coin_y > 600:
        coin_y = 350
        coin_x = random.choice([left_lane_x, right_lane_x])

    screen.blit(merc, (merc_x, merc_y))
    screen.blit(map_img, myCar)
    screen.blit(treeimg, (xfortree1, y21))
    screen.blit(treeimg, (xfortree2, y22))
    screen.blit(bush_img, (xforbush1, y31))
    screen.blit(bush_img, (xforbush2, y32))
    screen.blit(grass, (n1, n2))
    screen.blit(grass, (n3, n4))
    pygame.draw.circle(screen, (255, 255, 0), (700, 100), 50)
    pygame.draw.ellipse(screen, (255, 255, 255), (100, 100, 120, 60))
    pygame.draw.ellipse(screen, (255, 255, 255), (300, 80, 150, 70))
    pygame.draw.ellipse(screen, (255, 255, 255), (550, 120, 130, 65))
    if n1 <= 999:
        n1 += 5
        n2 += 5
        n3 -= 5
        n4 += 5 
    elif n % 157 == 0:
        n1 = 510
        n2 = 230
        n3 = 110
        n4 = 230

    screen.blit(coin, (coin_x, coin_y))
    speed += 0.009
    n += 1
    merc_rect = pygame.Rect(merc_x, merc_y, 100, 100)
    myCar_rect = pygame.Rect(myCar[0]+75, myCar[1]+60, 100, 100)
    coin_rect = pygame.Rect(coin_x, coin_y, 50, 50)

    screen.blit(font.render("Health:", True, (255, 255, 0)), (0, 3))
    pygame.draw.rect(screen, (255, 0, 0), (100, 5, 250, 20))
    pygame.draw.rect(screen, (0, 255, 0), (100, 5, health, 20))
    screen.blit(font.render(f"Coins: {coins}", True, (255, 255, 0)), (0, 30))

    if merc_rect.colliderect(myCar_rect):
        health = max(0, health - 1)
    if coin_rect.colliderect(myCar_rect):
        coins += 1
        coin_y = random.randint(50, 200)
        coin_x = random.choice([left_lane_x, right_lane_x])

    if health <= 0:
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
print(f"Your score is: {coins}...")
