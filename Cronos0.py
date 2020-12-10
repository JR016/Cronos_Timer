#                               First Cronos Sketch
#                   Contains Project Title and the Countdown

import random,pygame,Cronos_Text,sys,os,TimeControler

#GLOBAL CONSTANTS
IMAGES_DIRNAME = "images"
FONTS_DIRNAME = "fonts"
TITLE = "Cronos Sketch 0"
ICON = os.path.join(IMAGES_DIRNAME,"cronos.png")
DIMENSIONS = (300,200)

#Initialize pygame
pygame.init()

def main():
    
    global SCREEN, CLOCK, TEXT_TITLE, TIMER, TIMER_TEXT

    pygame.display.set_caption(TITLE)
    icon_img = pygame.image.load(ICON)
    pygame.display.set_icon(icon_img)
    SCREEN = pygame.display.set_mode(DIMENSIONS)
    CLOCK = pygame.time.Clock()
    
    TIMER = TimeControler.Timer()
    TIMER.seconds = random.randint(0,59)
    TIMER.minutes = random.randint(0,59)
    TIMER.hours = random.randint(0,99)
    TIMER.run()
    
    TEXT_TITLE = Cronos_Text.Cronos_Text(TITLE[:6],
                                         os.path.join(FONTS_DIRNAME,"shanghai.ttf"),
                                         50,
                                         (255,0,0),
                                         DIMENSIONS[0]//2,
                                         60)

    TIMER_TEXT = Cronos_Text.Cronos_Text(TIMER.timeFormat,
                                         os.path.join(FONTS_DIRNAME,"starmap.TTF"),
                                         40,
                                         (255,255,255),
                                         DIMENSIONS[0]//2 + 5,
                                         150)

    window_loop()


def window_loop():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_program()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit_program()

        TIMER.countdown()
        TIMER_TEXT.setMessage(TIMER.timeFormat)

        SCREEN.fill((32,32,32))
        SCREEN.blit(TEXT_TITLE.Surface,TEXT_TITLE.Surface_Rect)
        SCREEN.blit(TIMER_TEXT.Surface,TIMER_TEXT.Surface_Rect)

        update_window()
        

def exit_program():
    pygame.quit()
    sys.exit()
    

def update_window():
    pygame.display.update()
    CLOCK.tick(40)




if __name__ == "__main__": 
    main()
