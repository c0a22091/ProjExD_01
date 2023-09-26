import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    img3 = pg.image.load("ex01/fig/3.png")
    img3 = pg.transform.flip(img3,True,False)
    img4 = pg.transform.rotozoom(img3,3,1.0)
    img5 = pg.transform.rotozoom(img3,5,1.0)
    img6 = pg.transform.rotozoom(img3,7,1.0)
    img7 = pg.transform.rotozoom(img3,9,1.0)
    img8 = pg.transform.rotozoom(img3,11,1.0)
    img9 = pg.transform.rotozoom(img3,13,1.0)
    img10 = pg.transform.rotozoom(img3,15,1.0)
    img11 = pg.transform.rotozoom(img3,17,1.0)
    img12 = pg.transform.rotozoom(img3,19,1.0)
    img13 = pg.transform.rotozoom(img3,21,1.0)
    img14 = pg.transform.rotozoom(img3,23,1.0)
    img15 = pg.transform.rotozoom(img3,25,1.0)
    

    lst = [img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img14,img13,img12,img11,img10,img9,img8,img7,img6,img5,img4,img3]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[1600-x,0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(lst[tmr%25],[300,200])
        pg.display.update()
        tmr += 1      
        clock.tick(100)
        
        
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()