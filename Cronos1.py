#                               Second Cronos Sketch
#                   Contains Project Title and the Countdown
#                      Lets the user set the Countdown 

import pygame,Cronos_Text,PyB,sys,os,TimeControler

#GLOBAL CONSTANTS
IMAGES_DIRNAME = "images"
FONTS_DIRNAME = "fonts"
TITLE = "Cronos Sketch 1"
ICON = os.path.join(IMAGES_DIRNAME,"cronos.png")
DIMENSIONS = (500,450)

#Initialize pygame
pygame.init()

def main():
    
    global SCREEN, TEXT_TITLE, TIMER, TIMER_TEXT, \
           CRONOS_BUTTONS, \
           PLUS_BUTTONS, MINUS_BUTTONS

    pygame.display.set_caption(TITLE)
    icon_img = pygame.image.load(ICON)
    pygame.display.set_icon(icon_img)
    SCREEN = pygame.display.set_mode(DIMENSIONS)
    
    TIMER = TimeControler.Timer()
    
    TEXT_TITLE = Cronos_Text.Cronos_Text(TITLE[:6],
                                         os.path.join(FONTS_DIRNAME,"shanghai.ttf"),
                                         70,
                                         (255,0,0),
                                         DIMENSIONS[0]//2,
                                         70)

    TIMER_TEXT = Cronos_Text.Cronos_Text(TIMER.timeFormat,
                                         os.path.join(FONTS_DIRNAME,"starmap.TTF"),
                                         50,
                                         (255,255,255),
                                         DIMENSIONS[0]//2 + 5,
                                         200)

    CRONOS_BUTTONS = (
        
        PyB.Rect_Button(60,
                        300,
                        70,
                        50,
                        "Run Timer",
                        (240,240,240),
                        12,
                        (100,100,100)
                        ),

        PyB.Rect_Button(205,
                        300,
                        90,
                        50,
                        "Freeze Timer",
                        (240,240,240),
                        12,
                        (100,100,100)
                        ),

        PyB.Rect_Button(370,
                        300,
                        80,
                        50,
                        "Reset Timer",
                        (240,240,240),
                        12,
                        (100,100,100)
                        ),

        PyB.Rect_Button(225,
                        400,
                        50,
                        30,
                        "Exit",
                        (240,240,240),
                        12,
                        (100,100,100)
                        )
        )


    PLUS_BUTTONS = (

        PyB.Circular_Button(175,
                            150,
                            13,
                            "+",
                            (240,240,240),
                            15,
                            (0,155,0)
                            ),

        PyB.Circular_Button(250,
                            150,
                            13,
                            "+",
                            (240,240,240),
                            15,
                            (0,155,0)
                            ),

        PyB.Circular_Button(325,
                            150,
                            13,
                            "+",
                            (240,240,240),
                            15,
                            (0,155,0)
                            )
        )

    MINUS_BUTTONS = (

        PyB.Circular_Button(175,
                            250,
                            13,
                            "-",
                            (240,240,240),
                            13,
                            (155,0,0)
                            ),

        PyB.Circular_Button(250,
                            250,
                            13,
                            "-",
                            (240,240,240),
                            13,
                            (155,0,0)
                            ),

        PyB.Circular_Button(325,
                            250,
                            13,
                            "-",
                            (240,240,240),
                            13,
                            (155,0,0)
                            )
        )

    window_loop()


