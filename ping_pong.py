from pygame import *



img_back = "back_img.jpg"

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))

    display.update()

