import sys,pygame
import math
import time
import random
import _thread
from economy import *
from functions import *
from battle import *
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

economy_background = pygame.image.load("images\\png\\backgrounds\\economy.png").convert()
economy_background=pygame.transform.smoothscale(economy_background,(width,height))
economy_background_Rect = economy_background.get_rect()
#screen.blit(economy_background, economy_background_Rect)
#initializarea ecranului si colorarea lui cu negru
'''
</screen init>
''' 


"""
<game variables>
"""
game=True    #cand avem game over devine fals.
you_won="Not Yet"   #daca ai castigat, devine True, altfel devine False

intro=1  #variabila care retine ca se reda introducerea in joc
clicked_next=-1   #daca s-a dat click pe butonul next in intro

minimised_screen=False  #variabila care verifica daca ecranul este minimizat


delay=(1920*1080/(infoObject.current_w*infoObject.current_h))/10000
if infoObject.current_w<1000:
    delay*=5

click=Clicker()    #initializam clicker-ul, care tine scorul si proceseaza click-urile pe banut

left_click=-1
right_click=-1     #variabile pt a sti ce click s-a dat


clicked_worker=-1
clicked_upgrade=-1

clicked_soldier=-1
clicked_soldier_upgrade=-1

clicked_horse=-1         
clicked_horse_upgrade=-1   

clicked_research=-1        #variabile pt a procesa cand s-a dat click pe anumite elemente, necesare pt a sesiza cand s-a ridicat butonul de click-stanga de pe ele
production_counter=0       #o valoare ce va creste pana la 60, din motive de optimizare. Asadar unele verificari/actualizari se fac o data la 60 de iteratii ale buclei jocului

clicked_battle_button=-1  #variabila memoreaza pe ce buton s-a dat click in timpul bataliei

worker_list=list()          #initializam muncitorii si calul

worker0=Worker(name="Refugee",price=20,cash=3,cash_increment=1,can_be_upgraded=False,upgrade_cost=500,time_period=1,center=(400,450),
 image="images\\png\\workers\\refugee.png")
worker_list.append(worker0)
worker1=Worker(name="Peasant",price=300,cash=100,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=800,time_period=3.5,center=(400,505),
 image="images\\png\\workers\\peasant.png")
worker_list.append(worker1)
worker2=Worker(name="Hunter",price=1500,cash=120,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=5000,time_period=0.65,center=(400,560),
 image="images\\png\\workers\\hunter.png")
worker_list.append(worker2)
worker3=Worker(name="Lumberjack",price=8000,cash=550,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=25000,time_period=1.3,center=(400,615),
 image="images\\png\\workers\\lumberjack.png")
worker_list.append(worker3)
worker4=Worker(name="Miner",price=45000,cash=2000,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=110000,time_period=2.1,center=(400,670),
 image="images\\png\\workers\\miner.png")
worker_list.append(worker4)
worker5=Worker(name="Mason",price=100000,cash=15000,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=300000,time_period=4.5,center=(400,725), 
image="images\\png\\workers\\mason.png")
worker_list.append(worker5)
worker6=Worker(name="Blacksmith",price=100000,cash=15000,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=350000,time_period=1.8,center=(400,780),
image="images\\png\\workers\\blacksmith.png")
worker_list.append(worker6)
worker7=Worker(name="Goldsmith",price=500000,cash=175000,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=1200000,time_period=2.2,center=(400,835),
image="images\\png\\workers\\goldsmith.png")
worker_list.append(worker7)
worker8=Worker(name="Armourer",price=1000000,cash=60000,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=2200000,time_period=2,center=(400,890),
image="images\\png\\workers\\armourer.png")
worker_list.append(worker8)

horse=Horse(image="images\\png\\horse2.png")

worker9=Worker(name="Merchant",price=15000000,cash=1000000,cash_increment=1.3,can_be_upgraded=True,upgrade_cost=60000000,time_period=1.15,center=(400,1000),
image="images\\png\\workers\\merchant.png")
worker_list.append(worker9)



research_list=list()
agriculture=Research("Agriculture",2500,(150,450),50)          #[0]
research_list.append(agriculture)
hunting_dogs=Research("Hunting Dogs",15000,(850,500),50)        #[1]
research_list.append(hunting_dogs)
horse_breeding=Research("Horse Breeding",10000000,(960,500),50)   #[2]
research_list.append(horse_breeding)
woodcutting=Research("Woodcutting",85000,(75,550),50)           #[3]
research_list.append(woodcutting)
coal_mining=Research("Coal Mining",3000000,(910,600),50)         #[4]
research_list.append(coal_mining)
stone_mining=Research("Stone Mining",1000000,(150,650),50)        #[5]
research_list.append(stone_mining)
iron_mining=Research("Iron Mining",1500000,(850,650),50)          #[6]
research_list.append(iron_mining)
gold_mining=Research("Gold Mining",1500000,(960,650),50)         #[7]
research_list.append(gold_mining)
flanged_mace=Research("Flanged Mace",2500,(1010,750),50)       #[8]
research_list.append(flanged_mace)
a_pole_arms=Research("Adv. Pole Arms",2500,(1830,500),50)      #[9]
research_list.append(a_pole_arms)
jewelry=Research("Jewelry",7000000,(125,750),50)                 #[10]
research_list.append(jewelry)
armourer=Research("Armourer",12000000,(90,860),50)                #[11]
research_list.append(armourer)
sword_forging=Research("Sword Forging",2500,(1150,790),50)     #[12]
research_list.append(sword_forging)
arbalest=Research("Arbalest",2500,(1200,250),50)               #[13]
research_list.append(arbalest)
plate_mail=Research("Plate Mail",2500,(1060,850),50)         #[14]
research_list.append(plate_mail)
gunpowder=Research("Gunpowder",2500,(90,860),50)             #[15]
research_list.append(gunpowder)
musket=Research("Musket",2500,(1200,1000),50)                   #[16]
research_list.append(musket)
market=Research("Market",200000000,(150,200),80)              #[17]
research_list.append(market)

#army researches:
crude_weapons=Research("Crude Weapons",2000,(1200,150),50)              #[18]
research_list.append(crude_weapons)
drafting=Research("Drafting",2000,(1800,290),50)                        #[19]
research_list.append(drafting)
longbow=Research("Longbow",2000,(1200,250),50)                          #[20]
research_list.append(longbow)
battleaxe=Research("Battleaxe",2000,(1830,395),50)                       #[21]
research_list.append(battleaxe)
crossbow=Research("Crossbow",2500,(1200,250),50)                          #[22]
research_list.append(crossbow)
polearms=Research("Polearms",2000,(1150,450),50)                         #[23]
research_list.append(polearms)
guild=Research("Builders' Guild",2000,(1180,610),50)                     #[24]
research_list.append(guild)
school=Research("Engineering School",2000,(1830,610),57)                #[25]
research_list.append(school)
ballistics=Research("Ballistics",2000,(1830,900),50)                    #[26]
research_list.append(ballistics)
heavy_w=Research("Heavy Weapons",2000,(1830,730),50)                    #[27]
research_list.append(heavy_w)
artillery=Research("Artillery",2000,(1650,1000),50)                    #[28]
research_list.append(artillery)

army=Recruit_army()
battle=Battle(army.soldier_list)
animation=Animation()

