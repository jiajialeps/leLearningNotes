import pygame
import random

# 初始化 Pygame
pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("飞机大战")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 创建玩家飞机
player_image = pygame.Surface((50, 40))
player_image.fill(GREEN)
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

# 创建敌机
enemy_image = pygame.Surface((50, 40))
enemy_image.fill(RED)

# 敌机列表
enemies = []
enemy_count = 5  # 敌机数量
for _ in range(enemy_count):
    enemy_rect = enemy_image.get_rect(topleft=(random.randint(0, WIDTH - 50), random.randint(-150, -50)))
    enemies.append(enemy_rect)

# 子弹设置
bullet_image = pygame.Surface((5, 10))
bullet_image.fill(WHITE)
bullets = []

# 游戏循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 控制飞机移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5
    if keys[pygame.K_SPACE]:  # 按空格键发射子弹
        bullet_rect = bullet_image.get_rect(midbottom=player_rect.midtop)
        bullets.append(bullet_rect)

    # 更新敌机位置
    for enemy_rect in enemies:
        enemy_rect.y += 5
        if enemy_rect.top > HEIGHT:  # 如果敌机超出屏幕
            enemy_rect.topleft = (random.randint(0, WIDTH - 50), random.randint(-150, -50))  # 重新生成敌机

    # 更新子弹位置
    for bullet in bullets[:]:  # 使用切片避免修改列表时出错
        bullet.y -= 10
        if bullet.bottom < 0:  # 如果子弹超出屏幕
            bullets.remove(bullet)

    # 碰撞检测
    for bullet in bullets[:]:  # 使用切片避免修改列表时出错
        for enemy_rect in enemies[:]:  # 对每个敌机进行碰撞检测
            if bullet.colliderect(enemy_rect):
                bullets.remove(bullet)  # 移除子弹
                enemy_rect.topleft = (random.randint(0, WIDTH - 50), random.randint(-150, -50))  # 重新生成敌机
                break  # 只处理一次碰撞

    # 绘制
    screen.fill(BLACK)
    screen.blit(player_image, player_rect)  # 绘制玩家飞机
    for enemy_rect in enemies:
        screen.blit(enemy_image, enemy_rect)  # 绘制所有敌机
    for bullet in bullets:
        screen.blit(bullet_image, bullet)  # 绘制子弹

    pygame.display.flip()  # 更新显示
    clock.tick(60)  # 控制帧率

pygame.quit()
