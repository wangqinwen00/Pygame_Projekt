import pygame


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的方法
        #如果父类有意义的初始化操作需要被继承或扩展，那么通常建议在子类的构造方法中调用 super().__init__() 以确保这些操作被执行。但在一些情况下，根据具体需求，可以选择不调用 super().__init__()。根据课程，由于Sprite在sprite里面，要super一下，pycharm也有提示

        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

        #重写父类update方法
    def update(self):
        # 垂直方向移动
        self.rect.y += self.speed
        pass
