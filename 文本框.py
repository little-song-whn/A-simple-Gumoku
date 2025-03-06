import pygame
from pygame.locals import *
from tkinter import Tk, messagebox

class PopupWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("结束！")
        self.geometry("200x100")

    def show_message(self, message):
        messagebox.showinfo("结束！", message)
        
popup_window = PopupWindow()
popup_window.withdraw()

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
# 设置文本框字体和大小
font = pygame.font.Font(None, 32)

# 设置文本框位置和尺寸
input_box = pygame.Rect(100, 100, 140, 32)

# 设置文本输入框的颜色
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('gray15')
color = color_inactive

# 设置文本内容
text = ''
line = 0
# 游戏主循环
running = True
while running:
    screen.fill("#FFF111")

    # 获取所有的事件
    for event in pygame.event.get():
        # 判断事件类型是否为QUIT
        if event.type == QUIT:
            running = False

        # 判断事件类型是否为KEYDOWN
        elif event.type == KEYDOWN:
            # 如果按下的是回车键
            if event.key == K_RETURN:
                # 打印并清空玩家输入的文本
                line = int(text)
                if line>15 or line<5:
                    popup_window.show_message("棋盘大小应大于5且小于15")
                    continue
                print(text)
                text = ''

            # 如果按下的是退格键
            elif event.key == K_BACKSPACE:
                # 删除最后一个字符
                text = text[:-1]

            else:
                # 将玩家输入的字符添加到文本中
                text += event.unicode

    # 设置文本输入框的外观
    pygame.draw.rect(screen, color, input_box, 2)

    # 绘制文本
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # 更新屏幕
    pygame.display.flip()