victories=Victories()
capital_army=2000                #HP-ul total al armatei dusmane din jurul capitalei

"""
</game variables>
"""

"""
<functii>
"""

def get_worker_cash(worker_list,horse_number,horse_power):           #functie care verifica daca s-a ajuns la durata de productie a muncitorilor
    cash=0
    present=time.time()
    for worker in worker_list:
        if worker.time_bought+worker.time_period<=present:
            worker.time_bought=present
            cash+=int(worker.cash*worker.nr*(100+horse_power*horse_number)/100)
    return cash


def check_for_upgrades(click,worker_list,horse,soldier_list):                    # functia afiseaza upgrade-uri posibile pt fiecare muncitor 
    if click.upgrade_cost/2<=click.cash and click.upgrade_available==False:
        click.upgrade_available=True
    if click.upgrade_available==True and click.upgrade_inserted==False:
        click.insert_text("upgrade")
        click.upgrade_inserted=True
    for worker in worker_list:
        if worker.can_be_upgraded==True:
            if worker.upgrade_cost/2<=click.cash and worker.nr>0 and worker.upgrade_available==False:       #conditia: muncitorul sa permita upgrade-uri si sa avem macar jumatate din banii necesari
                worker.upgrade_available=True
            if worker.upgrade_available==True and worker.upgrade_inserted==False:
                worker.insert_picture("upgrade")
                worker.upgrade_inserted=True
    for soldier in soldier_list:
        if soldier.can_be_upgraded==True:
            if soldier.upgrade_cost/2<=click.cash and soldier.nr>0 and soldier.upgrade_available==False:       #conditia: muncitorul sa permita upgrade-uri si sa avem macar jumatate din banii necesari
                soldier.upgrade_available=True
            if soldier.upgrade_available==True and soldier.upgrade_inserted==False:
                soldier.insert_picture("upgrade")
                soldier.upgrade_inserted=True
    if horse.upgrade_cost/2<=click.cash and horse.nr>0 and horse.upgrade_available==False:
        horse.upgrade_available=True
    if horse.upgrade_available==True and horse.upgrade_inserted==False:
        horse.insert_picture("upgrade")
        horse.upgrade_inserted=True


def show_researches(worker_list,cash):                  #functia va afisa research-urile (ce permit accesarea unor muncitori/soldati noi) 
    ok_sword_forging=0
    for worker in worker_list:
        if worker.name=="Refugee":
            if worker.nr>=10:
                agriculture.available=True
                crude_weapons.available=True

        elif worker.name=="Peasant":
            if worker.times_upgraded>=5:
                hunting_dogs.available=True
            if worker.nr>=12:
                drafting.available=True
            if worker.nr>=100:
                horse_breeding.available=True
                
        elif worker.name=="Hunter":
            if worker.times_upgraded>=3:
                if worker.nr>=15:
                    woodcutting.available=True
            if worker.times_upgraded>=5:
                longbow.available=True

        elif worker.name=="Lumberjack":
            if worker.nr>=20:
                coal_mining.available=True
                polearms.available=True
            if worker.times_upgraded>=7:
                battleaxe.available=True
        
        elif worker.name=="Miner":
            if worker.nr>=20:
                stone_mining.available=True
            if worker.times_upgraded>=10:
                iron_mining.available=True
            if worker.nr>=50 and worker.times_upgraded>=15:
                gold_mining.available=True

        elif worker.name=="Mason":
            if worker.nr>=15 and worker.times_upgraded>=10:
                guild.available=True
        
        elif worker.name=="Blacksmith":
            if worker.nr>=10:
                flanged_mace.available=True
            if worker.nr>=20:
                a_pole_arms.available=True
            if worker.nr>=30 and worker.times_upgraded>=15:
                heavy_w.available=True
            if worker.nr>=35 and gold_mining.researched==True:
                jewelry.available=True
            if worker.nr>=40:
                ok_sword_forging=1
            if worker.nr>=60:
                armourer.available=True

        elif worker.name=="Goldsmith":
            if worker.nr>=10:
                market.available=True
            if worker.nr>=5 and ok_sword_forging==1:
                sword_forging.available=True

        elif worker.name=="Armourer":
            if worker.nr>=5 and crossbow.researched==True:
                arbalest.available=True
            if worker.nr>=20 and sword_forging.researched==True:
                plate_mail.available=True
            if worker.nr>=50:
                gunpowder.available=True
            if worker.nr>=60 and gunpowder.researched==True:
                musket.available=True


    if guild.researched==True and army.Builder.nr>10:
        school.available=True

    if army.Engineer.nr>=10 and longbow.researched==True:
        crossbow.available=True

    if army.Engineer.nr>=25:
        ballistics.available=True

    if army.Engineer.nr>=100 and gunpowder.researched==True:
        artillery.available=True

    for research in research_list:
        if research.available==True and research.researched==False:
            research.show()



def setup_game(workers_available,horse_available,reseaches_available,soldiers_available):
    for worker in worker_list:
        if worker.name =="Refugee":
            worker.worker_available=True
        else:
            worker.worker_available=workers_available
        
        if worker.worker_available==True:
            worker.insert_picture("name")
            worker.insert_text()
            if worker.upgrade_available==True:
                worker.insert_picture("upgrade")


    horse.horse_available=horse_available
    if horse.horse_available==True:
        horse.insert_picture("name")
        horse.insert_text()
        if horse.upgrade_available==True:
            horse.insert_picture("upgrade")

    for soldier in army.soldier_list:
        soldier.soldier_available=soldiers_available
        if soldier.soldier_available==True:
            soldier.insert_picture("name")
            soldier.insert_text()
            if soldier.upgrade_available==True:
                soldier.insert_picture("upgrade")



    for research in research_list:
        research.available=reseaches_available

def info_frame():
    poza = pygame.image.load("images\\large\\frame2.png").convert_alpha()
    poza=pygame.transform.smoothscale(poza,(width_correction(370),height_correction(395)))
    poza_Rect = poza.get_rect()
    poza_Rect.left=width_correction(765)
    poza_Rect.top=height_correction(0)
    screen.blit(poza,poza_Rect)

