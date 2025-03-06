import copy
Map=[[' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ' ]]
map1=['|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|','  ','|' ]
map2=[' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ','--',' ' ]
test=0
mark=0
m_ark=0
markpoint=[1,1]

for i in range(0,14):
    k=copy.copy(map1)
    Map.append(k)
    l=copy.copy(map2)
    Map.append(l)

for i in range(0,29):
    print(''.join(Map[i]))

def people(x,y): #人下棋
    Map[(x-1)*2][(y-1)*2]='0'
    return

def ai_(x,y):   #ai下棋（未找出优解）
    if x!=1 and x!=15 and y!=1 and y!=15: #中间部分
        if Map[(x)*2][(y-1)*2]!='0'and Map[(x)*2][(y-1)*2]!='&':#下
            Map[(x)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y)*2]!='0'and Map[(x-1)*2][(y)*2]!='&':#右
            Map[(x-1)*2][(y)*2]='&'
        elif Map[(x)*2][(y)*2]!='0'and Map[(x)*2][(y)*2]!='&':#右下
            Map[(x)*2][(y)*2]='&'
        elif Map[(x-2)*2][(y-1)*2]!='0'and Map[(x-2)*2][(y-1)*2]!='&':#上
            Map[(x-2)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y-2)*2]!='0'and Map[(x-1)*2][(y-2)*2]!='&':#左
            Map[(x-1)*2][(y-2)*2]='&'
        elif Map[(x-2)*2][(y-2)*2]!='0'and Map[(x-2)*2][(y-2)*2]!='&':#左上
            Map[(x-2)*2][(y-2)*2]='&'
        elif Map[(x)*2][(y-2)*2]!='0'and Map[(x)*2][(y-2)*2]!='&':#左下
            Map[(x)*2][(y-2)*2]='&'
        elif Map[(x-2)*2][(y)*2]!='0'and Map[(x-2)*2][(y)*2]!='&':#右上
            Map[(x-2)*2][(y)*2]='&'
    elif x==1 and y!=1 and y!=15:        #上排
        if Map[(x)*2][(y-1)*2]!='0'and Map[(x)*2][(y-1)*2]!='&':#下
            Map[(x)*2][(y-1)*2]='&'
        elif Map[(x)*2][(y-2)*2]!='0'and Map[(x)*2][(y-2)*2]!='&':#左下
            Map[(x)*2][(y-2)*2]='&'
        elif Map[(x-1)*2][(y)*2]!='0'and Map[(x-1)*2][(y)*2]!='&':#右
            Map[(x-1)*2][(y)*2]='&'
        elif Map[(x)*2][(y)*2]!='0'and Map[(x)*2][(y)*2]!='&':#右下
            Map[(x)*2][(y)*2]='&'
        elif Map[(x-1)*2][(y-2)*2]!='0'and Map[(x-1)*2][(y-2)*2]!='&':#左
            Map[(x-1)*2][(y-2)*2]='&'
    elif x==15 and y!=1 and y!=15:         #下排
        if Map[(x-2)*2][(y-1)*2]!='0'and Map[(x-2)*2][(y-1)*2]!='&':#上
            Map[(x-2)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y)*2]!='0'and Map[(x-1)*2][(y)*2]!='&':#右
            Map[(x-1)*2][(y)*2]='&'
        elif Map[(x-2)*2][(y-2)*2]!='0'and Map[(x-2)*2][(y-2)*2]!='&':#左上
            Map[(x-2)*2][(y-2)*2]='&'
        elif Map[(x-2)*2][(y)*2]!='0'and Map[(x-2)*2][(y)*2]!='&':#右上
            Map[(x-2)*2][(y)*2]='&'
        elif Map[(x-1)*2][(y-2)*2]!='0'and Map[(x-1)*2][(y-2)*2]!='&':#左
            Map[(x-1)*2][(y-2)*2]='&'
    elif y==1 and x!=1 and x!=15:          #左排
        if Map[(x)*2][(y-1)*2]!='0'and Map[(x)*2][(y-1)*2]!='&':#下
            Map[(x)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y)*2]!='0'and Map[(x-1)*2][(y)*2]!='&':#右
            Map[(x-1)*2][(y)*2]='&'
        elif Map[(x-2)*2][(y)*2]!='0'and Map[(x-2)*2][(y)*2]!='&':#右上
            Map[(x-2)*2][(y)*2]='&'
        elif Map[(x)*2][(y)*2]!='0'and Map[(x)*2][(y)*2]!='&':#右下
            Map[(x)*2][(y)*2]='&'
        elif Map[(x-2)*2][(y-1)*2]!='0'and Map[(x-2)*2][(y-1)*2]!='&':#上
            Map[(x-2)*2][(y-1)*2]='&'
    elif y==15 and x!=1 and x!=15:         #右排
        if Map[(x-2)*2][(y-1)*2]!='0'and Map[(x-2)*2][(y-1)*2]!='&':#上
            Map[(x-2)*2][(y-1)*2]='&'
        elif Map[(x)*2][(y-1)*2]!='0'and Map[(x)*2][(y-1)*2]!='&':#下
            Map[(x)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y-2)*2]!='0'and Map[(x-1)*2][(y-2)*2]!='&':#左
            Map[(x-1)*2][(y-2)*2]='&'
        elif Map[(x-2)*2][(y-2)*2]!='0'and Map[(x-2)*2][(y-2)*2]!='&':#左上
            Map[(x-2)*2][(y-2)*2]='&'
        elif Map[(x)*2][(y-2)*2]!='0'and Map[(x)*2][(y-2)*2]!='&':#左下
            Map[(x)*2][(y-2)*2]='&'
    elif x==1 and y==1:
        if Map[(x)*2][(y-1)*2]!='0'and Map[(x)*2][(y-1)*2]!='&':#下
            Map[(x)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y)*2]!='0'and Map[(x-1)*2][(y)*2]!='&':#右
            Map[(x-1)*2][(y)*2]='&'
        elif Map[(x)*2][(y)*2]!='0'and Map[(x)*2][(y)*2]!='&':#右下
            Map[(x)*2][(y)*2]='&'
    elif x==1 and y==15:
        if Map[(x)*2][(y-1)*2]!='0'and Map[(x)*2][(y-1)*2]!='&':#下
            Map[(x)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y-2)*2]!='0'and Map[(x-1)*2][(y-2)*2]!='&':#左
            Map[(x-1)*2][(y-2)*2]='&'
        elif Map[(x)*2][(y-2)*2]!='0'and Map[(x)*2][(y-2)*2]!='&':#左下
            Map[(x)*2][(y-2)*2]='&'
    elif x==15 and y==1:
        if Map[(x-2)*2][(y-1)*2]!='0'and Map[(x-2)*2][(y-1)*2]!='&':#上
            Map[(x-2)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y)*2]!='0'and Map[(x-1)*2][(y)*2]!='&':#右
            Map[(x-1)*2][(y)*2]='&'
        elif Map[(x-2)*2][(y)*2]!='0'and Map[(x-2)*2][(y)*2]!='&':#右上
            Map[(x-2)*2][(y)*2]='&'
    elif x==15 and y==15:
        if Map[(x-2)*2][(y-1)*2]!='0'and Map[(x-2)*2][(y-1)*2]!='&':#上
            Map[(x-2)*2][(y-1)*2]='&'
        elif Map[(x-1)*2][(y-2)*2]!='0'and Map[(x-1)*2][(y-2)*2]!='&':#左
            Map[(x-1)*2][(y-2)*2]='&'
        elif Map[(x-2)*2][(y-2)*2]!='0'and Map[(x-2)*2][(y-2)*2]!='&':#左上
            Map[(x-2)*2][(y-2)*2]='&'
    for i in range(0,29):
        print(''.join(Map[i]))
    return()

