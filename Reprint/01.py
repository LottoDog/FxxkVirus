import pgzrun
import random


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
plane.x = bg.width / 2
plane.y = bg.height - plane.height
# 游戏状态
state = False
# 病毒列表
virusList = []
# 子弹列表
bulletList = []
# score分数
score = 0
# 存活
alive = True


def getVirus():
    v = Actor('virus.png')
    v.x = random.randint(0, bg.width)
    v.y = random.randint(0 - bg.height, 0)
    virusList.append(v)

    print('产生一个病毒' * 5)


# 子弹数据
def getBullet():
    bullet = Actor('bullet.png')
    bullet.x = plane.x
    bullet.y = plane.y - 50
    bulletList.append(bullet)

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


# 检测碰撞
def judge():
    global score, alive
    for v in virusList:
        v.y += 2  # 病毒移动
        if v.y >= bg.height - v.height:  # 病毒越界
            virusList.remove(v)
        if v.colliderect(plane):  # 病毒飞机碰撞
            alive = False

    for bullet in bulletList:
        bullet.y -= 5  # 子弹移动
        if bullet.y <= 0:  # 子弹越界
            bulletList.remove(bullet)
        for virus in virusList:  # 子弹病毒碰撞
            if virus.colliderect(bullet):
                print("collide 击中目标" * 5)
                score += 1
                virusList.remove(virus)
                if bullet in bulletList:  # 有可能会空列表执行
                    bulletList.remove(bullet)

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
# 绘制
def draw():
    drwaBg()
    judge()
    plane.draw()



    for v in virusList:
        v.draw()
    for b in bulletList:
        b.draw()

    if not alive:
        screen.blit('over.png', (0, 0))
        screen.draw.text('GameOver', center=[255, 500], fontsize=110, color='red')
    screen.draw.text(str(score), center=[450, 35], fontsize=80)


clock.schedule_interval(getVirus, 1)  # 可以实现自动攻击,参数一没有括号
# clock.schedule_interval(getVirus(), 0.5) # 只能触发一次
# clock.schedule_unique(getBullet(), 1.0)# 报警告 没效果

pgzrun.go()
