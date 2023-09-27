import pygame
# 游戏初始化，窗口，初始位置，设置游戏时钟
pygame.init()

# 返回结果是主屏幕，要记录
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./image/buellt_image/wsparticle_backgrounddandelion.png')
screen.blit(bg, (0, 0))

# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load('./image/aircraft_image/main_2.png')
screen.blit(hero, (200, 500))

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 游戏的正式开始
# 设置刷新帧率60，检测用户交互，更新所有图像位置，更新屏幕显示
i = 0
while True:
# 可以指定循环体内部的代码执行频率
    clock.tick(1)

    print(i)
    i += 1
    pass

pygame.quit()