def ai():       #ai下棋（找优解）
    mvp=0
    value=0
    for i in range(1,16):
        for o in range(1,16):
            if Map[(i-1)*2][(o-1)*2]==' ':
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

def Test(): #判胜函数（人）
    global test
    for i in range(1,12):
        for o in range(1,16):
            if Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-1)*2]=='0' and Map[(i+1)*2][(o-1)*2]=='0' and Map[(i+2)*2][(o-1)*2]=='0' and Map[(i+3)*2][(o-1)*2]=='0':
                test=1
    for i in range(1,16):
        for o in range(1,12):
            if Map[(i-1)*2][(o-1)*2]=='0' and Map[(i-1)*2][(o)*2]=='0' and Map[(i-1)*2][(o+1)*2]=='0' and Map[(i-1)*2][(o+2)*2]=='0' and Map[(i-1)*2][(o+3)*2]=='0':
                test=1
    for i in range(1,12):
        for o in range(1,12):
            if Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o)*2]=='0' and Map[(i+1)*2][(o+1)*2]=='0' and Map[(i+2)*2][(o+2)*2]=='0' and Map[(i+3)*2][(o+3)*2]=='0':
                test=1
    for i in range(1,12):
        for o in range(5,16):
            if Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-2)*2]=='0' and Map[(i+1)*2][(o-3)*2]=='0' and Map[(i+2)*2][(o-4)*2]=='0' and Map[(i+3)*2][(o-5)*2]=='0':
                test=1
    if test==1:
        print('you are win')
    return(test)   

