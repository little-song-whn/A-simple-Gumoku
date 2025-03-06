import pygame
import copy
from tkinter import Tk, messagebox
state=0

Map_set=[0]*15             #--------------------------------数据准备
Map=[]
for i in range(0,15):
    k=copy.copy(Map_set)
    Map.append(k)

class PopupWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("结束！")
        self.geometry("200x100")

    def show_message(self, message):
        messagebox.showinfo("结束！", message)
        
popup_window = PopupWindow()
popup_window.withdraw()

pygame.init()             
window = pygame.display.set_mode((600,400))             #-----------------图标等一系列操作
pygame.display.set_caption("五子棋")
icon = pygame.image.load("C:/Users/25771/OneDrive/桌面/图片1.jpg")
pygame.display.set_icon(icon)

def Test(): #判胜函数（人）
    global Map
    test=0
    for i in range(1,12):
        for o in range(1,16):
            if Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]==1 and Map[(i+3)][(o-1)]==1:
                test=1
    for i in range(1,16):
        for o in range(1,12):
            if Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]==1 and Map[(i-1)][(o+3)]==1:
                test=1
    for i in range(1,12):
        for o in range(1,12):
            if Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]==1 and Map[(i+3)][(o+3)]==1:
                test=1
    for i in range(1,12):
        for o in range(5,16):
            if Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]==1 and Map[(i+3)][(o-5)]==1:
                test=1
    return(test)   

def T_est(): #判胜函数（ai）
    global Map
    test=0
    for i in range(1,12):
        for o in range(1,16):
            if Map[(i-1)][(o-1)]==2 and Map[(i)][(o-1)]==2 and Map[(i+1)][(o-1)]==2 and Map[(i+2)][(o-1)]==2 and Map[(i+3)][(o-1)]==2:
                test=2
    for i in range(1,16):
        for o in range(1,12):
            if Map[(i-1)][(o-1)]==2 and Map[(i-1)][(o)]==2 and Map[(i-1)][(o+1)]==2 and Map[(i-1)][(o+2)]==2 and Map[(i-1)][(o+3)]==2:
                test=2
    for i in range(1,12):
        for o in range(1,12):
            if Map[(i-1)][(o-1)]==2 and Map[(i)][(o)]==2 and Map[(i+1)][(o+1)]==2 and Map[(i+2)][(o+2)]==2 and Map[(i+3)][(o+3)]==2:
                test=2
    for i in range(1,12):
        for o in range(5,16):
            if Map[(i-1)][(o-1)]==2 and Map[(i)][(o-2)]==2 and Map[(i+1)][(o-3)]==2 and Map[(i+2)][(o-4)]==2 and Map[(i+3)][(o-5)]==2:
                test=2
    return(test)   

def Test_win(num1,num2): #判断函数（ai算法用）下完这一手如果ai胜利则返回至少为2，否则返回1
    global Map
    test=1
    Map[(num1)][(num2)]=2
    for i in range(1,12):
        for o in range(1,16):
            if Map[(i-1)][(o-1)]==2 and Map[(i)][(o-1)]==2 and Map[(i+1)][(o-1)]==2 and Map[(i+2)][(o-1)]==2 and Map[(i+3)][(o-1)]==2 and i-1<=num1<=i+3 and num2==o-1:
                test+=1
    for i in range(1,16):
        for o in range(1,12):
            if Map[(i-1)][(o-1)]==2 and Map[(i-1)][(o)]==2 and Map[(i-1)][(o+1)]==2 and Map[(i-1)][(o+2)]==2 and Map[(i-1)][(o+3)]==2 and num1==i-1 and o-1<=num2<=o+3:
                test+=1
    for i in range(1,12):
        for o in range(1,12):
            if Map[(i-1)][(o-1)]==2 and Map[(i)][(o)]==2 and Map[(i+1)][(o+1)]==2 and Map[(i+2)][(o+2)]==2 and Map[(i+3)][(o+3)]==2 and i-1<=num1<=i+3 and o-1<=num2<=o+3:
                test+=1
    for i in range(1,12):
        for o in range(5,16):
            if Map[(i-1)][(o-1)]==2 and Map[(i)][(o-2)]==2 and Map[(i+1)][(o-3)]==2 and Map[(i+2)][(o-4)]==2 and Map[(i+3)][(o-5)]==2 and i-1<=num1<=i+3 and o-5<=num2<=o-1:
                test+=1
    Map[(num1)][(num2)]=0
    return(test)   