def info_box(what='',nr=-1):

    info_rectagle=pygame.draw.rect(screen,white,(width_correction(799),height_correction(22),width_correction(305),height_correction(350)))
    info_frame()
    if what=='coin':
        insert_fixed_text("Magic",940,60,word_color=black,background_color=white)
        insert_fixed_text("Gold Coin",940,110,word_color=black,background_color=white)
        insert_fixed_text("It grants you",940,150,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"{click.click_cash} gold",940,200,font_size=16,word_color=black,background_color=white)
        insert_fixed_text("when you left-click on it",940,250,font_size=16,word_color=black,background_color=white)

    elif what=='coin_upg':
        insert_fixed_text("Coin Upgrade",940,60,word_color=black,background_color=white)
        insert_fixed_text("Makes your magic coin",940,150,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"produce {correct_big_nr(click.upgrade_bonus)} more gold",940,200,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"per click",940,250,font_size=16,word_color=black,background_color=white)
    
    elif what=="worker":
        insert_fixed_text(f"{worker_list[nr].name}",940,60,word_color=black,background_color=white)
        insert_fixed_text(f"Each worker",940,125,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"produces {correct_big_nr(worker_list[nr].cash)} gold",940,175,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"per {worker_list[nr].time_period} seconds",940,225,font_size=16,word_color=black,background_color=white)

    elif what=="worker_upg":
        insert_fixed_text(f"{worker_list[nr].name}",940,60,word_color=black,background_color=white)
        insert_fixed_text("Upgrade",940,110,word_color=black,background_color=white)
        insert_fixed_text(f"Cost:{correct_big_nr(worker_list[nr].upgrade_cost)}",940,175,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"Makes {worker_list[nr].name}s produce",940,225,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"x{worker_list[nr].cash_increment} more gold",940,275,font_size=16,word_color=black,background_color=white)

    elif what=="soldier":
        insert_fixed_text(f"{army.soldier_list[nr].name}",940,60,word_color=black,background_color=white)
        if army.soldier_list[nr].siege==0:
            insert_fixed_text(f"HP:{army.soldier_list[nr].HP}",940,150,font_size=16,word_color=black,background_color=white)
            insert_fixed_text(f"Attack:{army.soldier_list[nr].attack}%",940,200,font_size=16,word_color=black,background_color=white)
            insert_fixed_text(f"Defense:{army.soldier_list[nr].defense}%",940,250,font_size=16,word_color=black,background_color=white)
        else:
            insert_fixed_text(f"HP:{army.soldier_list[nr].HP}",940,125,font_size=16,word_color=black,background_color=white)
            insert_fixed_text(f"Attack:{army.soldier_list[nr].attack}%",940,175,font_size=16,word_color=black,background_color=white)
            insert_fixed_text(f"Defense:{army.soldier_list[nr].defense}%",940,225,font_size=16,word_color=black,background_color=white)
            insert_fixed_text(f"Siege:{army.soldier_list[nr].siege}%",940,275,font_size=16,word_color=black,background_color=white)

    elif what=="soldier_upg":
        insert_fixed_text(f"{army.soldier_list[nr].name}",940,60,word_color=black,background_color=white)
        insert_fixed_text("Upgrade",940,110,word_color=black,background_color=white)
        upgrade_list=army.select_upgrade_list(nr)
        list_poz=army.soldier_list[nr].times_upgraded%len(upgrade_list)
        upg_name=upgrade_list[list_poz]
        if(upg_name=="HP"):
            insert_fixed_text(f"Cost:{correct_big_nr(army.soldier_list[nr].upgrade_cost)}",940,200,font_size=16,word_color=black,background_color=white)           
            insert_fixed_text(f"Grants +{army.soldier_list[nr].hp_upg} HP",940,250,font_size=16,word_color=black,background_color=white)
        elif(upg_name=="AT"):
            insert_fixed_text(f"Cost:{correct_big_nr(army.soldier_list[nr].upgrade_cost)}",940,200,font_size=16,word_color=black,background_color=white)   
            insert_fixed_text(f"Grants +{army.soldier_list[nr].at_upg}% attack",940,250,font_size=16,word_color=black,background_color=white)
        elif(upg_name=="DEF"):
            insert_fixed_text(f"Cost:{correct_big_nr(army.soldier_list[nr].upgrade_cost)}",940,200,font_size=16,word_color=black,background_color=white)   
            insert_fixed_text(f"Grants +{army.soldier_list[nr].at_upg}% defense",940,250,font_size=16,word_color=black,background_color=white)
        elif(upg_name=="S"):
            insert_fixed_text(f"Cost:{correct_big_nr(army.soldier_list[nr].upgrade_cost)}",940,200,font_size=16,word_color=black,background_color=white)   
            insert_fixed_text(f"Grants +{army.soldier_list[nr].siege_upg}% siege",940,250,font_size=16,word_color=black,background_color=white)

    elif what=="horse":
        insert_fixed_text(f"Horse",940,60,word_color=black,background_color=white)
        insert_fixed_text(f"Each horse",940,125,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"increases production by",940,175,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"+{horse.power}%",940,225,font_size=16,word_color=black,background_color=white)

    elif what=="horse_upg":
        insert_fixed_text(f"Horse",940,60,word_color=black,background_color=white)
        insert_fixed_text("Upgrade",940,110,word_color=black,background_color=white)
        insert_fixed_text(f"Cost:{correct_big_nr(horse.upgrade_cost)}",940,175,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"Increases horse",940,225,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"production bonus",940,275,font_size=16,word_color=black,background_color=white)
        insert_fixed_text(f"by +1%",940,325,font_size=16,word_color=black,background_color=white)



    else:
        insert_fixed_text("Info Box",940,60,word_color=black,background_color=white)
        insert_fixed_text("Right click on something",940,150,font_size=16,word_color=black,background_color=white)
        insert_fixed_text("To find out what it does",940,200,font_size=16,word_color=black,background_color=white)

def draw_economy():
    screen.blit(economy_background, economy_background_Rect)
    click.draw_unclicked()

    rectagle=pygame.draw.rect(screen,white,(width_correction(1880),height_correction(0),width_correction(40),height_correction(40)))        #desenam butonul de iesire
    insert_fixed_text(text="X",centerX=1900, centerY=20,word_color=black,background_color="None")

    info_box()
    info_frame()
    
    click.insert_text("cash")
    click.insert_text("upgrade")
    click.upgrade_inserted=True
    army.insert_army_score()
    victories.write()

    for worker in worker_list:
        if worker.worker_available==True:
            worker.insert_picture("name")
            worker.insert_text()
            worker.upgrade_inserted=False

    if horse.horse_available==True:
        horse.insert_picture("name")
        horse.insert_text()
        horse.upgrade_inserted=False

    for soldier in army.soldier_list:
        if soldier.soldier_available==True:
            soldier.insert_picture("name")
            soldier.insert_text()
            soldier.upgrade_inserted=False

    check_for_upgrades(click,worker_list,horse,army.soldier_list)       #afisam upgrade-urile posibile
    for research in research_list:                                      #afisam research-urile disponibile
        if research.available==True and research.researched==False:
            research.show()


    if victories.nr>=30:              #daca avem min 30 de victorii, putem sa desenam butonul
        victories.capital_button()

    pygame.display.flip()

def game_over():
    global you_won
    screen.fill(black)
    if you_won==False:
        background = pygame.image.load("images\\png\\backgrounds\\defeat.jpg").convert_alpha()
        background=pygame.transform.smoothscale(background,(width_correction(1920),height_correction(1080)))
        background_Rect = background.get_rect()
        screen.blit(background,background_Rect)
        insert_fixed_text('Game Over',960,540,correction='w')
    elif you_won==True:
        background = pygame.image.load("images\\png\\backgrounds\\victory.jpg").convert_alpha()
        background=pygame.transform.smoothscale(background,(width_correction(1920),height_correction(1080)))
        background_Rect = background.get_rect()
        screen.blit(background,background_Rect)
        insert_fixed_text('Congratulations! You have driven the enemy out of the country!',960,540,correction='w') 
    rectagle=pygame.draw.rect(screen,white,(width_correction(1880),height_correction(0),width_correction(40),height_correction(40)))        #desenam butonul de iesire
    insert_fixed_text(text="X",centerX=1900, centerY=20,word_color=black,background_color="None")
    pygame.display.flip()


