import sys,pygame
import math
import time
import random
pygame.init()
from functions import *     
#importuri si initializari

infoObject = pygame.display.Info()
size = width, height = infoObject.current_w, infoObject.current_h
economy_background = pygame.image.load("images\\png\\backgrounds\\economy.png").convert()
economy_background=pygame.transform.smoothscale(economy_background,(width,height))


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
<classes>
'''
'''
<clicker class>
'''
class Clicker:             #clasa care tine scorul, detecteaza click-uri pe ban si upgrade-uri pt ban
    text_size=width_correction(32)

    cash=0
    click_cash=1
    upgrade_cost=30
    upgrade_bonus=1
    upgrade_available=True
    click_ok=0
    upgrade_ok=0
    upgrade_inserted=False


    def insert_text(self,what):                                        #insereaza text pt scor si upgrade-uri
        font = pygame.font.SysFont('georgia', self.text_size)
        if what=="cash":
            text = font.render(f'Gold: {str(correct_big_nr(int(self.cash)))}', True, yellow)
            self.cashRect = text.get_rect()
            self.cashRect.center=(width_correction(400),height_correction(50))
            screen.blit(text, self.cashRect)

        elif what=="upgrade" and self.upgrade_available==True:
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(300),height_correction(55)))
            self.upgradeRect=poza.get_rect()
            self.upgradeRect.center=(width_correction(400),height_correction(340))
            screen.blit(poza,self.upgradeRect)

            if self.upgrade_cost<10**15:
                font = pygame.font.SysFont('georgia', self.text_size)
            else:
                font = pygame.font.SysFont('georgia', int(self.text_size/1.5))
            upgrade_text = font.render(str(f'Upgrade: {correct_big_nr(self.upgrade_cost)}'), True, yellow)
            text_rect=upgrade_text.get_rect()

            text_rect.center=(width_correction(400),height_correction(340))
            screen.blit(upgrade_text, text_rect)


    def erase(self,what):                                                  #sterge text
        font = pygame.font.SysFont('georgia', self.text_size)
        if what=="cash":
            screen.blit(economy_background, self.cashRect,self.cashRect)

        elif what=="upgrade":
            screen.blit(economy_background, self.upgradeRect,self.upgradeRect)
            self.upgrade_inserted=False

 
    def __init__(self):
        self.coin_picture=pygame.image.load("images\\png\\coin.png").convert_alpha()
        self.coin_picture=pygame.transform.smoothscale(self.coin_picture,(width_correction(200),height_correction(200)))
        self.coin_Rect=self.coin_picture.get_rect()
        self.coin_Rect.center=(width_correction(400),height_correction(200))               
        self.insert_text("cash")
        self.insert_text("upgrade")

    def draw_unclicked(self):
        self.coin_picture=pygame.image.load("images\\png\\coin.png").convert_alpha()
        self.coin_picture=pygame.transform.smoothscale(self.coin_picture,(width_correction(200),height_correction(200)))
        self.coin_Rect=self.coin_picture.get_rect()
        self.coin_Rect.center=(width_correction(400),height_correction(200))
        screen.blit(self.coin_picture,self.coin_Rect)

    def draw_clicked(self):
        screen.blit(economy_background,self.coin_Rect,self.coin_Rect)
        self.coin_picture=pygame.transform.smoothscale(self.coin_picture,(width_correction(180),height_correction(180)))
        self.coin_Rect=self.coin_picture.get_rect()
        self.coin_Rect.center=(width_correction(400),height_correction(200))
        screen.blit(self.coin_picture,self.coin_Rect)



    def click_coin(self,poz='left'):           #functia de click, creste scorul cu valoarea pt un click si afiseaza noua valoare
        self.click_ok=0
        if poz=='left':
            self.erase("cash")
            self.cash+=self.click_cash
            self.insert_text("cash")


    def click_upgrade(self,poz='left'):              #cand dam click pe upgrade, se actualizeaza valori: scorul (cash), castigul per click si costul pt noul upgrade
        self.upgrade_ok=0
        if poz=='left':
            self.erase("cash")
            self.cash-=self.upgrade_cost
            self.insert_text("cash")
            self.erase("upgrade")
            self.upgrade_cost=round(self.upgrade_cost*1.5)
            if self.upgrade_cost/2>self.cash:
                self.upgrade_available=False
            if self.upgrade_cost/2<=self.cash and self.upgrade_available==True:
                self.insert_text("upgrade")
            self.click_cash+=self.upgrade_bonus
            self.upgrade_bonus+=0.25
    

'''
</clicker class>
'''


'''
<worker class>
'''




class Worker:                     #clasa sablon pentru toate tipurile de muncitori (mai putin calul)
    
    text_size=width_correction(20)
    worker_available=False
    nr=0
    time_bought=0
    center=(0,0)
    owned=False
    can_be_upgraded=False
    upgrade_cost=5
    upgrade_available=False
    times_upgraded=0
    image=''
    upgrade_inserted=False

    def insert_picture(self,what):
        if what=="name":
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(250),height_correction(50)))
            self.rect = poza.get_rect()
            self.rect.center=(self.center[0],self.center[1])
            screen.blit(poza, self.rect)

            poza = pygame.image.load(self.image).convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(40),height_correction(40)))
            self.rect1 = poza.get_rect()
            self.rect1.center=(self.center[0]-width_correction(95),self.center[1])
            screen.blit(poza, self.rect1)

        elif what=="upgrade" and self.upgrade_available==True and self.can_be_upgraded==True:
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(50),height_correction(50)))
            self.upgradeRect = poza.get_rect()
            self.upgradeRect.center=(self.center[0]+width_correction(165),self.center[1])
            screen.blit(poza, self.upgradeRect)

            poza = pygame.image.load("images\\png\\upgrade.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(40),height_correction(40)))
            self.poza_upg_Rect = poza.get_rect()
            self.poza_upg_Rect.center=(self.upgradeRect.centerx,self.center[1])
            screen.blit(poza, self.poza_upg_Rect)

    def insert_text(self):
        font = pygame.font.SysFont('georgia', self.text_size)
        insert_text = font.render(f'x{correct_big_nr(self.nr)}', True, yellow)
        self.nr_Rect = insert_text.get_rect()
        self.nr_Rect.left=self.rect1.right
        self.nr_Rect.centery=self.center[1]-width_correction(10)
        screen.blit(insert_text, self.nr_Rect)

        insert_text = font.render(f'Cost:{correct_big_nr(round(self.price))}', True, yellow)
        self.price_info_Rect = insert_text.get_rect()
        self.price_info_Rect.left=self.rect1.right
        self.price_info_Rect.centery=self.center[1]+width_correction(10)
        screen.blit(insert_text, self.price_info_Rect)


    def erase_text(self):
        screen.blit(economy_background, self.nr_Rect, self.nr_Rect) 
        screen.blit(economy_background, self.price_info_Rect, self.price_info_Rect) 

    def erase_upgrade(self):
        screen.blit(economy_background, self.upgradeRect,self.upgradeRect)
        self.upgrade_inserted=False 


    def __init__(self,name,price,cash,cash_increment,can_be_upgraded,upgrade_cost,time_period,center,image):   

        self.name=name                             #numele muncitorului
        self.price=price                           #cat costa
        self.cash=cash                             #cat produce
        self.cash_increment=cash_increment         #de cate ori va creste productia sa la fiecare upgrade
        self.can_be_upgraded=can_be_upgraded       # daca permite upgrade-uri (True/False)
        self.upgrade_cost=upgrade_cost             #costul pt upgrade
        self.time_period=time_period               #la ce perioada de timp va produce resurse (exprimat in secunde) 
        self.center=(width_correction(center[0]),height_correction(center[1]))                         # pozitia centrului dreptunghiului in care vom afisa textul sau
        self.image=image

        if self.worker_available==True:
            self.insert_picture("name")
            self.insert_text()
            if self.can_be_upgraded==True and self.upgrade_available==True:
                self.insert_text("upgrade")



    def check_clicked(self,x,y,cash,poz='left'):                                          #functia verifca daca am dat click pt a cumpara un muncitor
        if poz=='left':
            if self.worker_available==False or self.price>cash:
                return False
        elif poz=='right':
            if self.worker_available==False:
                return False
        if x>=self.rect.x and x<=self.rect.x+self.rect.width:
            if y>=self.rect.y and y<=self.rect.y+self.rect.height:
                return True
        return False


    def check_upg_clicked(self,x,y,cash,poz='left'):                                      #functia verifica daca am dat click pe butonul de upgrade
        if poz=="left":
            if self.worker_available==False or self.upgrade_cost>cash or self.upgrade_available==False or self.can_be_upgraded==False:
                return False
        if poz=="right":
            if self.worker_available==False or self.upgrade_available==False or self.can_be_upgraded==False:
                return False
        if self.can_be_upgraded==True:
            if x>=self.upgradeRect.x and x<=self.upgradeRect.x+self.upgradeRect.width:
                if y>=self.upgradeRect.y and y<=self.upgradeRect.y+self.upgradeRect.height:
                    return True
        return False


    def buy(self, your_cash):                                 #functia de cumparare: incrementeaza cu 1 nr de munciori, scade costul sau din scorul total,
        if your_cash<round(self.price):                              #apoi sterge si reafiseaza valorile modificate pe ecran                      
            return your_cash
        if self.nr==0:
            self.time_bought=time.time()
        #print(self.time_bought)

        self.erase_text()
        your_cash-=round(self.price)
        self.nr+=1
        self.price=self.price*self.cash_increment
        self.insert_text()
        return your_cash


    def upgrade(self, your_cash):                #upgrade-ul modifica productia, pretul pt urmatorul upgrade si scorul. 
        if your_cash<self.upgrade_cost or self.nr<1:
            return your_cash

        your_cash-=self.upgrade_cost
        self.upgrade_cost=round(self.upgrade_cost*1.5)
        self.cash=round(self.cash*self.cash_increment)
        self.times_upgraded+=1

        if self.upgrade_cost/2<=your_cash:
            self.upgrade_available=True
        else:
            self.upgrade_available=False
            self.erase_upgrade()

        return your_cash

    def reduce_by_one(self):
        self.erase_text()
        self.nr-=1
        self.price=self.price/self.cash_increment
        self.insert_text()
        if self.nr==0:
            self.upgrade_available=False
            self.erase_upgrade()


'''
</worker class>
'''


'''
<horse class>
'''


class Horse:                  #Horse este o clasa aparte deoarece nu produce nimic, dar creste randamentul celorlalti muncitori cu un anumit procent per cal cumparat.
    text_size=width_correction(20)              #functiile sunt similare cu worker, dar cu unele modificari
    horse_available=False
    name="Horse"
    nr=0
    price=60000
    power=3              #procentul cu care fiecare cal creste eficenta muncitorilor
    center=(width_correction(400),height_correction(945)) 
    owned=False
    can_be_upgraded=True
    upgrade_cost=200000
    upgrade_available=False
    image=''
    upgradeRect=None
    upgrade_inserted=False

    def insert_picture(self,what):
        if what=="name":
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(250),height_correction(50)))
            self.rect = poza.get_rect()
            self.rect.center=(self.center[0],self.center[1])
            screen.blit(poza, self.rect)

            poza = pygame.image.load(self.image).convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(40),height_correction(40)))
            self.rect1 = poza.get_rect()
            self.rect1.center=(self.center[0]-width_correction(95),self.center[1])
            screen.blit(poza, self.rect1)

        elif what=="upgrade" and self.upgrade_available==True and self.can_be_upgraded==True:
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(50),height_correction(50)))
            self.upgradeRect = poza.get_rect()
            self.upgradeRect.center=(self.center[0]+width_correction(165),self.center[1])
            screen.blit(poza, self.upgradeRect)

            poza = pygame.image.load("images\\png\\upgrade.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(40),height_correction(40)))
            self.poza_upg_Rect = poza.get_rect()
            self.poza_upg_Rect.center=(self.upgradeRect.centerx,self.center[1])
            screen.blit(poza, self.poza_upg_Rect)


    def insert_text(self):
        font = pygame.font.SysFont('georgia', self.text_size)
        insert_text = font.render(f'x{correct_big_nr(self.nr)}', True, yellow)
        self.nr_Rect = insert_text.get_rect()
        self.nr_Rect.left=self.rect1.right
        self.nr_Rect.centery=self.center[1]-width_correction(10)
        screen.blit(insert_text, self.nr_Rect)

        insert_text = font.render(f'Cost:{correct_big_nr(round(self.price))}', True, yellow)
        self.price_info_Rect = insert_text.get_rect()
        self.price_info_Rect.left=self.rect1.right
        self.price_info_Rect.centery=self.center[1]+width_correction(10)
        screen.blit(insert_text, self.price_info_Rect)


    def erase_text(self):
        screen.blit(economy_background, self.nr_Rect, self.nr_Rect) 
        screen.blit(economy_background, self.price_info_Rect, self.price_info_Rect) 

    def erase_upgrade(self):
        screen.blit(economy_background, self.upgradeRect,self.upgradeRect)
        self.upgrade_inserted=False 





    def __init__(self,image):
        self.image=image
        if self.horse_available==True:
            self.insert_picture("name")
            self.insert_text()
        
        if self.upgrade_available==True and self.can_be_upgraded==True:
            self.insert_picture("upgrade")



    def check_clicked(self,x,y,cash,poz='left'):
        if poz=='left':
            if self.horse_available==False or round(self.price)>cash:
                return False
        elif poz=='right':
            if self.horse_available==False:
                return False
        if x>=self.rect.x and x<=self.rect.x+self.rect.width:
            if y>=self.rect.y and y<=self.rect.y+self.rect.height:
                return True
        return False

    def check_upg_clicked(self,x,y,cash,poz='left'):
        if poz=='left':
            if self.horse_available==False or self.upgrade_cost>cash or self.upgrade_available==False or self.can_be_upgraded==False:
                return False
        elif poz=='right':
            if self.horse_available==False or self.upgrade_available==False or self.can_be_upgraded==False:
                return False
        if self.can_be_upgraded==True:
            if x>=self.upgradeRect.x and x<=self.upgradeRect.x+self.upgradeRect.width:
                if y>=self.upgradeRect.y and y<=self.upgradeRect.y+self.upgradeRect.height:
                    return True
        return False


    def buy(self, your_cash):
        if your_cash<round(self.price):
            return your_cash
        #print(self.time_bought)

        self.erase_text()
        your_cash-=round(self.price)
        self.nr+=1
        self.price=self.price*1.3
        self.insert_text()
        return your_cash


    def upgrade(self, your_cash):
        if your_cash<self.upgrade_cost or self.nr<1:
            return your_cash

        #print(self.time_bought)

        your_cash-=self.upgrade_cost
        self.upgrade_cost=round(self.upgrade_cost*1.5)
        self.power=self.power+1
        if self.upgrade_cost/2<=your_cash:
            self.upgrade_available=True
        else:
            self.upgrade_available=False
            self.erase_upgrade()
        return your_cash

    def reduce_by_one(self):
        self.erase_text()
        self.nr-=1
        self.price=self.price/1.3
        self.insert_text()
        if self.nr==0:
            self.upgrade_available=False
            self.erase_upgrade()

'''
</horse class>
'''


'''
<reseach class>
'''

class Research:
    def __init__(self, name,cost,center,radius):
        self.name=name
        self.cost=cost
        self.center=(width_correction(center[0]),height_correction(center[1])) 
        self.radius=height_correction(radius)
        self.available=False
        self.researched=False
    
    def show(self):
        if self.available==True and self.researched==False:
            if self.name=="Market":
                self.rect=pygame.draw.circle(screen,red,self.center,self.radius)

                font = pygame.font.SysFont('georgia',height_correction(12))
                insert_text = font.render("Research Market", True,yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]-height_correction(36))
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render(f"Cost: {correct_big_nr(self.cost)} +", True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]-height_correction(24))
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render("50 Peasants", True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]-height_correction(12))
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render("30 Hunters", True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1])
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render("25 Woodcutters", True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]+height_correction(12))
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render("15 Blacksmiths", True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]+height_correction(24))
                screen.blit(insert_text, insert_textRect)


                insert_text = font.render("5 Goldsmiths", True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]+height_correction(36))
                screen.blit(insert_text, insert_textRect)

                
            else:
                self.rect=pygame.draw.circle(screen,red,self.center,self.radius)

                font = pygame.font.SysFont('georgia',height_correction(12))
                insert_text = font.render("Research", True,yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]-height_correction(12))
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render(str(self.name), True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1])
                screen.blit(insert_text, insert_textRect)

                insert_text = font.render(str(correct_big_nr(self.cost)), True, yellow)
                insert_textRect = insert_text.get_rect()
                insert_textRect.center=(self.center[0],self.center[1]+height_correction(12))
                screen.blit(insert_text, insert_textRect)


    def erase(self):
        screen.blit(economy_background, self.rect, self.rect)

    def check_clicked(self,x,y,cash,poz='left'):
        if self.available==False:
            return False
        if self.researched==True:
            return False
        if poz=='left':
            if self.cost>cash:
                return False
        if math.sqrt( (self.center[0]-x)**2 + (self.center[1]-y)**2)<=self.radius:
            return True
        return False


'''
</reseach class>
'''

'''
<soldier class>
'''




class Soldier:                     #clasa sablon pentru toate tipurile de soldati
    
    text_size=width_correction(24)
    soldier_available=False
    nr=0
    center=(0,0)
    owned=False
    can_be_upgraded=False
    upgrade_cost=5
    upgrade_available=False
    times_upgraded=0
    maximum_upgrades=0
    hp_upg=0
    at_upg=0
    def_upg=0
    image=''
    upgrade_inserted=False

    def insert_picture(self,what):
        if what=="name":
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(250),height_correction(50)))
            self.rect = poza.get_rect()
            self.rect.center=(self.center[0],self.center[1])
            screen.blit(poza, self.rect)

            poza = pygame.image.load(self.image).convert()
            poza=pygame.transform.smoothscale(poza,(width_correction(40),height_correction(40)))
            self.rect1 = poza.get_rect()
            self.rect1.center=(self.center[0]-width_correction(95),self.center[1])
            screen.blit(poza, self.rect1)

        elif what=="upgrade" and self.upgrade_available==True and self.can_be_upgraded==True:
            poza = pygame.image.load("images\\png\\frame.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(50),height_correction(50)))
            self.upgradeRect = poza.get_rect()
            self.upgradeRect.center=(self.center[0]+width_correction(165),self.center[1])
            screen.blit(poza, self.upgradeRect)

            poza = pygame.image.load("images\\png\\upgrade.png").convert_alpha()
            poza=pygame.transform.smoothscale(poza,(width_correction(40),height_correction(40)))
            self.poza_upg_Rect = poza.get_rect()
            self.poza_upg_Rect.center=(self.upgradeRect.centerx,self.center[1])
            screen.blit(poza, self.poza_upg_Rect)

    def insert_text(self):
        font = pygame.font.SysFont('georgia', self.text_size)
        insert_text = font.render(f'x{correct_big_nr(self.nr)}', True, yellow)
        self.nr_Rect = insert_text.get_rect()
        self.nr_Rect.left=self.rect1.right
        self.nr_Rect.centery=self.center[1]-width_correction(10)
        screen.blit(insert_text, self.nr_Rect)

        insert_text = font.render(f'Cost:{correct_big_nr(round(self.price))}', True, yellow)
        self.price_info_Rect = insert_text.get_rect()
        self.price_info_Rect.left=self.rect1.right
        self.price_info_Rect.centery=self.center[1]+width_correction(10)
        screen.blit(insert_text, self.price_info_Rect)


    def erase_text(self):
        screen.blit(economy_background, self.nr_Rect, self.nr_Rect) 
        screen.blit(economy_background, self.price_info_Rect, self.price_info_Rect) 

    def erase_upgrade(self):
        screen.blit(economy_background, self.upgradeRect,self.upgradeRect)
        self.upgrade_inserted=False 


    def __init__(self,name,price,price_increment,troop_type,HP,attack,defense,can_be_upgraded,upgrade_cost,upgrade_increment,maximum_upgrades,center,
    image,hp_upg=0,at_upg=0,def_upg=0,siege=0,siege_upg=0):   

        self.name=name                             #numele muncitorului
        self.price=price                           #cat costa
        self.price_increment=price_increment       #de cate ori creste pretul sau la fiecare cumparare
        self.type=troop_type                       #ce tip de unitate este (melee, ranged, siege)
        self.HP=HP                                 #cata viata are
        self.attack=attack                         #attack va fi un procent ce se va inmulti cu HP pt a determina puterea concreta de atac    
        self.defense=defense                       #defense este un procent, cu care se va reduce damage-ul primit
        self.can_be_upgraded=can_be_upgraded       # daca permite upgrade-uri (True/False)
        self.upgrade_cost=upgrade_cost             #costul pt upgrade
        self.upgrade_increment=upgrade_increment   #cu cat creste upgrade-ul
        self.maximum_upgrades=maximum_upgrades         #de cate ori i se poate da upgrade
        self.image=image
        self.hp_upg=hp_upg
        self.at_upg=at_upg
        self.def_upg=def_upg
        self.siege=siege
        self.siege_upg=siege_upg                        
        self.center=(width_correction(center[0]),height_correction(center[1]))                         # pozitia centrului dreptunghiului in care vom afisa textul sau
        if self.soldier_available==True:
            self.insert_picture("name")
            self.insert_text()
            if self.can_be_upgraded==True:
                self.insert_picture("upgrade")

    def check_clicked(self,x,y,cash,poz='left'):                                          #functia verifca daca am dat click pt a cumpara un muncitor
        if poz=='left':
            if self.soldier_available==False or self.price>cash:
                return False
        elif poz=='right':
            if self.soldier_available==False:
                return False
        if x>=self.rect.x and x<=self.rect.x+self.rect.width:
            if y>=self.rect.y and y<=self.rect.y+self.rect.height:
                return True
        return False


    def check_upg_clicked(self,x,y,cash,poz='left'):                                      #functia verifica daca am dat click pe butonul de upgrade
        if poz=="left":
            if self.soldier_available==False or self.upgrade_cost>cash or self.upgrade_available==False or self.can_be_upgraded==False:
                return False
        if poz=="right":
            if self.soldier_available==False or self.upgrade_available==False or self.can_be_upgraded==False:
                return False
        if self.can_be_upgraded==True:
            if x>=self.upgradeRect.x and x<=self.upgradeRect.x+self.upgradeRect.width:
                if y>=self.upgradeRect.y and y<=self.upgradeRect.y+self.upgradeRect.height:
                    return True
        return False


    def buy(self, your_cash):                                 #functia de cumparare: incrementeaza cu 1 nr de munciori, scade costul sau din scorul total,
        if your_cash<round(self.price):                              #apoi sterge si reafiseaza valorile modificate pe ecran                      
            return your_cash
        if self.nr==0:
            self.time_bought=time.time()
        #print(self.time_bought)

        self.erase_text()
        your_cash-=round(self.price)
        self.nr+=1
        self.price=self.price*self.price_increment
        self.insert_text()
        return your_cash

    def reduce_by_one(self):
        self.erase_text()
        self.nr-=1
        self.price=self.price/self.price_increment
        self.insert_text()
        if self.nr==0:
            self.upgrade_available=False
            self.erase_upgrade()

    def reduce_by_one_lite(self):
        self.nr-=1
        self.price=self.price/self.price_increment


'''
</soldier class>
'''

'''
<recruit_army class>
'''
class Recruit_army:
    text_size=width_correction(32)
    strength=0
    soldier_list=list()
    militia_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    archer_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    crossbowman_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    axeman_upgrades=["HP","HP","AT","HP","S","HP","DEF","HP","HP","S"]
    spearman_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    #pikeman primeste aceleasi upgrade-uri ca si spearman
    ballista_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP","S"]
    catapult_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP","S"]
    arbalest_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    musketeer_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    maceman_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    warhammer_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    swordsman_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    lightcav_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    heavycav_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]
    cannon_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP","S"]
    

    def insert_army_score(self):
        font = pygame.font.SysFont('georgia', self.text_size)
        self.strength=0
        for soldier in self.soldier_list:
            self.strength+=soldier.HP*soldier.nr
        text = font.render(f'Army strength: {str(correct_big_nr(int(self.strength)))}', True, yellow)
        self.cashRect = text.get_rect()
        self.cashRect.center=(width_correction(1300),height_correction(50))
        screen.blit(text, self.cashRect) 

    def erase_army_score(self):
        screen.blit(economy_background, self.cashRect,self.cashRect)




    def __init__(self):
        self.insert_army_score()
        self.Rabble= Soldier(name="Rabble",price=55,price_increment=1,troop_type="Melee",HP=100,attack=3,defense=0,   #nr 0
        can_be_upgraded=False,upgrade_cost=0,upgrade_increment=0,maximum_upgrades=0,center=(1400,120),
        image="images\\png\\soldiers\\rabble.png")
        self.soldier_list.append(self.Rabble)

        self.Militia= Soldier(name="Militia",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,   #nr 1
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=16,center=(1400,175),
        image="images\\png\\soldiers\\militia.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Militia)

        self.Archer= Soldier(name="Archer",price=700,price_increment=1.02,troop_type="Ranged",HP=180,attack=12,defense=0,   #nr 2
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,230),
        image="images\\png\\soldiers\\archer.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Archer)

        self.Crossbowman= Soldier(name="Crossbowman",price=700,price_increment=1.02,troop_type="Ranged",HP=250,attack=4,defense=0,   #nr 3
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,285),
        image="images\\png\\soldiers\\crossbowman.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Crossbowman)
        
        self.Arbalest= Soldier(name="Arbalest",price=700,price_increment=1.02,troop_type="Ranged",HP=250,attack=4,defense=0,  #nr 4
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,340),
        image="images\\png\\soldiers\\arbalest.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Arbalest)

        self.Musketeer= Soldier(name="Musketeer",price=700,price_increment=1.02,troop_type="Ranged",HP=250,attack=4,defense=0,   #nr 5
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,395),
        image="images\\png\\soldiers\\musketeer.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Musketeer)

        self.Axeman= Soldier(name="Axeman",price=700,price_increment=1.02,troop_type="Melee,Siege",HP=250,attack=4,defense=0,   #nr 6
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=15,center=(1400,450),
        image="images\\png\\soldiers\\axeman.png",hp_upg=10,at_upg=0.5,def_upg=0.25,
        siege=2,siege_upg=1)
        self.soldier_list.append(self.Axeman)

        self.Spearman= Soldier(name="Spearman",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,    #nr 7
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1300,505),
        image="images\\png\\soldiers\\spearman.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Spearman)

        self.Pikeman= Soldier(name="Pikeman",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,     #nr 8
        can_be_upgraded=False,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1750,505),
        image="images\\png\\soldiers\\pikeman.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Pikeman)

        self.Builder= Soldier(name="Builder",price=700,price_increment=1.02,troop_type="-",HP=0,attack=0,defense=0,        #nr 9
        can_be_upgraded=False,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1300,560),
        image="images\\png\\soldiers\\builder.png")
        self.soldier_list.append(self.Builder)

        self.Engineer= Soldier(name="Engineer",price=700,price_increment=1.02,troop_type="-",HP=0,attack=0,defense=0,       #nr 10
        can_be_upgraded=False,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1750,560),
        image="images\\png\\soldiers\\engineer.png")
        self.soldier_list.append(self.Engineer)

        self.Ballista= Soldier(name="Ballista",price=700,price_increment=1.02,troop_type="Siege,Ranged",HP=250,attack=4,defense=0,    #nr 11
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,615),
        image="images\\png\\soldiers\\ballista.png",hp_upg=10,at_upg=0.5,def_upg=0.25,
        siege=10,siege_upg=1)
        self.soldier_list.append(self.Ballista)

        self.Maceman= Soldier(name="Maceman",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,            #nr 12
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,670),
        image="images\\png\\soldiers\\maceman.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Maceman)

        self.Catapult= Soldier(name="Catapult",price=700,price_increment=1.02,troop_type="Siege,Ranged",HP=250,attack=4,defense=0,    #nr 13
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,725),
        image="images\\png\\soldiers\\catapult.png",hp_upg=10,at_upg=0.5,def_upg=0.25,
        siege=15,siege_upg=1.5)
        self.soldier_list.append(self.Catapult)

        self.Warhammer= Soldier(name="Warhammer",price=700,price_increment=1.02,troop_type="Melee,Siege",HP=250,attack=4,defense=0,   #nr 14
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,780),
        image="images\\png\\soldiers\\warhammer.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Warhammer)

        self.Swordsman= Soldier(name="Swordsman",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,        # nr 15
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,835),
        image="images\\png\\soldiers\\swordsman.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Swordsman)
        
        self.Lcav= Soldier(name="Light Cav.",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,           # nr 16
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,890),
        image="images\\png\\soldiers\\lcav.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Lcav)

        self.Hcav= Soldier(name="Heavy Cav.",price=700,price_increment=1.02,troop_type="Melee",HP=250,attack=4,defense=0,          #nr 17
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,945),
        image="images\\png\\soldiers\\hcav.png",hp_upg=10,at_upg=0.5,def_upg=0.25)
        self.soldier_list.append(self.Hcav)

        self.Cannon= Soldier(name="Cannon",price=700,price_increment=1.02,troop_type="Siege,Ranged",HP=250,attack=4,defense=0,      #nr 18
        can_be_upgraded=True,upgrade_cost=2500,upgrade_increment=1.2,maximum_upgrades=10,center=(1400,1000),
        image="images\\png\\soldiers\\cannon.png",hp_upg=10,at_upg=0.5,def_upg=0.25,
        siege=25,siege_upg=2)
        self.soldier_list.append(self.Cannon)


    def update_army_score(self):
        self.erase_army_score()
        self.insert_army_score()

    def select_upgrade_list(self,nr):
        upgrade_l=list()
        if nr==1:
            upgrade_l=self.militia_upgrades
        elif nr==2:
            upgrade_l=self.archer_upgrades
        elif nr==3:
            upgrade_l=self.crossbowman_upgrades
        elif nr==4:
            upgrade_l=self.arbalest_upgrades
        elif nr==5:
            upgrade_l=self.musketeer_upgrades
        elif nr==6:
            upgrade_l=self.axeman_upgrades
        elif nr==7:
            upgrade_l=self.spearman_upgrades
        elif nr==11:
            upgrade_l=self.ballista_upgrades
        elif nr==12:
            upgrade_l=self.maceman_upgrades
        elif nr==13:
            upgrade_l=self.catapult_upgrades
        elif nr==14:
            upgrade_l=self.warhammer_upgrades
        elif nr==15:
            upgrade_l=self.swordsman_upgrades
        elif nr==16:
            upgrade_l=self.lightcav_upgrades
        elif nr==17:
            upgrade_l=self.heavycav_upgrades
        elif nr==18:
            upgrade_l=self.cannon_upgrades

        return upgrade_l

    def upgrade(self,nr,your_cash):                #upgrade-ul modifica productia, pretul pt urmatorul upgrade si scorul. 
        if your_cash<self.soldier_list[nr].upgrade_cost or self.soldier_list[nr]==0:
            return your_cash

        #print(self.time_bought)



        your_cash-=self.soldier_list[nr].upgrade_cost


        '''
        <situatiile particulare per soldat>
        '''
        upgrade_list=self.select_upgrade_list(nr)

        list_poz=self.soldier_list[nr].times_upgraded % len(upgrade_list)
        what=upgrade_list[list_poz]
        if what=="HP":
            self.soldier_list[nr].HP+=self.soldier_list[nr].hp_upg
        elif what=="AT":
            self.soldier_list[nr].attack+=self.soldier_list[nr].at_upg
        elif what=="DEF":
            self.soldier_list[nr].defense+=self.soldier_list[nr].def_upg
        elif what=="S":
            self.soldier_list[nr].siege+=self.soldier_list[nr].siege_upg

        if nr==7:                       #cand avem Spearman, trebuie sa dam upgrade si pt Pikeman:
            if what=="HP":
                self.Pikeman.HP+=self.Pikeman.hp_upg
            elif what=="AT":
                self.Pikeman.attack+=self.Pikeman.at_upg
            elif what=="DEF":
                self.Pikeman.defense+=self.Pikeman.def_upg
            self.Pikeman.times_upgraded+=1
        '''
        </situatiile particulare per soldat>
        '''

        self.soldier_list[nr].upgrade_cost=round(self.soldier_list[nr].upgrade_cost*self.soldier_list[nr].upgrade_increment)
        self.soldier_list[nr].times_upgraded+=1
        if self.soldier_list[nr].times_upgraded==self.soldier_list[nr].maximum_upgrades:
            self.soldier_list[nr].can_be_upgraded=False
            self.soldier_list[nr].erase_upgrade()

        if self.soldier_list[nr].upgrade_cost/2<=your_cash:
            self.soldier_list[nr].upgrade_available=True
        else:
            self.soldier_list[nr].upgrade_available=False
            self.soldier_list[nr].erase_upgrade()
        return your_cash

'''
</recruit_army class>
'''

'''
<victories class>
'''
class Victories:
    text_size=width_correction(32)
    nr=29
    clicked=-1

    def write(self):
        font = pygame.font.SysFont('georgia', self.text_size)
        text = font.render(f'Victories: {self.nr}/30', True, yellow)
        self.Rect = text.get_rect()
        self.Rect.center=(width_correction(1650),height_correction(50))
        screen.blit(text, self.Rect) 

    def erase(self):
        screen.blit(economy_background, self.Rect,self.Rect)

    def capital_button(self):
        poza = pygame.image.load("images\\png\\swords.png").convert_alpha()
        poza=pygame.transform.smoothscale(poza,(width_correction(140),height_correction(140)))
        self.buttonRect = poza.get_rect()
        self.buttonRect.center=(width_correction(1800),height_correction(150))
        screen.blit(poza,self.buttonRect)
        #self.buttonRect=pygame.draw.rect(screen,blue,(width_correction(1725),height_correction(125),width_correction(150),height_correction(25)+2*self.text_size))
        font = pygame.font.SysFont('georgia', self.text_size)
        text = font.render('Liberate', True, yellow)
        self.capitalRect1= text.get_rect()
        self.capitalRect1.center=(width_correction(1800),height_correction(130)+int(0.5*self.text_size))
        screen.blit(text, self.capitalRect1)
        text = font.render('Capital', True, yellow)
        self.capitalRect2= text.get_rect()
        self.capitalRect2.center=(width_correction(1800),height_correction(130)+int(1.5*self.text_size))
        screen.blit(text, self.capitalRect2) 

    def remove_capital_button(self):
        screen.blit(economy_background,self.buttonRect,self.buttonRect)

    def check_clicked(self,x,y):                                          #functia verifca daca am dat click pt a cumpara un muncitor
        if self.nr<30:
            return False
        if x>=self.buttonRect.x and x<=self.buttonRect.x+self.buttonRect.width:
            if y>=self.buttonRect.y and y<=self.buttonRect.y+self.buttonRect.height:
                return True
        return False
'''
</victories class>
'''



'''
</classes>
'''