def Test_four(num1,num2): #判断函数（ai算法用）下完这一手如果ai有活四则至少返回2，否则返回1
    global Map
    test=1
    Map[(num1)][(num2)]=2
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-1)]==2 and Map[(i+1)][(o-1)]==2 and Map[(i+2)][(o-1)]==2 and Map[(i+3)][(o-1)]!=1:
                test+=1
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)][(o-2)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i-1)][(o)]==2 and Map[(i-1)][(o+1)]==2 and Map[(i-1)][(o+2)]==2 and Map[(i-1)][(o+3)]!=1:
                test+=1
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)][(o-2)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o)]==2 and Map[(i+1)][(o+1)]==2 and Map[(i+2)][(o+2)]==2 and Map[(i+3)][(o+3)]!=1:
                test+=1
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)][(o)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-2)]==2 and Map[(i+1)][(o-3)]==2 and Map[(i+2)][(o-4)]==2 and Map[(i+3)][(o-5)]!=1:
                test+=1
    Map[(num1)][(num2)]=0
    return(test)   

def Test_three(num1,num2):  #判断函数（ai算法用）下完这一手如果ai有活三则至少返回2，否则返回1
    global Map
    test=1
    Map[(num1)][(num2)]=2
    for i in range(2,13):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]==0 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-1)]==2 and Map[(i+1)][(o-1)]==2 and Map[(i+2)][(o-1)]==0 :
                test+=1
    for i in range(1,16):
        for o in range(2,13):
            if Map[(i-1)][(o-2)]==0 and Map[(i-1)][(o-1)]==2 and Map[(i-1)][(o)]==2 and Map[(i-1)][(o+1)]==2 and Map[(i-1)][(o+2)]==0:
                test+=1
    for i in range(2,13):
        for o in range(2,13):
            if Map[(i-2)][(o-2)]==0 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o)]==2 and Map[(i+1)][(o+1)]==2 and Map[(i+2)][(o+2)]==0 :
                test+=1
    for i in range(2,13):
        for o in range(5,15):
            if Map[(i-2)][(o)]==0 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-2)]==2 and Map[(i+1)][(o-3)]==2 and Map[(i+2)][(o-4)]==0:
                test+=1
    Map[(num1)][(num2)]=0
    return(test)

def Fence_three(num1,num2):   #判断函数（ai算法用）下完这一手如果ai堵住了活三则至少返回2，否则返回1
    global Map
    test=1
    Map[(num1)][(num2)]=2
    for i in range(2,13):
        for o in range(1,16):
            if ((Map[(i-2)][(o-1)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]!=2) or (Map[(i-2)][(o-1)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]==2)) and (i-2<=num1<=i+2 and o-1==num2) :
                test+=1
    for i in range(1,16):
        for o in range(2,13):
            if ((Map[(i-1)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]!=2) or (Map[(i-1)][(o-2)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]==2)) and (i-1==num1 and o-2<=num2<=o+2):
                test+=1
    for i in range(2,13):
        for o in range(2,13):
            if ((Map[(i-2)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]!=2) or (Map[(i-2)][(o-2)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]==2)) and (i-2==o-2<=num1==num2<=i+2==o+2):
                test+=1
    for i in range(2,13):
        for o in range(4,15):
            if ((Map[(i-2)][(o)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]!=2) or (Map[(i-2)][(o)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]==2)) and (i+o-2==num1+num2 and i-2<=num1<=i+2 and o-4<=num2<=o):
                test+=1
    Map[(num1)][(num2)]=0
    return(test)

def Fence_four(num1,num2):     #判断函数（ai算法用）下完这一手如果ai堵住了半死四则至少返回2，否则返回1
    global Map
    test=1
    Map[(num1)][(num2)]=2
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]==1 and Map[(i+3)][(o-1)]==2 and i-2<=num1<=i+3 and o-1==num2:
                test+=1
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]==1 and Map[(i-1)][(o+3)]==2 and i-1==num1 and o-2<=num2<=o+3:
                test+=1
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]==1 and Map[(i+3)][(o+3)]==2 and o-2==i-2<=num1==num2<=o+3==i+3:
                test+=1
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)][(o)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]==1 and Map[(i+3)][(o-5)]==2 and i-2<=num1<=i+3 and o-5<=num2<=o and i+o-2==num1+num2:
                test+=1
    Map[(num1)][(num2)]=1
    if Test()==1:
        test+=2
    Map[(num1)][(num2)]=0
    return(test)   

