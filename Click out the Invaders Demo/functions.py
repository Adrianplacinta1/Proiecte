import sys,pygame
import math
import time
import random
pygame.init()     
#importuri si initializari


'''
<colors>
'''
black = 0, 0, 0
yellow = 255,255,0
dark_yellow=155,135,12
white= 255,255,255
red=255,0,0
green = (0, 255, 0)
blue = (0, 0, 128)
orange=(255,173,0)

'''
<colors>
'''

'''
<screen init>
'''
infoObject = pygame.display.Info()
size = width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode(size,pygame.FULLSCREEN|pygame.RESIZABLE)
screen.fill(black)
#initializarea ecranului si colorarea lui cu negru
'''
</screen init>
'''     

'''
<big nr correcting function>
'''
def correct_big_nr(nr):
    suffix=['','K','M','B','T','Quadr','Quint','Sext','Sept','Oct','Non','Dec']
    counter=0
    while nr>1000:
        nr=nr/1000
        counter+=1
    if counter==0:
        return nr
    nr=format(nr,".2f")
    return f'{nr} {suffix[counter]}'

'''
</big nr correcting function>
'''  

'''
<resolution correction function>
'''
def width_correction(w):
    if w==0:
        return 0
    return int(width/(1920.0/w))

def height_correction(h):
    if h==0:
        return 0
    return int(height/(1080.0/h))

'''
</resolution correction function>
'''


def in_rect(x,y,rectx,recty,width,height):      #detecteaza daca s-a dat click intr-un anumit dreptunghi
    if x>=rectx and x<=rectx+width:
        if y>=recty and y<=recty+height:
            return True
    return False


def in_circle(x,y,centerx,centery,radius):                  #detecteaza daca s-a dat click intr-un anumit cerc
    if math.sqrt( (centerx-x)**2 + (centery-y)**2)<=radius:
        return True
    return False


def insert_fixed_text(text, centerX,centerY,font_size=32,word_color=dark_yellow,background_color=yellow,correction='w'):                     #insereaza text
    if correction=='w':
        font_size=width_correction(font_size)
    elif correction=='h':
        fontsize=height_correction(font_size)
    elif correction=='n':
        pass
    font = pygame.font.SysFont('georgia',font_size)
    if background_color=="None":
        insert_text = font.render(text, True, word_color)
    else:
        insert_text = font.render(text, True, word_color, background_color)
    insert_textRect = insert_text.get_rect()
    centerX=width_correction(centerX)
    centerY=height_correction(centerY)
    insert_textRect.center=(centerX,centerY)
    screen.blit(insert_text, insert_textRect)
    return insert_textRect




def intro_screen(image,text,x_poz,y_poz,font_size=32):
    intro = pygame.image.load(image).convert_alpha()
    intro=pygame.transform.smoothscale(intro,(width_correction(1920),height_correction(1080)))
    intro_rect=intro.get_rect()
    screen.blit(intro,intro_rect)
    for i in range(0,len(text)):
        insert_fixed_text(text[i],x_poz[i], y_poz[i], background_color="None", font_size=font_size)