def battle_loop(battle,final=False):
    # drawn_armies=1
    global game,left_click,clicked_battle_button,click,production_counter,victories,capital_army,you_won
    time.sleep(2)
    print(len(battle.button_list))
    while game:                                                      #bucla luptei
        if infoObject.current_w<1920 or infoObject.current_h<1080:
            time.sleep(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.VIDEOEXPOSE:
                screen.blit(battle.battle_background,battle.battle_background_Rect)
                screen.fill(black)
                pygame.display.update()

        
        if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
            left_click=1
            x,y=pygame.mouse.get_pos()
                        #verificarea daca s-a dat click pe patratul de iesire

            for i in range(0,len(battle.button_list)):
                if battle.button_list[i].check_clicked(x,y)==True:
                    clicked_battle_button=i
                    print(i)
                    break

        elif pygame.mouse.get_pressed() == (0, 0, 0):   #verificam cand s-a ridicat butonul de click-stanga, pt a procesa actiunea
            if left_click==1:
                left_click=-1
                if clicked_battle_button!=-1:
                    if clicked_battle_button==0:           #booze_button
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3) 
                        for i in range(0,5):
                            if battle.bonus_list[i]==0:
                                battle.bonus_list[i]=1500
                                battle.morale.your_morale=min(battle.morale.your_morale+2,100)
                                battle.morale.draw_your_morale()
                                break
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)    


                    elif clicked_battle_button==1:         #gold_button
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3) 
                        for i in range(5,10):
                            if battle.bonus_list[i]==0:
                                battle.bonus_list[i]=3300
                                battle.morale.your_morale=min(battle.morale.your_morale+5,100)
                                battle.morale.draw_your_morale()
                                break

                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3) 

                    elif clicked_battle_button==2:        #ladies_button
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3)
                        for i in range(10,13):
                            if battle.bonus_list[i]==0:
                                battle.bonus_list[i]=1200
                                break 
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)

                    elif clicked_battle_button==3:       #lands_button
                        battle.land_button.not_used=False
                        battle.bonus_list[13]=4500
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3) 
                        battle.morale.your_morale=min(battle.morale.your_morale+20,100)
                        battle.morale.draw_your_morale()
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)

                    elif clicked_battle_button==4:       #titles button
                        battle.titles_button.not_used=False
                        battle.bonus_list[14]=4500
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3)
                        battle.morale.your_morale=min(battle.morale.your_morale+50,100)
                        battle.morale.draw_your_morale() 
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)

                    elif clicked_battle_button==5:
                        battle.rabble_button.not_used=False
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3)
                        battle.your_acc_damage[0]=0
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)

                    elif clicked_battle_button==6:
                        battle.militia_button.not_used=False
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3)
                        battle.your_acc_damage[1]=0
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)

                    elif clicked_battle_button==7:
                        battle.archers_button.not_used=False
                        battle.erase_army_stats(1,1)
                        battle.erase_army_stats(1,2)
                        battle.erase_army_stats(1,3)
                        battle.your_acc_damage[2]=0
                        battle.insert_army_stats(1,1)
                        battle.insert_army_stats(1,2)
                        battle.insert_army_stats(1,3)

                    elif clicked_battle_button==8:               #retreat button
                        click.cash=battle.end()                                      #incheiem lupta (adica pregatim urmatoarea armata dusmana)
                        battle.victory=2     #enemy wins
                        victories.nr-=2                         #daca ne predam, penalizarea e mai mica
                        if victories.nr<0:
                            you_won=False
                            game_over()                                       #afisam game over
                            game=False                                        #incheiem jocul
                            return
                        for i in range(0,len(army.soldier_list)):            #reducem soldatii pierduti din armata jucatorului
                            while army.soldier_list[i].nr>battle.your_army_list[i].nr:         
                                army.soldier_list[i].reduce_by_one_lite()
                        time.sleep(1.5)                                     #trebuie sleep o secunda sa se incheie threadurile cu animatiile
                        draw_economy()                                    #desenam ecranul cu economia
                        battle.set_next_attack()                          #setam timpul urmatorului atac
                        left_click=-1
                        clicked_battle_button=-1                          #resetam left-click-ul si battle button-ul
                        break

                    battle.erase_army_stats(1,4)
                    battle.button_tax(clicked_battle_button)
                    battle.insert_army_stats(1,4)
                    battle.check_for_buttons()
                    clicked_battle_button=-1

        if production_counter==100:
            nr=random.randint(1,3)
            if battle.turn==1:
                if nr==1:
                    _thread.start_new_thread(animation.your_cannon_anim,(battle.battle_background,""))
                elif nr==2:
                    _thread.start_new_thread(animation.your_arrow_anim,(battle.battle_background,""))
                elif nr==3:
                    _thread.start_new_thread(animation.your_cavcharge,(battle.battle_background,""))
            if battle.turn==2:  #draw_enemy_cannonballs
                if nr==1:
                    _thread.start_new_thread(animation.enemy_cannon_anim,(battle.battle_background,""))
                elif nr==2:
                    _thread.start_new_thread(animation.enemy_arrow_anim,(battle.battle_background,""))
                elif nr==3:
                    _thread.start_new_thread(animation.enemy_cavcharge,(battle.battle_background,""))
        production_counter+=1           #folosim acelasi counter si pt a monitoriza batalia

        for i in range(0,len(battle.bonus_list)):  #scadem din durata bonusuriolr
            if battle.bonus_list[i]>0:
                battle.bonus_list[i]-=1
            if (i==13 or i==14):
                if battle.bonus_list[i]==0:
                    battle.button_list[i-10].not_used=True

        if production_counter%60==0:     #la fiecare a 60-a iteratie
            capital_army=math.ceil(capital_army*1.0002)

            battle.check_for_buttons()
            battle.modify_morale()
            if battle.morale.your_morale==0:  #daca armata ta si-a pierdut moralul
                battle.victory=2              #dusmanul a castigat
            elif battle.morale.enemy_morale==0:   #daca dusmanul si-a pierdut moralul
                battle.victory=1                  #tu ai castigat

            battle.erase_army_stats(1,1)
            battle.erase_army_stats(1,2)
            battle.erase_army_stats(1,3)

            battle.insert_army_stats(1,1)
            battle.insert_army_stats(1,2)
            battle.insert_army_stats(1,3)

        if production_counter==450:
            # if drawn_armies==0:
            #     animation.draw_ya()
            #     animation.draw_ea()
            #     drawn_armies=1
            # else:
            #     drawn_armies=0
            production_counter=0
            battle.attack()
            
            if battle.victory!=-1:        #daca a castigat cineva, incheiem lupta

                if battle.victory==1:           #daca a castigat jucatorul:
                    victories.nr+=1
                    if final==True:             #daca a invins armata de la capitala
                        you_won=True
                elif battle.victory==2:
                    victories.nr-=5
                    if victories.nr<0:
                        you_won=False

                click.cash=battle.end()    #incheiem lupta (adica pregatim urmatoarea armata dusmana)

                for i in range(0,len(army.soldier_list)):            #reducem soldatii pierduti din armata jucatorului
                    while army.soldier_list[i].nr>battle.your_army_list[i].nr:         
                        army.soldier_list[i].reduce_by_one_lite()


                if you_won==True or you_won==False:
                    time.sleep(1.5) 
                    game_over()                                       #afisam game over
                    game=False                                        #incheiem jocul
                    return
                else:
                    time.sleep(1.5) 
                    draw_economy()                                    #desenam ecranul cu economia


                battle.set_next_attack()                          #setam timpul urmatorului atac
                left_click=-1
                clicked_battle_button=-1                          #resetam left-click-ul si battle button-ul
                return


        pygame.display.flip()