def ai():                  #---------------------------------ai下棋（找优解）
    global Map
    mvp=0 
    value=0
    for i in range(0,15):
        for o in range(0,15):
            if Map[i][o] == 0:
                value2=0
                a1=Test_win(i,o)
                a2=Test_four(i,o)
                a3=Fence_four(i,o)
                a4=Fence_three(i,o)
                a5=Test_three(i,o)
                if a1>=2:
                    value2+=1000*a1
                if a2>=2:
                    value2+=80*a2
                if a3>=2:
                    value2+=90*a3
                if a4>=2:
                    value2+=50*a4
                if a5>=2:
                    value2+=40*a5
                if value2>value:
                    value=value2
                    mvp=[i,o]
    return mvp

def ai_(x,y):              #----------------------ai下棋（未找出优解）
    global Map
    x+=1
    y+=1
    if x!=1 and x!=15 and y!=1 and y!=15: #中间部分
        if Map[(x) ][(y-1) ]!=1 and Map[(x) ][(y-1) ]!=2:#下
            Map[(x) ][(y-1) ]=2
        elif Map[(x-1) ][(y) ]!=1 and Map[(x-1) ][(y) ]!=2:#右
            Map[(x-1) ][(y) ]=2
        elif Map[(x) ][(y) ]!=1 and Map[(x) ][(y) ]!=2:#右下
            Map[(x) ][(y) ]=2
        elif Map[(x-2) ][(y-1) ]!=1 and Map[(x-2) ][(y-1) ]!=2:#上
            Map[(x-2) ][(y-1) ]=2
        elif Map[(x-1) ][(y-2) ]!=1 and Map[(x-1) ][(y-2) ]!=2:#左
            Map[(x-1) ][(y-2) ]=2
        elif Map[(x-2) ][(y-2) ]!=1 and Map[(x-2) ][(y-2) ]!=2:#左上
            Map[(x-2) ][(y-2) ]=2
        elif Map[(x) ][(y-2) ]!=1 and Map[(x) ][(y-2) ]!=2:#左下
            Map[(x) ][(y-2) ]=2
        elif Map[(x-2) ][(y) ]!=1 and Map[(x-2) ][(y) ]!=2:#右上
            Map[(x-2) ][(y) ]=2
    elif x==1 and y!=1 and y!=15:        #上排
        if Map[(x) ][(y-1) ]!=1 and Map[(x) ][(y-1) ]!=2:#下
            Map[(x) ][(y-1) ]=2
        elif Map[(x) ][(y-2) ]!=1 and Map[(x) ][(y-2) ]!=2:#左下
            Map[(x) ][(y-2) ]=2
        elif Map[(x-1) ][(y) ]!=1 and Map[(x-1) ][(y) ]!=2:#右
            Map[(x-1) ][(y) ]=2
        elif Map[(x) ][(y) ]!=1 and Map[(x) ][(y) ]!=2:#右下
            Map[(x) ][(y) ]=2
        elif Map[(x-1) ][(y-2) ]!=1 and Map[(x-1) ][(y-2) ]!=2:#左
            Map[(x-1) ][(y-2) ]=2
    elif x==15 and y!=1 and y!=15:         #下排
        if Map[(x-2) ][(y-1) ]!=1 and Map[(x-2) ][(y-1) ]!=2:#上
            Map[(x-2) ][(y-1) ]=2
        elif Map[(x-1) ][(y) ]!=1 and Map[(x-1) ][(y) ]!=2:#右
            Map[(x-1) ][(y) ]=2
        elif Map[(x-2) ][(y-2) ]!=1 and Map[(x-2) ][(y-2) ]!=2:#左上
            Map[(x-2) ][(y-2) ]=2
        elif Map[(x-2) ][(y) ]!=1 and Map[(x-2) ][(y) ]!=2:#右上
            Map[(x-2) ][(y) ]=2
        elif Map[(x-1) ][(y-2) ]!=1 and Map[(x-1) ][(y-2) ]!=2:#左
            Map[(x-1) ][(y-2) ]=2
    elif y==1 and x!=1 and x!=15:          #左排
        if Map[(x) ][(y-1) ]!=1 and Map[(x) ][(y-1) ]!=2:#下
            Map[(x) ][(y-1) ]=2
        elif Map[(x-1) ][(y) ]!=1 and Map[(x-1) ][(y) ]!=2:#右
            Map[(x-1) ][(y) ]=2
        elif Map[(x-2) ][(y) ]!=1 and Map[(x-2) ][(y) ]!=2:#右上
            Map[(x-2) ][(y) ]=2
        elif Map[(x) ][(y) ]!=1 and Map[(x) ][(y) ]!=2:#右下
            Map[(x) ][(y) ]=2
        elif Map[(x-2) ][(y-1) ]!=1 and Map[(x-2) ][(y-1) ]!=2:#上
            Map[(x-2) ][(y-1) ]=2
    elif y==15 and x!=1 and x!=15:         #右排
        if Map[(x-2) ][(y-1) ]!=1 and Map[(x-2) ][(y-1) ]!=2:#上
            Map[(x-2) ][(y-1) ]=2
        elif Map[(x) ][(y-1) ]!=1 and Map[(x) ][(y-1) ]!=2:#下
            Map[(x) ][(y-1) ]=2
        elif Map[(x-1) ][(y-2) ]!=1 and Map[(x-1) ][(y-2) ]!=2:#左
            Map[(x-1) ][(y-2) ]=2
        elif Map[(x-2) ][(y-2) ]!=1 and Map[(x-2) ][(y-2) ]!=2:#左上
            Map[(x-2) ][(y-2) ]=2
        elif Map[(x) ][(y-2) ]!=1 and Map[(x) ][(y-2) ]!=2:#左下
            Map[(x) ][(y-2) ]=2
    elif x==1 and y==1:
        if Map[(x) ][(y-1) ]!=1 and Map[(x) ][(y-1) ]!=2:#下
            Map[(x) ][(y-1) ]=2
        elif Map[(x-1) ][(y) ]!=1 and Map[(x-1) ][(y) ]!=2:#右
            Map[(x-1) ][(y) ]=2
        elif Map[(x) ][(y) ]!=1 and Map[(x) ][(y) ]!=2:#右下
            Map[(x) ][(y) ]=2
    elif x==1 and y==15:
        if Map[(x) ][(y-1) ]!=1 and Map[(x) ][(y-1) ]!=2:#下
            Map[(x) ][(y-1) ]=2
        elif Map[(x-1) ][(y-2) ]!=1 and Map[(x-1) ][(y-2) ]!=2:#左
            Map[(x-1) ][(y-2) ]=2
        elif Map[(x) ][(y-2) ]!=1 and Map[(x) ][(y-2) ]!=2:#左下
            Map[(x) ][(y-2) ]=2
    elif x==15 and y==1:
        if Map[(x-2) ][(y-1) ]!=1 and Map[(x-2) ][(y-1) ]!=2:#上
            Map[(x-2) ][(y-1) ]=2
        elif Map[(x-1) ][(y) ]!=1 and Map[(x-1) ][(y) ]!=2:#右
            Map[(x-1) ][(y) ]=2
        elif Map[(x-2) ][(y) ]!=1 and Map[(x-2) ][(y) ]!=2:#右上
            Map[(x-2) ][(y) ]=2
    elif x==15 and y==15:
        if Map[(x-2) ][(y-1) ]!=1 and Map[(x-2) ][(y-1) ]!=2:#上
            Map[(x-2) ][(y-1) ]=2
        elif Map[(x-1) ][(y-2) ]!=1 and Map[(x-1) ][(y-2) ]!=2:#左
            Map[(x-1) ][(y-2) ]=2
        elif Map[(x-2) ][(y-2) ]!=1 and Map[(x-2) ][(y-2) ]!=2:#左上
            Map[(x-2) ][(y-2) ]=2
    return()

