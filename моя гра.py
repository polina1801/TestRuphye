from pygame import *
window = display.set_mode((700,500))
display.set_caption('Моя гра')
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        display.update()