"""
</functii>
"""

'''
<intro>
'''
intro_background="images\\png\\backgrounds\\intro.jpg"
intro_text=["CLICK OUT THE INVADERS", "",""]
x_positions=[500,960,960]
y_positions=[150,175,250]
intro_screen(intro_background,intro_text,x_positions,y_positions)
next_Rect=insert_fixed_text("START", 500, 350,font_size=40)
pygame.display.flip()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.VIDEOEXPOSE:
                intro_screen(intro_background,intro_text,x_positions,y_positions,font_size=50)
                insert_fixed_text("START", 500, 350,font_size=40)
                pygame.display.update()

    if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
        left_click=1
        x,y=pygame.mouse.get_pos()
        if in_rect(x,y,next_Rect.left,next_Rect.top,next_Rect.width,next_Rect.height)==True:
            clicked_next=1
    if pygame.mouse.get_pressed() == (0, 0, 0):
        if clicked_next==1:
            clicked_next=-1
            left_click=-1
            intro_background="images\\png\\backgrounds\\intro1.jpg"
            intro_text=["The neighbouring empire has invaded!", "An evil army is sweeping through the nation,","destroying everything in its path."]
            x_positions=[960,960,960]
            y_positions=[100,175,250]
            intro_screen(intro_background,intro_text,x_positions,y_positions)
            next_Rect=insert_fixed_text("NEXT", 960, 1000)
            pygame.display.flip()
            break
        else:
            left_click=-1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.VIDEOEXPOSE:
            intro_screen(intro_background,intro_text,x_positions,y_positions)
            insert_fixed_text("NEXT", 960, 1000)
            pygame.display.update()

    if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
        left_click=1
        x,y=pygame.mouse.get_pos()
        if in_rect(x,y,next_Rect.left,next_Rect.top,next_Rect.width,next_Rect.height)==True:
            clicked_next=1
    if pygame.mouse.get_pressed() == (0, 0, 0):
        if clicked_next==1:
            clicked_next=-1
            left_click=-1
            intro_background="images\\png\\backgrounds\\intro2.png"
            intro_text=["The King's armies have been defeated,", "the country, reduced to ruin!","Just look at your castle!"]
            x_positions=[400,400,400]
            y_positions=[100,175,250]
            intro_screen(intro_background,intro_text,x_positions,y_positions)
            next_Rect=insert_fixed_text("NEXT", 960, 1000)
            pygame.display.flip()
            break
        else:
            left_click=-1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.VIDEOEXPOSE:
            intro_screen(intro_background,intro_text,x_positions,y_positions)
            insert_fixed_text("NEXT", 960, 1000)
            pygame.display.update()

    if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
        left_click=1
        x,y=pygame.mouse.get_pos()
        if in_rect(x,y,next_Rect.left,next_Rect.top,next_Rect.width,next_Rect.height)==True:
            clicked_next=1
    if pygame.mouse.get_pressed() == (0, 0, 0):
        if clicked_next==1:
            clicked_next=-1
            left_click=-1
            intro_background="images\\png\\backgrounds\\intro3b.png"
            intro_text=["However, all in not lost. During your flee, you managed to rescue your family heirloom: a magic gold coin.", 
            "This special item creates gold out of thin air for its master, when they're in dire need.",
            "Use its powers to gather men and build an army, before the enemy conquers the capital city!"]
            x_positions=[960,960,960]
            y_positions=[100,175,250]
            intro_screen(intro_background,intro_text,x_positions,y_positions)
            next_Rect=insert_fixed_text("BEGIN", 960, 1000)
            pygame.display.flip()
            break
        else:
            left_click=-1 
            
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.VIDEOEXPOSE:
            intro_screen(intro_background,intro_text,x_positions,y_positions)
            insert_fixed_text("BEGIN", 960, 1000)
            pygame.display.update()

    if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
        left_click=1
        x,y=pygame.mouse.get_pos()
        if in_rect(x,y,next_Rect.left,next_Rect.top,next_Rect.width,next_Rect.height)==True:
            clicked_next=1
    if pygame.mouse.get_pressed() == (0, 0, 0):
        if clicked_next==1:
            clicked_next=-1
            left_click=-1
            break
        else:
            left_click=-1 

'''
</intro>
'''

screen.blit(economy_background, economy_background_Rect)
victories.write()
if victories.nr>=30:
    victories.capital_button()
#victories.capital_button()


click.draw_unclicked()   #desenam moneda

rectagle=pygame.draw.rect(screen,white,(width_correction(1880),height_correction(0),width_correction(40),height_correction(40)))        #desenam butonul de iesire
insert_fixed_text(text="X",centerX=1900, centerY=20,word_color=black,background_color="None")

setup_game(workers_available=False,horse_available=False,reseaches_available=False,soldiers_available=False)

info_box()
info_frame()
army.update_army_score()


