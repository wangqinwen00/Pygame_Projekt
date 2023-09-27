# 图像保存在磁盘上，如果要使用，现要将其加载到内存

import pygame

pygame.init()

# 返回结果是主屏幕，要记录
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./image/buellt_image/wsparticle_backgrounddandelion.png')
screen.blit(bg, (0, 0))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()