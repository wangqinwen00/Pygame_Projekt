import pygame
# 游戏初始化，窗口，初始位置，设置游戏时钟
pygame.init()

# 返回结果是主屏幕，要记录
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load('./image/aircraft_image/image_1.jpg')
screen.blit(bg, (0, 0))

# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load('./image/aircraft_image/main_2.png')
screen.blit(hero, (200, 500))

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1，定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 120, 79)


# 游戏循环 -> 游戏的正式开始
# 设置刷新帧率60，检测用户交互，更新所有图像位置，更新屏幕显示

while True:
# 可以指定循环体内部的代码执行频率
    clock.tick(60)
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
# 2，修改飞机的位置
    hero_rect.y -= 1
# 判断飞机位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
# 3，调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
# 4，调用update更新显示
    pygame.display.update()

pygame.quit()
