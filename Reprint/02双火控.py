import pgzrun
import random
from pgzero.screen import Screen


screen: Screen  # 类型标注

# 设置基本数据
TITLE = 'Fxxk Virus'
WIDTH = 480
HEIGHT = 670
music.play('car_park.mp3')
y1 = 0
y2 = -670
# 创建对象
bg = Actor('bg.png')
plane = Actor('plane.png')
plane.x = bg.width /  2
plane.y = bg.height - plane.height
# 游戏状态
state = False
# 病毒列表
virusList = []
# 子弹列表
bulletList = []
sec_BulletList = []
# score分数
score = 0
# 存活
life = 3
# 武器
double_fire = False
Sscore = 10


def getVirus():
    v = Actor('virus.png')
    v.x = random.randint(0, bg.width)
    v.y = random.randint(0 - bg.height, 0)
    virusList.append(v)


# 子弹数据
def getBullet():

    if double_fire:
        bulletL = Actor('1.png')
        bulletR = Actor('1.png')
        bulletL.x = plane.x - 80
        bulletR.x = plane.x + 80

        bulletL.y = plane.y - 50
        bulletR.y = plane.y - 50
        bulletList.append(bulletL)
        sec_BulletList.append(bulletR)
    else:
        bulletL = Actor('bullet.png')
        bulletL.x = plane.x
        bulletL.y = plane.y - 50
        bulletList.append(bulletL)




# 直接使用检测space事件：触发一次，回调函数执行多次，无法控制子弹数，所以使用抬起事件
def on_key_up(key, mod):  # 这么用也是醉了，幸亏我找到了例子
    if key == keys.SPACE:
        getBullet()


def update():
    if state:  # 暂时没啥用
        exit()
    else:
        if plane.x >= 480:
            plane.x = 480
        if plane.x <= 0:
            plane.x = 0
        if plane.y >= 670:
            plane.y = 670
        if plane.y <= 0:
            plane.y = 0
    # 按键事件
    if keyboard.left:
        plane.x -= 4
    if keyboard.right:
        plane.x += 4
    if keyboard.up:
        plane.y -= 4
    if keyboard.down:
        plane.y += 4

def loseLife():
    global life
    print(99)
    life -= 1

# 检测碰撞
def judge():
    global score, life, double_fire
    for v in virusList:
        v.y += 2  # 病毒移动
        if v.y >= bg.height - v.height:  # 病毒越界
            virusList.remove(v)
        if v.colliderect(plane):  # 病毒飞机碰撞
            print('碰')
            clock.schedule_unique(loseLife, 0.3)#


    for bullet in bulletList:
        bullet.y -= 5  # 子弹移动
        if bullet.y <= 0:  # 子弹越界
            bulletList.remove(bullet)
        for virus in virusList:  # 子弹病毒碰撞
            if virus.colliderect(bullet):
                score += 1
                if score >= Sscore:
                    double_fire = True
                virusList.remove(virus)
                if bullet in bulletList:  # 有可能会空列表执行
                    bulletList.remove(bullet)
    # 双火控子弹逻辑
    for bullet in sec_BulletList:
        bullet.y -= 5  # 子弹移动
        if bullet.y <= 0:  # 子弹越界
            sec_BulletList.remove(bullet)
        for virus in virusList:  # 子弹病毒碰撞
            if virus.colliderect(bullet):
                score += 1
                virusList.remove(virus)
                if bullet in sec_BulletList:  # 有可能会空列表执行
                    sec_BulletList.remove(bullet)


def drwaBg():
    global y1, y2
    y1 += 2
    y2 += 2
    screen.blit('bg.png', (0, y1))
    screen.blit('bg.png', (0, y2))

    if y2 > 670:
        y2 = -670
    if y1 > 670:
        y1 = -670

# 文字显示
def display():
        screen.blit('over.png', (-80, -10))
        screen.draw.text('GameOver', center=[255, 500], fontsize=110, color='red')
    screen.draw.text(str(score), center=[425, 35], fontsize=80, fontname="simkai")
    # life
    screen.draw.text('Life:' + str(life), center=[80, 35], fontsize=40, color='green', fontname="simkai")

    if double_fire:
        screen.draw.text('SuperFire', center=[410, 80], fontsize=30, color='yellow', fontname="simkai")
    if score >= 60:
        screen.draw.text('HighScore', center=[405, 105], fontsize=30, color='orange', fontname="simkai")
    if score >= 100:
        screen.draw.text('Extreme', center=[405, 130], fontsize=40, color='red', fontname="simkai")
    if score >= 150:
        screen.draw.text('Legend', center=[400, 163], fontsize=50, color='gold', fontname="simkai")

# 绘制
def draw():
    global life
    drwaBg()
    judge()
    plane.draw()

    for v in virusList:
        v.draw()

    for b in bulletList:
        b.draw()

    #双火控
    for b in sec_BulletList:
        b.draw()

    if life <= 0:
        life = 0

    display()

clock.schedule_interval(getVirus, 0.1)  # 可以实现自动攻击,参数一没有括号
# clock.schedule_unique(getBullet(), 1.0)#

pgzrun.go()