def window_loop():

    while True:

        SCREEN.fill((32,32,32))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_program()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit_program()

            elif event.type == pygame.MOUSEMOTION:
                mouse_coors = event.pos

                for btn in CRONOS_BUTTONS:
                    btn.check_onhover(mouse_coors)

                for btn in PLUS_BUTTONS:
                    btn.check_onhover(mouse_coors)

                for btn in MINUS_BUTTONS:
                    btn.check_onhover(mouse_coors)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coors = event.pos

                if event.button == 1:

                    for btn in CRONOS_BUTTONS:
                        btn.check_clicked(mouse_coors)

                    for btn in PLUS_BUTTONS:
                        btn.check_clicked(mouse_coors)

                    for btn in MINUS_BUTTONS:
                        btn.check_clicked(mouse_coors)
                 

        for btn in CRONOS_BUTTONS:
            btn.on_hover(lambda:change_color(btn,
                                            (160,160,160),
                                            (250,250,250)))

        for btn in PLUS_BUTTONS:
            btn.on_hover(lambda:change_color(btn,
                                             (0,255,0),
                                             (250,250,250)))

        for btn in MINUS_BUTTONS:
            btn.on_hover(lambda:change_color(btn,
                                             (255,0,0),
                                             (250,250,250)))

        for btn in CRONOS_BUTTONS:
            btn.not_onhover(lambda:change_color(btn,
                                                (140,140,140),
                                                (240,240,240)))

        for btn in PLUS_BUTTONS:
            btn.not_onhover(lambda:change_color(btn,
                                                (0,155,0),
                                                (240,240,240)))

        for btn in MINUS_BUTTONS:
            btn.not_onhover(lambda:change_color(btn,
                                                (155,0,0),
                                                (240,240,240)))

        TIMER.countdown()
        TIMER_TEXT.setMessage(TIMER.timeFormat)

        SCREEN.blit(TEXT_TITLE.Surface,TEXT_TITLE.Surface_Rect)
        SCREEN.blit(TIMER_TEXT.Surface,TIMER_TEXT.Surface_Rect)

        CRONOS_BUTTONS[0].on_click(run_timer)
        CRONOS_BUTTONS[1].on_click(freeze_timer)
        CRONOS_BUTTONS[2].on_click(reset_timer)
        CRONOS_BUTTONS[3].on_click(exit_program)

        #Only change seconds, minutes and hours if the timer is not running
        if not TIMER.isRunning:
         
            PLUS_BUTTONS[0].on_click(lambda:change_time_measure("h",1))      
            PLUS_BUTTONS[1].on_click(lambda:change_time_measure("m",1))
            PLUS_BUTTONS[2].on_click(lambda:change_time_measure("s",1))
            
            MINUS_BUTTONS[0].on_click(lambda:change_time_measure("h",-1))
            MINUS_BUTTONS[1].on_click(lambda:change_time_measure("m",-1))
            MINUS_BUTTONS[2].on_click(lambda:change_time_measure("s",-1))

        for btn in CRONOS_BUTTONS:
            btn.draw_button(SCREEN)

        for btn in PLUS_BUTTONS:
            btn.draw_button(SCREEN)

        for btn in MINUS_BUTTONS:
            btn.draw_button(SCREEN)

        update_window()
        

def exit_program():
    pygame.quit()
    sys.exit()
    

def update_window():
    pygame.display.update()


#Functions when buttons are on Hover
def change_color(button,bgcolor,textcolor):

    button.changeBgColor(bgcolor)
    button.changeTextColor(textcolor)

#Functions when buttons are clicked
def run_timer():

    if TIMER.seconds > 0 or TIMER.minutes > 0 or TIMER.hours > 0:
        TIMER.run()

def freeze_timer():
    TIMER.freeze()

def reset_timer():
    TIMER.reset()


def nearest_num(num,min_num,max_num):

    if num in range(min_num,max_num + 1):
        return num

    else:
        if num < min_num:
            return min_num

        else:
            return max_num

def change_time_measure(measure,change_value):

    #This function will be called in a loop
    #Return early to avoid increasing more than required

    if measure == "s":
        
        TIMER.seconds += change_value
        TIMER.seconds = nearest_num(TIMER.seconds,
                                    TimeControler.Timer.MIN_SECS,
                                    TimeControler.Timer.MAX_SECS)

    elif measure == "m":
        
        TIMER.minutes += change_value
        TIMER.minutes = nearest_num(TIMER.minutes,
                                    TimeControler.Timer.MIN_MINS,
                                    TimeControler.Timer.MAX_MINS)
    elif measure == "h":

        TIMER.hours += change_value
        TIMER.hours = nearest_num(TIMER.hours,
                                  TimeControler.Timer.MIN_HOURS,
                                  TimeControler.Timer.MAX_HOURS)


if __name__ == "__main__": 
    main()
