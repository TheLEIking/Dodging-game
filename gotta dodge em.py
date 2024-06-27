import pygame
import random


pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gotta dodge em Game')


player_image = pygame.image.load('player_plane.png')
enemy_image = pygame.image.load('enemy_plane.png')



player_rect = player_image.get_rect()
player_rect.x = SCREEN_WIDTH // 10 - player_rect.width // 10
player_rect.y = SCREEN_HEIGHT - player_rect.height - 0


bullets = []
bullet_speed = 2


enemies = []
enemy_speed = 3
enemy_spawn_time = 60
enemy_spawn_counter = 0


score = 0
font = pygame.font.Font(None, 36)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 10
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += 10
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= 10
    if keys[pygame.K_DOWN] and player_rect.bottom < SCREEN_HEIGHT:
        player_rect.y += 10
    if keys[pygame.K_SPACE]:
        bullets.append(player_rect.midtop)


 
    enemy_spawn_counter += 1
    if enemy_spawn_counter >= enemy_spawn_time:
        enemy_spawn_counter = 1
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = random.randint(0, SCREEN_WIDTH - enemy_rect.width)
        enemy_rect.y = -enemy_rect.height
        enemies.append(enemy_rect)


    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.colliderect(player_rect):
            running = False  
        if enemy.top > SCREEN_HEIGHT:
            enemies.remove(enemy)

    screen.fill(BLACK)
    screen.blit(player_image, player_rect)
    for bullet in bullets:
        screen.blit(bullet_image, bullet)
    for enemy in enemies:
        screen.blit(enemy_image, enemy)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
