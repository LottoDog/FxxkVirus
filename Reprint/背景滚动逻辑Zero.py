import pgzrun


WIDTH = 480
HEIGHT = 670
TITLE = 'FXXL'
# bg = Actor('bg.png')
# bg.x = 240
# bg.y = 335
# bg2 = Actor('bg.png')

y1 = 0
y2 = -670
def update():
    global x1, y1, x2, y2
    y1 += 2
    y2 += 2
    screen.blit('bg.png', (0, y1))
    screen.blit('bg.png', (0, y2))

    if y2 > 670:
        y2 = -670
    if y1 > 670:
        y1 = -670


# def draw():
#     bg.draw()
#     bg2.draw()

pgzrun.go()