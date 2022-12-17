import pygame
import win32api
import win32con
import win32gui
import pyautogui
import time
import tkinter as tk
import random
import sys


pygame.init()
info = pygame.display.Info()
w = info.current_w
h = info.current_h
screen = pygame.display.set_mode((w, h), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
stop = False
first_time = True
mouseclick = False
stasis = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (255, 100, 0)
dark_orange = (255, 255, 0)
clicked = 1
display_width = 1920
display_height = 1080
frame = 0
task = False
X = -200
RunAnim = True
triggered = False
mouseclickcount = 1
runAnim = False


# x = (display_width *0.45)
# y = (display_height *0.8)
gameDisplay = pygame.display.set_mode((display_width,display_height))
sprite_sheet = pygame.image.load('Fox Sprite Sheet.png').convert_alpha()
clickeded = False
smallfont = pygame.font.SysFont('Corbel',35)
WHITE = (255,255,255)
text = smallfont.render('quit' , True , WHITE)
# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()



# idleAnim = [pygame.image.load('Fox Sprite Sheet_1.png'), pygame.image.load('Fox Sprite Sheet_2.png'), pygame.image.load('Fox Sprite Sheet_3.png'), pygame.image.load('Fox Sprite Sheet_4.png'), ]


# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
# font = pygame.font.SysFont("Arial", 72)
# text = []
# text.append((font.render("Invisible background", 0, dark_red), (0, 10)))
# text.append((font.render("Press Esc to close the window", 0, dark_red), (0, 100)))
# Create functions
def get_image(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,-104), ((frame*width), 5 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image2(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 5 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image3(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,-204), ((frame*width), 5 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image


import tkinter as tk






window = tk.Tk()
window.title("To-Do List")
window.geometry('300x275')
window.minsize(300, 275)
window.maxsize(1920, 1080)




# frame_0 = get_image(sprite_sheet,0, 32,32,5)
# frame_1 = get_image(sprite_sheet,1, 32,32,5)

enter_animationlist = []
idle_animationlist = []
clicked_animationlist=[]
animation_steps = 11
idleanimation_steps = 4
clickedanimation_steps = 7
last_update = pygame.time.get_ticks()
animation_cooldown = 150






for x in range(animation_steps):
        enter_animationlist.append(get_image(sprite_sheet, x, 32, 128, 8))

for x in range(idleanimation_steps):
        idle_animationlist.append(get_image2(sprite_sheet, x, 32, 32, 8))

for z in range(clickedanimation_steps):
        clicked_animationlist.append(get_image3(sprite_sheet, z, 32, 228, 8))
#


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclickcount += 1
            time.sleep(0.1)

    screen.fill(fuchsia)  # Transparent background
    # pygame.image.load("index.png")
    left, middle, right = pygame.mouse.get_pressed()
    # print(x)
    # print(y)

    time.sleep((8/1000))

    # if left:
    #     clicked += 1
    #     time.sleep(0.1)
    if stasis:
        y = 900
    else:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        print(clickeded)

    if y > 800:
        triggered = True
        if (mouseclickcount % 2) == 0:
            runAnim = True
            stasis = True
            count = True
        else:
            stasis = False
            runAnim = False
            count = False
        # if (clicked % 2) == 0:
        #     clickeded = True
        # else:
        #     clickeded = False
        mouse = pygame.mouse.get_pos()
        if RunAnim:
                current_time = pygame.time.get_ticks()
                if current_time - last_update >= animation_cooldown:
                    frame += 1
                    X += 50
                    last_update = current_time
                if frame >= len(enter_animationlist):
                    frame = 0
                    RunAnim = False
                screen.blit(enter_animationlist[frame], (X, 800))

        elif runAnim:
            # if first_time:
            #     frame = 0
            #     first_time = False
                screen.fill(fuchsia)
                current_time = pygame.time.get_ticks()
                if current_time - last_update >= animation_cooldown:
                     frame += 1
                     last_update = current_time
                if frame >= 7:
                     frame = 6
                screen.blit(clicked_animationlist[frame], (350, 850))

                if count:
                    window = tk.Tk()
                    window.title("To-Do List")
                    window.geometry('200x275')
                    window.minsize(300, 275)
                    window.maxsize(1920, 1080)

                for i in range(10):
                    label = tk.Label(window, text=i + 1).grid(row=i)
                    task = tk.Entry(window)
                    task.grid(row=i, column=1)
                window.mainloop()




        else:
         current_time = pygame.time.get_ticks()
         if current_time - last_update >= animation_cooldown:
                    frame += 1
                    last_update = current_time
         if frame >= len(idle_animationlist):
                    frame = 0
         screen.blit(idle_animationlist[frame], (350, 740))
         print("killme")



    if y < 800:
              if triggered:
                current_time = pygame.time.get_ticks()
                if current_time - last_update >= animation_cooldown:
                  frame += 1
                  X += 150
                  last_update = current_time
                if frame >= len(enter_animationlist):
                    frame = 0
                screen.blit(enter_animationlist[frame], (X, 800))
                RunAnim = True
                if X >= 1920:
                   triggered = False
                   X = -200













    pygame.display.update()

pygame.quit()