while 1:                                                          #bucla jocului
    while game:                                                      #bucla economica
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.VIDEOEXPOSE and minimised_screen==False:
                minimised_screen=True
            elif event.type==pygame.VIDEOEXPOSE and minimised_screen==True: 
                minimised_screen=False 
                draw_economy()
                pygame.display.update()
            

        if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
            left_click=1
            x,y=pygame.mouse.get_pos()

            #verificarea daca s-a dat click pe banut
            if in_circle(x,y,width_correction(400),height_correction(200),height_correction(95))==True:
                click.click_ok=1
                click.draw_clicked()

            #verificarea daca s-a dat click pe patratul de iesire
            elif in_rect(x,y,width_correction(1880),height_correction(0),width_correction(40),height_correction(40))==True:
                sys.exit()

            #verificarea daca s-a dat click pe dreptunghiul de upgrade:
            elif in_rect(x,y,click.upgradeRect.x,click.upgradeRect.y,click.upgradeRect.width,click.upgradeRect.height)==True:
                if click.cash>=click.upgrade_cost:
                    click.upgrade_ok=1

            #verificam daca s-a dat click pe cal/upgrade-ul pt cal
            elif horse.check_clicked(x,y,click.cash)==True:
                clicked_horse=1
            elif horse.check_upg_clicked(x,y,click.cash)==True:
                clicked_horse_upgrade=1

            elif victories.check_clicked(x,y)==True:      #verificam daca s-a dat click pe butonul de eliberat capitala
                victories.clicked=1

            #verificam daca s-a dat click pe un muncitor/upgrade al unui muncitor
            else:
                for i in range (0,len(worker_list)):
                    if worker_list[i].check_clicked(x,y,click.cash)==True:
                        clicked_worker=i
                        break
                    elif worker_list[i].check_upg_clicked(x,y,click.cash)==True:
                        clicked_upgrade=i
                        break
                for i in range (0,len(army.soldier_list)):                           #verificam daca s-a dat click pe un soldat
                    if army.soldier_list[i].check_clicked(x,y,click.cash)==True:
                        clicked_soldier=i
                        break
                    elif army.soldier_list[i].check_upg_clicked(x,y,click.cash)==True:
                        clicked_soldier_upgrade=i
                        break

                #verificam daca s-a dat click pe un Research:
                for i in range (0,len(research_list)):
                    if research_list[i].check_clicked(x,y,click.cash)==True:
                        clicked_research=i
                        if clicked_research==17:     #daca s-a dat click pe market, care cere mai mult decat bani:
                            if worker1.nr<50 or worker2.nr<30 or worker3.nr<25 or worker6.nr<15 or worker7.nr<5:
                                clicked_research=-1
                        break

        if pygame.mouse.get_pressed() == (0, 0, 1) and right_click==-1:              #verificam cand s-a dat click-dreapta
            right_click=1
            x,y=pygame.mouse.get_pos()

            #verificarea daca s-a dat click pe banut
            if in_circle(x,y,width_correction(400),height_correction(200),height_correction(100))==True:
                click.click_ok=1

            #verificarea daca s-a dat click pe dreptunghiul de upgrade:
            elif in_rect(x,y,click.upgradeRect.x,click.upgradeRect.y,click.upgradeRect.width,click.upgradeRect.height)==True:
                click.upgrade_ok=1  

            #verificam daca s-a dat click pe cal/upgrade-ul pt cal
            elif horse.check_clicked(x,y,click.cash,poz='right')==True:
                clicked_horse=1
            elif horse.check_upg_clicked(x,y,click.cash,poz='right')==True:
                clicked_horse_upgrade=1

            #verificam daca s-a dat click pe un muncitor/upgrade al unui muncitor
            else:
                for i in range (0,len(worker_list)):
                    if worker_list[i].check_clicked(x,y,click.cash,poz='right')==True:
                        clicked_worker=i
                        break
                    elif worker_list[i].check_upg_clicked(x,y,click.cash,poz='right')==True:
                        clicked_upgrade=i
                        break
                for i in range (0,len(army.soldier_list)):                           #verificam daca s-a dat click pe un soldat
                    if army.soldier_list[i].check_clicked(x,y,click.cash,poz='right')==True:
                        clicked_soldier=i
                        break
                    elif army.soldier_list[i].check_upg_clicked(x,y,click.cash,poz='right')==True:
                        clicked_soldier_upgrade=i
                        break

                #verificam daca s-a dat click pe un Research:
                # for i in range (0,len(research_list)):
                #     if research_list[i].check_clicked(x,y,click.cash,poz='right')==True:
                #         clicked_research=i
                #         break
            

        if pygame.mouse.get_pressed() == (0, 0, 0):   #verificam cand s-a ridicat butonul de click-stanga/click-dreapta, pt a procesa actiunea
            if left_click==1:
                left_click=-1
                if click.click_ok==1:         #daca click-ul a fost pe banut
                    click.click_coin()
                    click.draw_unclicked()

                elif click.upgrade_ok==1:     #daca s-a dat click pe upgrade_ul pt banut
                    click.click_upgrade()

                elif victories.clicked==1:    #daca s-a dat click pe butonul de eliberat capitala
                    victories.clicked=-1
                    capital_battle=Battle(army.soldier_list)   #creem armata la capitala
                    HP_per_soldier=capital_army/17
                    for i in range(0,len(capital_battle.enemy_army_list_at_start)):
                        if i!=9 and i!=10:
                            capital_battle.enemy_army_list_at_start[i].nr=math.ceil(HP_per_soldier/capital_battle.enemy_army_list_at_start[i].HP)
                            if capital_battle.enemy_army_list_at_start[i].can_be_upgraded==True:
                                while capital_battle.enemy_army_list_at_start[i].can_be_upgraded==True:
                                    capital_battle.upgrade(i)

                    capital_battle.enemy_army_list=copy.deepcopy(capital_battle.enemy_army_list_at_start)
                    screen.fill(black)
                    capital_battle.select_background(final=True)   
                    capital_battle.begin(army.soldier_list,click.cash)
                    animation.draw_ya()
                    animation.draw_ea()
                    left_click=-1                                 #resetam left click
                    right_click=-1                                #resetam right click
                    pygame.display.flip()
                    battle_loop(battle=capital_battle,final=True)
                    


                elif clicked_worker>-1:      #daca s-a dat click pt a cumpara un muncitor, verificam care este si incercam sa-l cumparam

                    if clicked_worker==0:                                   #daca am cumparat Refugee
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")


                    if clicked_worker==1 and worker_list[0].nr>0:            #daca am cumparat Peasant:

                        worker_list[0].erase_text()
                        worker_list[0].nr-=1
                        worker_list[0].insert_text()                        #reducem un Refugee
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==2 and worker_list[1].nr>0:             #daca am cumparat Hunter
                        worker_list[1].reduce_by_one()                          #reducem un Peasant
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==3 and worker_list[2].nr>0:             #daca am cumparat Lumberjack
                        worker_list[2].reduce_by_one()                          #reducem un Hunter
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==4 and worker_list[3].nr>0:             #daca am cumparat Miner
                        worker_list[3].reduce_by_one()                          #reducem un Lumberjack
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==5 and worker_list[4].nr>0:             #daca am cumparat Mason
                        worker_list[4].reduce_by_one()                          #reducem un Miner
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==6 and worker_list[4].nr>0:             #daca am cumparat Blacksmith
                        worker_list[4].reduce_by_one()                          #reducem un Miner
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==7 and worker_list[6].nr>0:             #daca am cumparat Goldsmith
                        worker_list[6].reduce_by_one()                          #reducem un Blacksmith
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==8 and worker_list[6].nr>0:             #daca am cumparat Armourer
                        worker_list[6].reduce_by_one()                          #reducem un Blacksmith
                        click.erase("cash")
                        click.cash=worker_list[clicked_worker].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_worker==9:             #daca am cumparat Merchant
                        available=0
                        for i in range(1,9):
                            if worker_list[i].nr>0:
                                available+=1
                        if available>0:
                            x=0
                            while x==0:
                                reduced=random.randint(1,8)                             #reducem random unul din ceilalti muncitori (pt ca oricine se poate apuca de negot)
                                x=worker_list[reduced].nr

                            worker_list[reduced].reduce_by_one()                          
                            click.erase("cash")
                            click.cash=worker_list[clicked_worker].buy(click.cash)
                            click.insert_text("cash")

                    clicked_worker=-1



                elif clicked_upgrade>-1:    #daca s-a dat click pe upgrade, incarcam functia de upgrade.
                    click.erase("cash")
                    click.cash=worker_list[clicked_upgrade].upgrade(click.cash)
                    clicked_upgrade=-1
                    click.insert_text("cash")



                elif clicked_soldier>-1:      #daca s-a dat click pt a cumpara un soldat, verificam care este si incercam sa-l cumparam  
                    if clicked_soldier==0 and worker_list[0].nr>0:    #daca s-a dat click pe un Rabble                           
                        worker_list[0].erase_text()
                        worker_list[0].nr-=1
                        worker_list[0].insert_text()  #reducem un Refugee            
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==1 and worker_list[1].nr>0:      #daca s-a dat click pe un Militia
                        worker_list[1].reduce_by_one()                          #reducem un Peasant
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==2 and worker_list[2].nr>0:      #daca s-a dat click pe un Archer
                        worker_list[2].reduce_by_one()                          #reducem un Hunter
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==3 and army.Archer.nr>0:      #daca s-a dat click pe un Crossbowman
                        army.Archer.reduce_by_one()                          #reducem un Archer
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==4 and army.Crossbowman.nr>0:      #daca s-a dat click pe un Arbalest
                        army.Crossbowman.reduce_by_one()                          #reducem un Crossbowman
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==5 and army.Arbalest.nr>0:      #daca s-a dat click pe un Musketeer
                        army.Arbalest.reduce_by_one()                          #reducem un Arbalest
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==6 and worker_list[3].nr>0:      #daca s-a dat click pe un Axeman
                        worker_list[3].reduce_by_one()                          #reducem un Lumberjack
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==7 and worker_list[3].nr>0:      #daca s-a dat click pe un Spearman
                        worker_list[3].reduce_by_one()                          #reducem un Lumberjack
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==8 and army.Spearman.nr>0:      #daca s-a dat click pe un Pikeman
                        army.Spearman.reduce_by_one()                          #reducem un Spearman
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==9 and worker_list[5].nr>0:      #daca s-a dat click pe un Builder
                        worker_list[5].reduce_by_one()                          #reducem un Mason
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==10 and army.Builder.nr>0:      #daca s-a dat click pe un Engineer
                        army.Builder.reduce_by_one()                          #reducem un Builder
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==11 and army.Builder.nr>0 and army.Engineer.nr>1:      #daca s-a dat click pe o Ballista
                        army.Builder.reduce_by_one()                          #reducem un Builder
                        army.Engineer.reduce_by_one()
                        army.Engineer.reduce_by_one()                       #reducem 2 Engineers
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    
                    elif clicked_soldier==12:             #daca s-a dat click pe un Maceman
                        available=0
                        for i in range(0,7):
                            if worker_list[i].nr>0:
                                available+=1
                        if available>0:
                            x=0
                            while x==0:
                                reduced=random.randint(0,6)                             #reducem random un muncitor din intervalul Refugee-Blacksmith
                                x=worker_list[reduced].nr

                            worker_list[reduced].reduce_by_one()                          
                            click.erase("cash")
                            click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                            click.insert_text("cash")

                    elif clicked_soldier==13 and army.Builder.nr>1 and army.Engineer.nr>1:      #daca s-a dat click pe o Catapulta
                        army.Builder.reduce_by_one()
                        army.Builder.reduce_by_one()                          #reducem 2 Builderi
                        army.Engineer.reduce_by_one()
                        army.Engineer.reduce_by_one()                       #reducem 2 Engineers
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==14 and worker_list[6].nr>0:      #daca s-a dat click pe un Warhammer
                        worker_list[6].reduce_by_one()                          #reducem un Blacksmith
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==15:             #daca s-a dat click pe un Swordsman
                        available=0
                        for i in range(4,8):
                            if worker_list[i].nr>0:
                                available+=1
                        if available>0:
                            x=0
                            while x==0:
                                reduced=random.randint(4,7)                             #reducem random un muncitor din intervalul Miner-Goldsmith
                                x=worker_list[reduced].nr

                            worker_list[reduced].reduce_by_one()                          
                            click.erase("cash")
                            click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                            click.insert_text("cash")

                    elif clicked_soldier==16 and army.Swordsman.nr>0 and horse.nr>0:      #daca s-a dat click pe un Light Cavalry
                        army.Swordsman.reduce_by_one()                          #reducem un Swordsman
                        horse.reduce_by_one()                                   #reducem un cal
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==17 and army.Lcav.nr>0:      #daca s-a dat click pe un Heavy Cavalry
                        army.Lcav.reduce_by_one()                          #reducem un Light Cavalry
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    elif clicked_soldier==18 and army.Builder.nr>1 and army.Engineer.nr>1:      #daca s-a dat click pe un Tun
                        army.Builder.reduce_by_one()
                        army.Builder.reduce_by_one()                          #reducem 2 Builderi
                        army.Engineer.reduce_by_one()
                        army.Engineer.reduce_by_one()                       #reducem 2 Engineers
                        click.erase("cash")
                        click.cash=army.soldier_list[clicked_soldier].buy(click.cash)
                        click.insert_text("cash")

                    army.update_army_score()
                    clicked_soldier=-1

                elif clicked_soldier_upgrade>-1:    #daca s-a dat click pe upgrade pt soldati, incarcam functia de upgrade.
                    click.erase("cash")
                    click.cash=army.upgrade(clicked_soldier_upgrade,click.cash)
                    clicked_soldier_upgrade=-1
                    click.insert_text("cash")
                    army.update_army_score()
                    clicked_soldier_upgrade=-1

                #horse similar cu muncitorul
                elif clicked_horse>-1:                  
                    clicked_horse=-1
                    click.erase("cash")
                    click.cash=horse.buy(click.cash)
                    click.insert_text("cash")

                elif clicked_horse_upgrade>-1:
                    click.erase("cash")
                    click.cash=horse.upgrade(click.cash)
                    clicked_horse_upgrade=-1
                    click.insert_text("cash")

                #research e mai stufos, deoarece fiecare research face altceva:
                elif  clicked_research>-1:
                    click.erase("cash")
                    click.cash-=research_list[i].cost
                    click.insert_text("cash")
                    research_list[clicked_research].researched=True
                    research_list[clicked_research].erase()

                    if clicked_research==0:   #agriculture
                        worker_list[1].worker_available=True
                        worker_list[1].insert_picture("name")
                        worker_list[1].insert_text()

                    elif clicked_research==1:  #hunting dogs
                        worker_list[2].worker_available=True
                        worker_list[2].insert_picture("name")
                        worker_list[2].insert_text()

                    elif clicked_research==2:  #horse breeding
                        horse.horse_available=True
                        horse.insert_picture("name")
                        horse.insert_text()

                    elif clicked_research==3:  #woodcutting
                        worker_list[3].worker_available=True
                        worker_list[3].insert_picture("name")
                        worker_list[3].insert_text()
                    elif clicked_research==4:   #coal mining
                        worker_list[4].worker_available=True
                        worker_list[4].insert_picture("name")
                        worker_list[4].insert_text()
                    elif clicked_research==5:     #stone mining
                        worker_list[5].worker_available=True
                        worker_list[5].insert_picture("name")
                        worker_list[5].insert_text()
                    elif clicked_research==6:     #iron mining
                        worker_list[6].worker_available=True
                        worker_list[6].insert_picture("name")
                        worker_list[6].insert_text()
                    #gold mining nu intra, deoarece el este o conditie pt a permite research la gold smithing

                    elif clicked_research==8: #flanged mace
                        army.Maceman.soldier_available=True
                        army.Maceman.insert_picture("name")
                        army.Maceman.insert_text()

                    elif clicked_research==9:  #advanced Pole arms
                        army.Pikeman.soldier_available=True
                        army.Pikeman.insert_picture("name")
                        army.Pikeman.insert_text()
                    elif clicked_research==10: #jewelry
                        worker_list[7].worker_available=True
                        worker_list[7].insert_picture("name")
                        worker_list[7].insert_text()
                    elif clicked_research==11:   #armourer
                        worker_list[8].worker_available=True
                        worker_list[8].insert_picture("name")
                        worker_list[8].insert_text()
                    elif clicked_research==12:   #sword forging
                        army.Swordsman.soldier_available=True
                        army.Swordsman.insert_picture("name")
                        army.Swordsman.insert_text()
                        army.Lcav.soldier_available=True
                        army.Lcav.insert_picture("name")
                        army.Lcav.insert_text()
                    elif clicked_research==13:        #arbalest
                        army.Arbalest.soldier_available=True
                        army.Arbalest.insert_picture("name")
                        army.Arbalest.insert_text()
                    elif clicked_research==14:        #plate mail
                        army.Swordsman.soldier_available=True
                        army.Swordsman.insert_picture("name")
                        army.Swordsman.insert_text()
                    #gunpowder nu intra, deoarece el este conditie pt fire arms
                    elif clicked_research==16:        #musket
                        army.Musketeer.soldier_available=True
                        army.Musketeer.insert_picture("name")
                        army.Musketeer.insert_text()
                    elif clicked_research==17:          #market

                        for i in range(0,5):                   #reducerea muncitorilor
                            worker1.reduce_by_one()
                            worker2.reduce_by_one()
                            worker3.reduce_by_one()
                            worker6.reduce_by_one()
                            worker7.reduce_by_one()
                        for i in range(0,10):
                            worker1.reduce_by_one()
                            worker2.reduce_by_one()
                            worker3.reduce_by_one()
                            worker6.reduce_by_one()
                        for i in range(0,10):
                            worker1.reduce_by_one()
                            worker2.reduce_by_one()
                            worker3.reduce_by_one()
                        for i in range(0,5):
                            worker1.reduce_by_one()
                            worker2.reduce_by_one()
                        for i in range(0,20):
                            worker1.reduce_by_one()

                        worker_list[9].worker_available=True
                        worker_list[9].insert_picture("name")
                        worker_list[9].insert_text()

                    elif clicked_research==18:                 #crude weapons
                        army.Rabble.soldier_available=True
                        army.Rabble.insert_picture("name")
                        army.Rabble.insert_text()

                    elif clicked_research==19:                 #drafting
                        army.Militia.soldier_available=True
                        army.Militia.insert_picture("name")
                        army.Militia.insert_text()

                    elif clicked_research==20:                 #longbow:
                        army.Archer.soldier_available=True
                        army.Archer.insert_picture("name")
                        army.Archer.insert_text()

                    elif clicked_research==21:                #battleaxe
                        army.Axeman.soldier_available=True
                        army.Axeman.insert_picture("name")
                        army.Axeman.insert_text()

                    elif clicked_research==22:                #crossbow
                        army.Crossbowman.soldier_available=True
                        army.Crossbowman.insert_picture("name")
                        army.Crossbowman.insert_text()

                    elif clicked_research==23:                #polearms
                        army.Spearman.soldier_available=True
                        army.Spearman.insert_picture("name")
                        army.Spearman.insert_text()

                    elif clicked_research==24:                #guild
                        army.Builder.soldier_available=True
                        army.Builder.insert_picture("name")
                        army.Builder.insert_text()

                    elif clicked_research==25:                #school
                        army.Engineer.soldier_available=True
                        army.Engineer.insert_picture("name")
                        army.Engineer.insert_text()

                        army.Ballista.soldier_available=True
                        army.Ballista.insert_picture("name")
                        army.Ballista.insert_text()


                    elif clicked_research==26:                #ballistics
                        army.Catapult.soldier_available=True
                        army.Catapult.insert_picture("name")
                        army.Catapult.insert_text()

                    elif clicked_research==27:                #heavy weapons
                        army.Warhammer.soldier_available=True
                        army.Warhammer.insert_picture("name")
                        army.Warhammer.insert_text()

                    elif clicked_research==28:                #artillery
                        army.Cannon.soldier_available=True
                        army.Cannon.insert_picture("name")
                        army.Cannon.insert_text()


                    clicked_research=-1

            elif right_click==1:
                right_click=-1
                if click.click_ok==1:         #daca click-ul a fost pe banut
                    click.click_coin('right')
                    info_box(what='coin')

                elif click.upgrade_ok==1:     #daca s-a dat click pe upgrade_ul pt banut
                    click.click_upgrade('right')
                    info_box(what='coin_upg')
                    
                elif clicked_worker>-1:      #daca s-a dat click pe un muncitor, scriem informatiile despre el
                    info_box(what='worker',nr=clicked_worker)
                    clicked_worker=-1

                elif clicked_upgrade>-1:    #daca s-a dat click pe upgrade, scriem informatia despre upgrade
                    info_box(what='worker_upg',nr=clicked_upgrade)
                    clicked_upgrade=-1

                elif clicked_soldier>-1:      #daca s-a dat click pt a cumpara un soldat, verificam care este si incercam sa-l cumparam                                 
                    info_box(what="soldier",nr=clicked_soldier)
                    clicked_soldier=-1

                elif clicked_soldier_upgrade>-1:    #daca s-a dat click pe upgrade pt soldati, incarcam functia de upgrade.
                    info_box(what="soldier_upg",nr=clicked_soldier_upgrade)
                    clicked_soldier_upgrade=-1

                #horse similar cu muncitorul
                elif clicked_horse>-1:
                    info_box(what="horse",nr=clicked_soldier_upgrade)                  
                    clicked_horse=-1

                elif clicked_horse_upgrade>-1:
                    info_box(what="horse_upg",nr=clicked_soldier_upgrade)
                    clicked_horse_upgrade=-1

                else:
                    info_box()


        if infoObject.current_w<1920 or infoObject.current_h<1080:   #delay-ul pt rezolutie
            time.sleep(delay)
        
        if minimised_screen==False:
            production_counter+=1   #la fiecare iteratie production counter creste cu 1
        if production_counter>=60:     #la fiecare a 60-a iteratie
            capital_army=math.ceil(capital_army*1.0002)
            #print(capital_army)
            production_counter=0
            click.erase("cash")
            click.cash+=get_worker_cash(worker_list,horse.nr,horse.power)   #verificam daca muncitorii au produs ceva
            click.insert_text("cash")
            check_for_upgrades(click,worker_list,horse,army.soldier_list)       #sau daca s-au indeplinit conditiile pentru a afisa noi upgrade-uri
            show_researches(worker_list,click.cash)                                 #sau daca au aparut research-uri noi
            battle.attack_time-=1
            if battle.attack_time<=0:
                    screen.fill(black)
                    battle.select_background(final=False)    
                    battle.begin(army.soldier_list,click.cash)
                    animation.draw_ya()
                    animation.draw_ea()
                    left_click=-1                                 #resetam left click
                    right_click=-1                                #resetam right click
                    pygame.display.flip()
                    battle_loop(battle=battle)


        pygame.display.flip()

    while game==False:                                                      #bucla pt game over screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        if pygame.mouse.get_pressed() == (1, 0, 0) and left_click==-1:              #verificam cand s-a dat click-stanga
            left_click=1
            x,y=pygame.mouse.get_pos()
            #verificarea daca s-a dat click pe patratul de iesire
            if in_rect(x,y,width_correction(1880),height_correction(0),width_correction(40),height_correction(40))==True:
                sys.exit()
            
            left_click=-1