def T_est(): #判胜函数（ai）
    global test
    for i in range(1,12):
        for o in range(1,16):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-1)*2]=='&' and Map[(i+1)*2][(o-1)*2]=='&' and Map[(i+2)*2][(o-1)*2]=='&' and Map[(i+3)*2][(o-1)*2]=='&':
                test=2
    for i in range(1,16):
        for o in range(1,12):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i-1)*2][(o)*2]=='&' and Map[(i-1)*2][(o+1)*2]=='&' and Map[(i-1)*2][(o+2)*2]=='&' and Map[(i-1)*2][(o+3)*2]=='&':
                test=2
    for i in range(1,12):
        for o in range(1,12):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o)*2]=='&' and Map[(i+1)*2][(o+1)*2]=='&' and Map[(i+2)*2][(o+2)*2]=='&' and Map[(i+3)*2][(o+3)*2]=='&':
                test=2
    for i in range(1,12):
        for o in range(5,16):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-2)*2]=='&' and Map[(i+1)*2][(o-3)*2]=='&' and Map[(i+2)*2][(o-4)*2]=='&' and Map[(i+3)*2][(o-5)*2]=='&':
                test=2
    if test==2:
        print('you are defeated')
    return(test)   

def Test_win(num1,num2): #判断函数（ai算法用）下完这一手如果ai胜利则返回2，否则返回1
    test=1
    Map[(num1-1)*2][(num2-1)*2]='&'
    for i in range(1,12):
        for o in range(1,16):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-1)*2]=='&' and Map[(i+1)*2][(o-1)*2]=='&' and Map[(i+2)*2][(o-1)*2]=='&' and Map[(i+3)*2][(o-1)*2]=='&':
                test=2
    for i in range(1,16):
        for o in range(1,12):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i-1)*2][(o)*2]=='&' and Map[(i-1)*2][(o+1)*2]=='&' and Map[(i-1)*2][(o+2)*2]=='&' and Map[(i-1)*2][(o+3)*2]=='&':
                test=2
    for i in range(1,12):
        for o in range(1,12):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o)*2]=='&' and Map[(i+1)*2][(o+1)*2]=='&' and Map[(i+2)*2][(o+2)*2]=='&' and Map[(i+3)*2][(o+3)*2]=='&':
                test=2
    for i in range(1,12):
        for o in range(5,16):
            if Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-2)*2]=='&' and Map[(i+1)*2][(o-3)*2]=='&' and Map[(i+2)*2][(o-4)*2]=='&' and Map[(i+3)*2][(o-5)*2]=='&':
                test=2
    Map[(num1-1)*2][(num2-1)*2]=' '
    return(test)   

def Test_four(num1,num2): #判断函数（ai算法用）下完这一手如果ai有活四则返回2，否则返回1
    test=1
    Map[(num1-1)*2][(num2-1)*2]='&'
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)*2][(o-1)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-1)*2]=='&' and Map[(i+1)*2][(o-1)*2]=='&' and Map[(i+2)*2][(o-1)*2]=='&' and Map[(i+3)*2][(o-1)*2]!='0':
                test=2
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)*2][(o-2)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i-1)*2][(o)*2]=='&' and Map[(i-1)*2][(o+1)*2]=='&' and Map[(i-1)*2][(o+2)*2]=='&' and Map[(i-1)*2][(o+3)*2]!='0':
                test=2
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)*2][(o-2)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o)*2]=='&' and Map[(i+1)*2][(o+1)*2]=='&' and Map[(i+2)*2][(o+2)*2]=='&' and Map[(i+3)*2][(o+3)*2]!='0':
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)*2][(o)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-2)*2]=='&' and Map[(i+1)*2][(o-3)*2]=='&' and Map[(i+2)*2][(o-4)*2]=='&' and Map[(i+3)*2][(o-5)*2]!='0':
                test=2
    Map[(num1-1)*2][(num2-1)*2]=' '
    return(test)   

def Test_three(num1,num2):  #判断函数（ai算法用）下完这一手如果ai有活三则返回2，否则返回1
    test=1
    Map[(num1-1)*2][(num2-1)*2]='&'
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)*2][(o-1)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-1)*2]=='&' and Map[(i+1)*2][(o-1)*2]=='&' and Map[(i+2)*2][(o-1)*2]!='0' :
                test=2
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)*2][(o-2)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i-1)*2][(o)*2]=='&' and Map[(i-1)*2][(o+1)*2]=='&' and Map[(i-1)*2][(o+2)*2]!='0':
                test=2
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)*2][(o-2)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o)*2]=='&' and Map[(i+1)*2][(o+1)*2]=='&' and Map[(i+2)*2][(o+2)*2]!='0' :
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)*2][(o)*2]!='0' and Map[(i-1)*2][(o-1)*2]=='&' and Map[(i)*2][(o-2)*2]=='&' and Map[(i+1)*2][(o-3)*2]=='&' and Map[(i+2)*2][(o-4)*2]!='0':
                test=2
    Map[(num1-1)*2][(num2-1)*2]=' '
    return(test)

