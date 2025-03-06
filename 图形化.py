import pygame
import copy

pygame.init()              #--------------------------------初始化页面
screen = pygame.display.set_mode((750,750))
pygame.display.set_caption("五子棋")
icon = pygame.image.load("C:/Users/25771/OneDrive/桌面/图片1.jpg")
pygame.display.set_icon(icon)  


Map_set=[0]*15             #--------------------------------数据准备
Map=[]
for i in range(0,15):
    k=copy.copy(Map_set)
    Map.append(k)
test=0


def people(x,y):           #---------------------------------人下棋
    Map[x-1][y-1]=1
    return

def ai():                  #---------------------------------ai下棋（找优解）
    mvp=0 
    value=0
    for i in range(0,15):
        for o in range(0,15):
            if Map[i][o]==0:
                value2=0
                if Test_win(i,o)==2:
                    value2+=1000
                if Test_four(i,o)==2:
                    value2+=80
                if Fence_four(i,o)==2:
                    value2+=90
                if Fence_three(i,o)==2:
                    value2+=50
                if Test_three(i,o)==2:
                    value2+=40
                if value2>value:
                    value=value2
                    mvp=[i,o]
    return mvp

def ai_(x,y):              #----------------------ai下棋（未找出优解）
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

def Test(): #判胜函数（人）
    global test
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
    #----------------------------------获胜处理记得做
    return(test)   

def T_est(): #判胜函数（ai）
    global test
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
    #----------------------------------失败处理记得做
    return(test)   

def Test_win(num1,num2): #判断函数（ai算法用）下完这一手如果ai胜利则返回2，否则返回1
    test=1
    Map[(num1-1)][(num2-1)]=2
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
    Map[(num1-1)][(num2-1)]=0
    return(test)   

def Test_four(num1,num2): #判断函数（ai算法用）下完这一手如果ai有活四则返回2，否则返回1
    test=1
    Map[(num1-1)][(num2-1)]=2
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-1)]==2 and Map[(i+1)][(o-1)]==2 and Map[(i+2)][(o-1)]==2 and Map[(i+3)][(o-1)]!=1:
                test=2
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)][(o-2)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i-1)][(o)]==2 and Map[(i-1)][(o+1)]==2 and Map[(i-1)][(o+2)]==2 and Map[(i-1)][(o+3)]!=1:
                test=2
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)][(o-2)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o)]==2 and Map[(i+1)][(o+1)]==2 and Map[(i+2)][(o+2)]==2 and Map[(i+3)][(o+3)]!=1:
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)][(o)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-2)]==2 and Map[(i+1)][(o-3)]==2 and Map[(i+2)][(o-4)]==2 and Map[(i+3)][(o-5)]!=1:
                test=2
    Map[(num1-1)][(num2-1)]=0
    return(test)   

def Test_three(num1,num2):  #判断函数（ai算法用）下完这一手如果ai有活三则返回2，否则返回1
    test=1
    Map[(num1-1)][(num2-1)]=2
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-1)]==2 and Map[(i+1)][(o-1)]==2 and Map[(i+2)][(o-1)]!=1 :
                test=2
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)][(o-2)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i-1)][(o)]==2 and Map[(i-1)][(o+1)]==2 and Map[(i-1)][(o+2)]!=1:
                test=2
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)][(o-2)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o)]==2 and Map[(i+1)][(o+1)]==2 and Map[(i+2)][(o+2)]!=1 :
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)][(o)]!=1 and Map[(i-1)][(o-1)]==2 and Map[(i)][(o-2)]==2 and Map[(i+1)][(o-3)]==2 and Map[(i+2)][(o-4)]!=1:
                test=2
    Map[(num1-1)][(num2-1)]=0
    return(test)

def Fence_three(num1,num2):   #判断函数（ai算法用）下完这一手如果ai堵住了活三则返回2，否则返回1
    test=1
    Map[(num1-1)][(num2-1)]=2
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]!=2 or Map[(i-2)][(o-1)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]==2 :
                test=2
    for i in range(1,16):
        for o in range(2,13):
            if Map[(i-1)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]!=2 or Map[(i-1)][(o-2)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]==2:
                test=2
    for i in range(2,12):
        for o in range(2,16):
            if Map[(i-2)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]!=2 or Map[(i-2)][(o-2)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]==2:
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)][(o)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]!=2 or Map[(i-2)][(o)]!=2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]==2:
                test=2
    Map[(num1-1)][(num2-1)]=0
    return(test)

def Fence_four(num1,num2):     #判断函数（ai算法用）下完这一手如果ai堵住了半死四则返回2，否则返回1
    test=1
    Map[(num1-1)][(num2-1)]=2
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)][(o-1)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-1)]==1 and Map[(i+1)][(o-1)]==1 and Map[(i+2)][(o-1)]==1 and Map[(i+3)][(o-1)]==2:
                test=2
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i-1)][(o)]==1 and Map[(i-1)][(o+1)]==1 and Map[(i-1)][(o+2)]==1 and Map[(i-1)][(o+3)]==2:
                test=2
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)][(o-2)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o)]==1 and Map[(i+1)][(o+1)]==1 and Map[(i+2)][(o+2)]==1 and Map[(i+3)][(o+3)]!=2:
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)][(o)]==2 and Map[(i-1)][(o-1)]==1 and Map[(i)][(o-2)]==1 and Map[(i+1)][(o-3)]==1 and Map[(i+2)][(o-4)]==1 and Map[(i+3)][(o-5)]!=2:
                test=2
    Map[(num1-1)][(num2-1)]=0
    return(test)   


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            col = round((x-25)/50)
            row = round((y-25)/50)
            

    screen.fill("#CD8500")

    for x in range(15):
        pygame.draw.line(screen,"#000000",[25+50*x,25],[25+50*x,725],2)
    for x in range(15):
        pygame.draw.line(screen,"#000000",[25,25+50*x],[725,25+50*x],2)
    
    pygame.draw.circle(screen,"#000000",[25+50*7,25+50*7],8)
    
    x,y=pygame.mouse.get_pos()
    x=round((x-25)/50)*50+25
    y=round((y-25)/50)*50+25

    pygame.draw.rect(screen,"#FFFFFF",[x-25,y-25,50,50],2)



    if test==0:
        people(round((x-25)/50),round((y-25)/50))
        Test()
        if test==1:
            pass         #--------------------获胜提示
        else:
            kk=ai()
            if kk==0:
                ai_(round((x-25)/50),round((y-25)/50))
            else:
                Map[(kk[0]-1)][(kk[1]-1)]=2
            T_est()
        if test==2:
            pass         #--------------------失败提示

    for i in range(0,15):
        for o in range(0,15):
            if Map[i][o]==1:
                pygame.draw.circle(screen,"#FFFFFF",[25+i*50,25+o*50],23)
            elif Map[i][o]==2:
                pygame.draw.circle(screen,"#000000",[25+i*50,25+o*50],23)


    pygame.display.update()


pygame.quit()
    