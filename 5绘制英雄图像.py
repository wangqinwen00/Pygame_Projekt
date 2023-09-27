import pygame

pygame.init()

# 返回结果是主屏幕，要记录
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./image/buellt_image/wsparticle_backgrounddandelion.png')
screen.blit(bg, (0, 0))
pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load('./image/aircraft_image/main_2.png')
screen.blit(hero, (200, 500))
pygame.display.update()


# 游戏循环
while True:
    pass

pygame.quit()