def Fence_three(num1,num2):   #判断函数（ai算法用）下完这一手如果ai堵住了活三则返回2，否则返回1
    test=1
    Map[(num1-1)*2][(num2-1)*2]='&'
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)*2][(o-1)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-1)*2]=='0' and Map[(i+1)*2][(o-1)*2]=='0' and Map[(i+2)*2][(o-1)*2]!='&' or Map[(i-2)*2][(o-1)*2]!='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-1)*2]=='0' and Map[(i+1)*2][(o-1)*2]=='0' and Map[(i+2)*2][(o-1)*2]=='&' :
                test=2
    for i in range(1,16):
        for o in range(2,13):
            if Map[(i-1)*2][(o-2)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i-1)*2][(o)*2]=='0' and Map[(i-1)*2][(o+1)*2]=='0' and Map[(i-1)*2][(o+2)*2]!='&' or Map[(i-1)*2][(o-2)*2]!='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i-1)*2][(o)*2]=='0' and Map[(i-1)*2][(o+1)*2]=='0' and Map[(i-1)*2][(o+2)*2]=='&':
                test=2
    for i in range(2,12):
        for o in range(2,16):
            if Map[(i-2)*2][(o-2)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o)*2]=='0' and Map[(i+1)*2][(o+1)*2]=='0' and Map[(i+2)*2][(o+2)*2]!='&' or Map[(i-2)*2][(o-2)*2]!='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o)*2]=='0' and Map[(i+1)*2][(o+1)*2]=='0' and Map[(i+2)*2][(o+2)*2]=='&':
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)*2][(o)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-2)*2]=='0' and Map[(i+1)*2][(o-3)*2]=='0' and Map[(i+2)*2][(o-4)*2]!='&' or Map[(i-2)*2][(o)*2]!='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-2)*2]=='0' and Map[(i+1)*2][(o-3)*2]=='0' and Map[(i+2)*2][(o-4)*2]=='&':
                test=2
    Map[(num1-1)*2][(num2-1)*2]=' '
    return(test)

def Fence_four(num1,num2):     #判断函数（ai算法用）下完这一手如果ai堵住了半死四则返回2，否则返回1
    test=1
    Map[(num1-1)*2][(num2-1)*2]='&'
    for i in range(2,12):
        for o in range(1,16):
            if Map[(i-2)*2][(o-1)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-1)*2]=='0' and Map[(i+1)*2][(o-1)*2]=='0' and Map[(i+2)*2][(o-1)*2]=='0' and Map[(i+3)*2][(o-1)*2]=='&':
                test=2
    for i in range(1,16):
        for o in range(2,12):
            if Map[(i-1)*2][(o-2)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i-1)*2][(o)*2]=='0' and Map[(i-1)*2][(o+1)*2]=='0' and Map[(i-1)*2][(o+2)*2]=='0' and Map[(i-1)*2][(o+3)*2]=='&':
                test=2
    for i in range(2,12):
        for o in range(2,12):
            if Map[(i-2)*2][(o-2)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o)*2]=='0' and Map[(i+1)*2][(o+1)*2]=='0' and Map[(i+2)*2][(o+2)*2]=='0' and Map[(i+3)*2][(o+3)*2]!='&':
                test=2
    for i in range(2,12):
        for o in range(5,15):
            if Map[(i-2)*2][(o)*2]=='&' and Map[(i-1)*2][(o-1)*2]=='0' and Map[(i)*2][(o-2)*2]=='0' and Map[(i+1)*2][(o-3)*2]=='0' and Map[(i+2)*2][(o-4)*2]=='0' and Map[(i+3)*2][(o-5)*2]!='&':
                test=2
    Map[(num1-1)*2][(num2-1)*2]=' '
    return(test)   

while True:    
    a,b = map(int,input().split())
    people(a,b)
    Test()
    if test==1:
        for i in range(0,29):
            print(''.join(Map[i]))
        break
    else:
        kk=ai()
        print(kk)
        if kk==0:
            ai_(a,b)
        else:
            Map[(kk[0]-1)*2][(kk[1]-1)*2]='&'
            for i in range(0,29):
                print(''.join(Map[i]))
        T_est()
    if test==2:
        for i in range(0,29):
            print(''.join(Map[i]))
        break
    else :
        print('go on!')