img = pygame.image.load("C:/Users/25771/OneDrive/桌面/picture1.jpg")  
img = pygame.transform.scale(img, (600, 400))
window.blit(img, (0, 0))
pygame.display.update() 
flag = True
while flag:                 #----------------------初始页面
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if 50<=x<=250 and 250<=y<=350:
                state = 1
                flag = False
            elif 350<=x<=550 and 250<=y<=350:
                state = 2
                flag = False
    font = pygame.font.Font("C:/Users/25771/OneDrive/桌面/STXINGKA.TTF",50)
    pygame.draw.rect(window,"#ADD8E6",[50,250,200,100])
    text = font.render('人机对战', True,'#000000')
    window.blit(text, (50, 275))
    pygame.draw.rect(window,"#E0EEE0",[350,250,200,100])
    text = font.render('双人对战', True,'#000000')
    window.blit(text, (350, 275))
    pygame.display.update()

if state != 0:                #--------------------人机对战与人人对战
    screen = pygame.display.set_mode((750,750))
    pygame.display.set_caption("五子棋")
    icon = pygame.image.load("C:/Users/25771/OneDrive/桌面/图片1.jpg")
    pygame.display.set_icon(icon)  
    if state ==1:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    col = round((x-25)/50)
                    row = round((y-25)/50)
                    if Map[col][row] == 0:
                        Map[col][row] = 1
                        if Test()==1:
                            popup_window.show_message("你赢了！")
                            pygame.time.wait(1000)
                            running = False
                            break
                        ans=ai()
                        if ans==0:
                            ai_(col,row)
                        else:
                            Map[(ans[0])][(ans[1])] = 2
                        if T_est()==2:
                            popup_window.show_message("你输了！")
                            pygame.time.wait(1000)
                            running = False
            
            #screen.fill("#CD8500")
            img = pygame.image.load("C:/Users/25771/OneDrive/桌面/picture2.jpg")  
            img = pygame.transform.scale(img, (750, 750))
            window.blit(img, (0, 0))

            for x in range(15):
                pygame.draw.line(screen,"#000000",[25+50*x,25],[25+50*x,725],2)
            for x in range(15):
                pygame.draw.line(screen,"#000000",[25,25+50*x],[725,25+50*x],2)
            
            pygame.draw.circle(screen,"#000000",[25+50*7,25+50*7],8)
            for i in range(0,15):
                for o in range(0,15):
                    if Map[i][o]==1:
                        pygame.draw.circle(screen,"#000000",[i*50+25,o*50+25],20)
                    elif Map[i][o]==2:
                        pygame.draw.circle(screen,"#FFFFFF",[i*50+25,o*50+25],20)
                

            x,y=pygame.mouse.get_pos()
            x=round((x-25)/50)*50+25
            y=round((y-25)/50)*50+25

            pygame.draw.rect(screen,"#FFFFFF",[x-25,y-25,50,50],2)
            pygame.draw.circle(screen,"#000000",[x,y],20)

            
            pygame.display.update()
    elif state == 2:
        running = True
        recent_player = 1
        latter_player = 2
        recent_color = "#000000"
        latter_color = "#FFFFFF"
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    col = round((x-25)/50)
                    row = round((y-25)/50)
                    if Map[col][row] == 0:
                        Map[col][row] = recent_player
                        recent_player,latter_player = latter_player,recent_player
                        recent_color,latter_color = latter_color,recent_color
                        if Test()==1:
                            popup_window.show_message("黑棋赢了！")
                            pygame.time.wait(1000)
                            running = False
                            break
                        if T_est()==2:
                            popup_window.show_message("白棋赢了！")
                            pygame.time.wait(1000)
                            running = False
            
            #screen.fill("#CD8500")
            img = pygame.image.load("C:/Users/25771/OneDrive/桌面/picture2.jpg")  
            img = pygame.transform.scale(img, (750, 750))
            window.blit(img, (0, 0))

            for x in range(15):
                pygame.draw.line(screen,"#000000",[25+50*x,25],[25+50*x,725],2)
            for x in range(15):
                pygame.draw.line(screen,"#000000",[25,25+50*x],[725,25+50*x],2)
            
            pygame.draw.circle(screen,"#000000",[25+50*7,25+50*7],8)
            for i in range(0,15):
                for o in range(0,15):
                    if Map[i][o]==1:
                        pygame.draw.circle(screen,"#000000",[i*50+25,o*50+25],20)
                    elif Map[i][o]==2:
                        pygame.draw.circle(screen,"#FFFFFF",[i*50+25,o*50+25],20)
    

            x,y=pygame.mouse.get_pos()
            x=round((x-25)/50)*50+25
            y=round((y-25)/50)*50+25

            pygame.draw.rect(screen,latter_color,[x-25,y-25,50,50],2)
            pygame.draw.circle(screen,recent_color,[x,y],20)

            pygame.display.update()
    
pygame.quit()