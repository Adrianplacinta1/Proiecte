import sys,pygame
import math
import time
import random
import copy
pygame.init()
from economy import *
from functions import*
import _thread

#pygame.draw.line(screen,Color_line,(60,80),(130,100))


class Button:
    name=''
    image=''

    def __init__(self,name='',color=red,corner=(960,540),width=100,height=100,can_click=True,not_used=True,image=''):
        self.name=name
        self.color=color
        self.corner=(width_correction(corner[0]), height_correction(corner[1]))
        self.width=width_correction(width)
        self.height=height_correction(height)
        self.text_center=(self.corner[0]+self.width/2, self.corner[1]+self.height+width_correction(16+6))
        self.can_click=can_click
        self.not_used=not_used
        self.image=image

        self.rama = pygame.image.load("images\\png\\frame.png").convert_alpha()
        self.rama=pygame.transform.smoothscale(self.rama,(width_correction(50),height_correction(50)))
        self.rect = self.rama.get_rect()
        self.rect.left=self.corner[0]
        self.rect.top=self.corner[1]

        self.poza = pygame.image.load(self.image).convert_alpha()
        self.poza=pygame.transform.smoothscale(self.poza,(width_correction(40),height_correction(40)))
        self.rect1 = self.poza.get_rect()
        self.rect1.left=self.corner[0]+width_correction(5)
        self.rect1.top=self.corner[1]+height_correction(5)
    
    def draw(self):
        if self.can_click==True and self.not_used==True:
            screen.blit(self.rama, self.rect)
            screen.blit(self.poza, self.rect1)
            return True
        return False
            

    def insert_name(self):
        font = pygame.font.SysFont('georgia',width_correction(16))
        insert_text = font.render(self.name, True, dark_yellow, black)
        self.text_rect = insert_text.get_rect()
        self.text_rect.center=(self.text_center[0],self.text_center[1])
        screen.blit(insert_text, self.text_rect)

    


    def check_clicked(self,x,y,poz='left'):                                          #functia verifca daca am dat click pt a cumpara un muncitor
        if self.can_click==False or self.not_used==False:
            return False
        if x>=self.rect.x and x<=self.rect.x+self.rect.width:
            if y>=self.rect.y and y<=self.rect.y+self.rect.height:
                return True
        return False


class Morale:
    your_morale=100
    enemy_morale=100
    text_size=width_correction(32)

    def draw(self):
        pygame.draw.rect(screen,yellow,(width_correction(200),height_correction(940),width_correction(1500),height_correction(100)))
        font = pygame.font.SysFont('georgia', self.text_size)
        insert_text = font.render("MORALE", True, black, yellow)
        text_rect = insert_text.get_rect()
        text_rect.center=(width_correction(960),height_correction(990))
        screen.blit(insert_text,text_rect)

    def draw_your_morale(self):
        color=green
        if self.your_morale<66:
            color=orange
        if self.your_morale<33:
            color=red
        pygame.draw.line(surface=screen,color=black,start_pos=(width_correction(1110),height_correction(990)),
        end_pos=(width_correction(1630),height_correction(990)),width=(height_correction(80)))
        if self.your_morale>0.99:
            pygame.draw.line(surface=screen,color=color,start_pos=(width_correction(1620),height_correction(990)),
            end_pos=(width_correction(1620-self.your_morale*5),height_correction(990)),width=(height_correction(60)))

    def draw_enemy_morale(self):
        color=green
        if self.enemy_morale<66:
            color=orange
        if self.enemy_morale<33:
            color=red
        pygame.draw.line(surface=screen,color=black,start_pos=(width_correction(810),height_correction(990)),
        end_pos=(width_correction(290),height_correction(990)),width=(height_correction(80)))
        if self.enemy_morale>0.99:
            pygame.draw.line(surface=screen,color=color,start_pos=(width_correction(300+self.enemy_morale*5),height_correction(990)),
            end_pos=(width_correction(300),height_correction(990)),width=(height_correction(60)))


    def lower_your_morale(self,nr):
        self.your_morale-=nr
        if self.your_morale<1:
            self.your_morale=0

    def lower_enemy_morale(self,nr):
        self.enemy_morale-=nr
        if self.enemy_morale<1:
            self.enemy_morale=0





class Battle:
    # general
    text_size=width_correction(32)
    battle_start_time=0
    battle_nr=0
    turn=0              #al cui e randul: 1=you,2=enemy
    victory=-1             #cine castiga lupta: 1-you; 2-enemy
    battle_background=''   #imaginea de background
    battle_background_Rect='' #dreptunghiul pt aceasta imagine

    #enemy army
    army_type="standard"
    enemy_best_unit="Militia"         #care este soldatul cel mai avansat al dusmanului
    enemy_strength_at_start=0
    attack_time=0
    enemy_strength=0
    enemy_attack=[]


    militia_upgrades=["HP","HP","AT","HP","HP","DEF","HP","HP"]         #dusmanul are nevoie de listele de upgrades
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



    #your army
    your_strength=0
    your_strength_at_start=0
    your_attack=[]
    your_war_funds=0

    def select_background(self,final=False):
        if final==False:
            picture_list=["images\\png\\backgrounds\\forest.jpg","images\\png\\backgrounds\\forest_fire.jpg","images\\png\\backgrounds\\village.jpg","images\\png\\backgrounds\\house_fire.jpg",
            "images\\png\\backgrounds\\mansion.jpg"]
            i=random.randint(0,4)
            self.battle_background=pygame.image.load(picture_list[i]).convert()


        else:
            self.battle_background=pygame.image.load("images\\png\\backgrounds\\capital.jpg").convert()

        self.battle_background=pygame.transform.smoothscale(self.battle_background,(width_correction(1920),height_correction(900)))
        self.battle_background_Rect=self.battle_background.get_rect()
        self.battle_background_Rect.left=0
        self.battle_background_Rect.top=0
        screen.blit(self.battle_background,self.battle_background_Rect)


    def set_next_attack(self):
        self.attack_time=random.randint(600,750)     #2 min -2 min 30 secunde
        #pt testari punem un minut
        self.attack_time=300   #60 de cicluri pt 12 secunde=> 300 cicluri/min (doar ca jocul incetineste cand avem multi muncitori, deci vom pune cca 250 cicluri/min)


    def __init__(self,army_list):
        self.enemy_army_list=list()
        self.enemy_army_list_at_start=list()
        self.enemy_acc_damage=list()
        self.your_army_list=list()
        self.your_army_list_at_start=list() 
        self.your_acc_damage=list()          #daca un soldat nu a fost omorat dintr-o singura runda, dar a primit damage, acesta se stocheaza aici
        self.bonus_list=list()    #lista de bonusuri: [0] -[4] booze, 5-9->gold 10-12 ->ladies  13-> land  14-> titles



        self.set_next_attack()
        self.enemy_army_list_at_start=copy.deepcopy(army_list)
        self.enemy_army_list_at_start[0].nr=10
        self.enemy_army_list_at_start[1].nr=2
        self.enemy_army_list=copy.deepcopy(self.enemy_army_list_at_start)

        self.button_list=list()
        self.booze_button=Button(name="Throw in booze",color=red,corner=(1750,100),width=40,height=40,can_click=False,image="images\\png\\buttons\\booze.png")    #initializam butoanele  #0
        self.button_list.append(self.booze_button)
        self.gold_button=Button(name="Throw in gold",color=red,corner=(1750,200),width=40,height=40,can_click=False,image="images\\png\\buttons\\gold.png")                              #1
        self.button_list.append(self.gold_button)
        self.ladies_button=Button(name='Throw in "ladies"',color=red,corner=(1750,300),width=40,height=40,can_click=False,image="images\\png\\buttons\\ladies1.png")                        #2
        self.button_list.append(self.ladies_button)
        self.land_button=Button(name='Promise land',color=red,corner=(1750,400),width=40,height=40,can_click=False,image="images\\png\\buttons\\land.jpg")                               #3
        self.button_list.append(self.land_button)
        self.titles_button=Button(name='Promise titles',color=red,corner=(1750,500),width=40,height=40,can_click=False,image="images\\png\\buttons\\titles.png")                           #4
        self.button_list.append(self.titles_button)

        self.rabble_button=Button(name='Get more Rabble in there',color=red,corner=(1750,600),width=40,height=40,can_click=False,image="images\\png\\buttons\\rabble.png")                 #5
        self.button_list.append(self.rabble_button)
        self.militia_button=Button(name='Get more Militia in there',color=red,corner=(1750,700),width=40,height=40,can_click=False,image="images\\png\\buttons\\militia.png")               #6
        self.button_list.append(self.militia_button)
        self.archers_button=Button(name='Get more Archers in there',color=red,corner=(1750,800),width=40,height=40,can_click=False,image="images\\png\\buttons\\archer.png")               #7
        self.button_list.append(self.archers_button)

        self.retreat_button=Button(name='RETREAT!',color=white,corner=(1733,940),width=74,height=74,image="images\\png\\buttons\\retreat.png")                              #8
        self.button_list.append(self.retreat_button)

        self.rectangle_list=list()  #o lista de dreptungiuri ce nu sunt butoane (chiar daca sunt facute cu aceeasi clasa)
        self.enemy_retreat=Button(name='RETREAT!',color=white,corner=(87,940),width=74,height=74,image="images\\png\\buttons\\enemy_retreat.png")
        self.rectangle_list.append(self.enemy_retreat)

        self.morale=Morale()           #initializam moralul

        for i in range(0,40):                #initializam listele de accumulated damage cu zero
            self.your_acc_damage.append(0)
            self.enemy_acc_damage.append(0)

        for i in range(0,15):                #initializam lista de bonusuri cu zero
            self.bonus_list.append(0)

    def erase_button(self,i):
        screen.blit(self.battle_background,self.button_list[i].rect,self.button_list[i].rect)

    def calculateHP(self,army_list,acc_damage):
        total_HP=0
        for soldier in army_list:
            total_HP+=soldier.nr*soldier.HP

        actual_HP=total_HP
        for damage in acc_damage:
            actual_HP-=damage
        if actual_HP<0:
            actual_HP=0
        return (total_HP,actual_HP) #returnam HP-ul daca toti cei vii nu ar fi raniti si HP-ul real, ce tine cont de raniti
    
    def calculateAttack(self,army_list,you=False):
        average_attack=0
        total_nr=0
        for soldier in army_list:
            total_nr+=soldier.nr
            average_attack+=soldier.nr*soldier.attack
        if total_nr==0:
            return(0,0,0)
        average_attack=average_attack/total_nr

        if you==True:     #in cazul jucatorului, trebuie sa adaugam bonusuri
            for i in range(0,15):
                if self.bonus_list[i]>0:
                    if i<5:
                        average_attack+=0.3
                    elif i<10:
                        average_attack+=0.4
                    elif i<13:
                        average_attack+=0.2
                    elif i==13:
                        average_attack+=1
                    elif i==14:
                        average_attack+=2
        min_attack=round(average_attack*0.75,2)
        max_attack=round(average_attack*1.5,2)
        average_attack=round(average_attack,2)
        return(min_attack,average_attack,max_attack)


    def insert_army_stats(self,who,what):
        font = pygame.font.SysFont('georgia', self.text_size)
        if who=='you'or who==1:
            self.your_strength=self.calculateHP(self.your_army_list,self.your_acc_damage)
            self.your_attack=self.calculateAttack(self.your_army_list,you=True)

            if what=="HP" or what==1:
                text = font.render(f'Your army strength:{str(correct_big_nr(int(self.your_strength[1])))}', True, green, blue)  #afisam HP-ul cu raniti
                self.your_str_Rect = text.get_rect()
                self.your_str_Rect.center=(width_correction(1400),height_correction(50))
                screen.blit(text, self.your_str_Rect) 
            
            elif what=="damage" or what==2:
                self.your_min_damage=round(self.your_attack[0]*self.your_strength[0]/100,2)   #damage-ul se calculeaza din primul strength
                self.your_max_damage=round(self.your_attack[2]*self.your_strength[0]/100,2)
                text = font.render(f'Damage:{correct_big_nr(self.your_min_damage)} - {correct_big_nr(self.your_max_damage)}', True, green, blue)
                self.your_damage_Rect = text.get_rect()
                self.your_damage_Rect.center=(width_correction(1400),height_correction(100))
                screen.blit(text, self.your_damage_Rect) 

            elif what=="atack" or what==3:
                text = font.render(f'({self.your_attack[0]}% - {self.your_attack[2]}% of army STR)', True, green, blue)
                self.your_attack_Rect = text.get_rect()
                self.your_attack_Rect.center=(width_correction(1400),height_correction(150))
                screen.blit(text, self.your_attack_Rect)

            elif what=="funds" or what==4:
                text = font.render(f'Funds: {correct_big_nr(self.your_war_funds)}', True, green, blue)
                self.your_funds_Rect = text.get_rect()
                self.your_funds_Rect.center=(width_correction(1400),height_correction(200))
                screen.blit(text, self.your_funds_Rect)

        elif who=='enemy'or who==2:
            self.enemy_strength=self.calculateHP(self.enemy_army_list,self.enemy_acc_damage)
            self.enemy_attack=self.calculateAttack(self.enemy_army_list)

            if what=="HP" or what==1:
                text = font.render(f'Enemy army strength: {str(correct_big_nr(int(self.enemy_strength[1])))}', True, green, blue)
                self.enemy_str_Rect = text.get_rect()
                self.enemy_str_Rect.center=(width_correction(400),height_correction(50))
                screen.blit(text, self.enemy_str_Rect) 
            
            elif what=="damage" or what==2:
                self.enemy_min_damage=round(self.enemy_attack[0]*self.enemy_strength[0]/100,2)
                self.enemy_max_damage=round(self.enemy_attack[2]*self.enemy_strength[0]/100,2)
                text = font.render(f'Damage:{correct_big_nr(self.enemy_min_damage)} - {correct_big_nr(self.enemy_max_damage)}', True, green, blue)
                self.enemy_damage_Rect = text.get_rect()
                self.enemy_damage_Rect.center=(width_correction(400),height_correction(100))
                screen.blit(text, self.enemy_damage_Rect) 

            elif what=="atack" or what==3:
                text = font.render(f'({self.enemy_attack[0]}% - {self.enemy_attack[2]}% of army STR)', True, green, blue)
                self.enemy_attack_Rect = text.get_rect()
                self.enemy_attack_Rect.center=(width_correction(400),height_correction(150))
                screen.blit(text, self.enemy_attack_Rect)  

    def erase_army_stats(self,who,what):
        font = pygame.font.SysFont('georgia', self.text_size)                  #erase old score
        if who=='you'or who==1:
            if what=="HP" or what==1:
                screen.blit(self.battle_background, self.your_str_Rect, self.your_str_Rect) 
            
            elif what=="damage" or what==2:
                screen.blit(self.battle_background, self.your_damage_Rect, self.your_damage_Rect) 

            elif what=="atack" or what==3:
                screen.blit(self.battle_background, self.your_attack_Rect, self.your_attack_Rect)

            elif what=="funds" or what==4:
                screen.blit(self.battle_background, self.your_funds_Rect, self.your_funds_Rect)

        elif who=='enemy'or who==2:
            if what=="HP" or what==1:
                screen.blit(self.battle_background, self.enemy_str_Rect, self.enemy_str_Rect) 
            
            elif what=="damage" or what==2:
                screen.blit(self.battle_background, self.enemy_damage_Rect, self.enemy_damage_Rect) 

            elif what=="attack" or what==3:
                screen.blit(self.battle_background, self.enemy_attack_Rect, self.enemy_attack_Rect) 


    def begin(self,army_list,cash):
        self.victory=-1                                                       #setam valoarea de victory la -1
        self.your_war_funds=cash
        self.your_army_list=copy.deepcopy(army_list)
        self.your_army_list_at_start=copy.deepcopy(army_list)
        for i in range(0,len(self.your_army_list)):
            self.your_acc_damage[i]=0
            self.enemy_acc_damage[i]=0
        self.your_strength_at_start=self.calculateHP(self.your_army_list,self.your_acc_damage)  #calculam HP-ul la inceputul bataliei
        self.enemy_strength_at_start=self.calculateHP(self.enemy_army_list_at_start,self.enemy_acc_damage)  #calculam HP-ul dusmanului la inceputul bataliei

        for i in range(1,3):
            for j in range(1,4):
                self.insert_army_stats(i,j)
        self.insert_army_stats(1,4)

        for i in range(3,5):
            self.bonus_list[i+10]=0
            self.button_list[i].not_used=True

        for i in range(5,8):
            self.button_list[i].not_used=True

        for button in self.button_list:   #desenam butoanele
            button.draw()
            button.insert_name()

        for bonus in self.bonus_list:
            bonus=0
        
        for r in self.rectangle_list:   #desenam dreptunghiurile
            r.draw()

        self.morale.draw()
        self.morale.draw_your_morale()
        self.morale.draw_enemy_morale()

        self.turn=random.randint(1,2)       #determinam cine incepe primul
        self.battle_start_time=time.time()  #determinam cand a inceput lupta

        #afisam armata dusmana(cu scop de testare):
        print("Battle nr: ",self.battle_nr)
        for i in range(0,len(self.enemy_army_list_at_start)):
            if self.enemy_army_list_at_start[i].nr>0:
                print(self.enemy_army_list_at_start[i].name," nr= ",self.enemy_army_list_at_start[i].nr,' HP= ',self.enemy_army_list_at_start[i].HP,
                ' attack= ',self.enemy_army_list_at_start[i].attack,' defense= ',self.enemy_army_list_at_start[i].defense,
                'times upgraded= ',self.enemy_army_list_at_start[i].times_upgraded)
        print()



    def distribute_damage(self,damage,army_list,acc_damage,you=False):             #functia care distribuie damage-ul unei armate in mod inegal in armata dusmana
        bonus=0
        if you==True:
            for i in range(0,len(self.bonus_list)):
                if self.bonus_list[i]>0:
                    if i<5:
                        bonus-=1.2
                    elif i<10:
                        pass
                    elif i<13:
                        bonus+=2.5
                    elif i==13:
                        bonus+=10
                    elif i==14:
                        bonus+=30

        nr_categorii=0                       #cate tipuri de soldati exista in acea armata
        for soldier in army_list:
            if soldier.nr>0 and soldier.name!="Engineer" and soldier.name!="Builder":
                nr_categorii+=1
        for i in range(0,len(army_list)):
            if nr_categorii==0:
                break
            if army_list[i].nr>0 and army_list[i].name!="Engineer" and army_list[i].name!="Builder":
                if nr_categorii>1:
                    soldier_damage=damage/nr_categorii
                    distribution_factor=random.choice([0,0.25,0.33,0.5,0.66,0.75,1,1.25,1.5,1.75,2,2.5,3])
                    soldier_damage*=distribution_factor
                    damage=damage-soldier_damage
                    soldier_damage=soldier_damage-(soldier_damage* (army_list[i].defense+bonus))/100 + acc_damage[i]
                    victims=soldier_damage/army_list[i].HP
                    killed=int(victims)
                    army_list[i].nr=army_list[i].nr-killed
                    if army_list[i].nr<0:
                        army_list[i].nr=0
                    acc_damage[i]=(victims-killed)*army_list[i].HP
                    nr_categorii-=1

                elif nr_categorii==1:
                    soldier_damage=damage-(damage*(army_list[i].defense+bonus))/100 + acc_damage[i]
                    victims=soldier_damage/army_list[i].HP
                    killed=int(victims)
                    army_list[i].nr=army_list[i].nr-killed
                    if army_list[i].nr<0:
                        army_list[i].nr=0
                    acc_damage[i]=(victims-killed)*army_list[i].HP
                    nr_categorii-=1

                

    def attack(self):
        if self.turn==1:  #cand e randul jucatorului
            if self.your_strength[1]<=0.25*self.your_strength_at_start[0]:    #daca ai pierdut mai mult de 3/4 din efectiv:
                self.victory=2                                               #castiga dusmanul
                return

            self.turn=2   #schimbam tura
            damage=random.uniform(self.your_min_damage,self.your_max_damage)         #calculam damage-ul pe care il face jucatorul
            self.distribute_damage(damage,self.enemy_army_list,self.enemy_acc_damage)  #il distribuim in armata dusmana
            self.erase_army_stats(2,1)
            self.erase_army_stats(2,2)
            self.erase_army_stats(2,3)
            self.insert_army_stats(2,1)
            self.insert_army_stats(2,2)
            self.insert_army_stats(2,3)



        
        elif self.turn==2: #cand e randul dusmanului
            if self.enemy_strength[1]<=0.25*self.enemy_strength_at_start[0]:   #daca dusmanul a pierdut mai mult de 3/4 din efectiv:
                self.victory=1                                                #a castigat jucatorul
                return

            self.turn=1
            damage=random.uniform(self.enemy_min_damage,self.enemy_max_damage)        #calculam damage-ul pe care il face dusmanul
            self.distribute_damage(damage,self.your_army_list,self.your_acc_damage,you=True)   #il distribuim in armata ta
            self.erase_army_stats(1,1)
            self.erase_army_stats(1,2)
            self.erase_army_stats(1,3)
            self.insert_army_stats(1,1)
            self.insert_army_stats(1,2)
            self.insert_army_stats(1,3)


    def modify_morale(self):
        if self.enemy_strength[1]*1.5<self.your_strength[1]:                     #daca armata ramasa a dusmanului e de 2 ori mai mica decat a jucatorului
            self.morale.lower_enemy_morale(math.ceil(self.your_strength[1]/(self.enemy_strength[1]*3)))   #dusmanul pierde moral
            self.morale.draw_enemy_morale()

        if self.your_strength[1]*1.5<self.enemy_strength[1] and (self.bonus_list[10]==0 or self.bonus_list[11]==0 or self.bonus_list[12]==0):                 #daca armata ta ramasa e de 2 ori mai mica decat a dusmanului
            nr=self.your_strength[1]
            if nr==0:
                nr=1
            self.morale.lower_your_morale(math.ceil(self.enemy_strength[1]/(nr*2)))     #pierzi moral
            self.morale.draw_your_morale()

    def select_best_unit(self):
        tier_list=["Rabble","Militia","Archer","Axeman",'Spearman','Crossbowman','Ballista','Maceman','Pikeman','Catapult','Warhammer','Swordsman','Light Cav.'
        ,'Arbalest','Heavy Cav.','Musketeer','Cannon']
        for i in range(1, len(tier_list)-1):
            if self.enemy_best_unit==tier_list[i]:
                self.enemy_best_unit=tier_list[i+1]
                break

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


    def upgrade(self,nr):                #upgrade pt dusman

        '''
        <situatiile particulare per soldat>
        '''
        upgrade_list=self.select_upgrade_list(nr)

        list_poz=self.enemy_army_list_at_start[nr].times_upgraded % len(upgrade_list)
        what=upgrade_list[list_poz]
        if what=="HP":
            self.enemy_army_list_at_start[nr].HP+=self.enemy_army_list_at_start[nr].hp_upg
        elif what=="AT":
            self.enemy_army_list_at_start[nr].attack+=self.enemy_army_list_at_start[nr].at_upg
        elif what=="DEF":
            self.enemy_army_list_at_start[nr].defense+=self.enemy_army_list_at_start[nr].def_upg
        elif what=="S":
            self.enemy_army_list_at_start[nr].siege+=self.enemy_army_list_at_start[nr].siege_upg

        if nr==7:                       #cand avem Spearman, trebuie sa dam upgrade si pt Pikeman:
            if what=="HP":
                self.enemy_army_list_at_start[8].HP+=self.enemy_army_list_at_start[8].hp_upg      #Pikeman e pe pozitia 8
            elif what=="AT":
                self.enemy_army_list_at_start[8].attack+=self.enemy_army_list_at_start[8].at_upg
            elif what=="DEF":
                self.enemy_army_list_at_start[8].defense+=self.enemy_army_list_at_start[8].def_upg
            self.enemy_army_list_at_start[8].times_upgraded+=1
        '''
        </situatiile particulare per soldat>
        '''

        self.enemy_army_list_at_start[nr].times_upgraded+=1
        if self.enemy_army_list_at_start[nr].times_upgraded==self.enemy_army_list_at_start[nr].maximum_upgrades:
            self.enemy_army_list_at_start[nr].can_be_upgraded=False


    def end(self):                    #functia de sfarsit pregateste dusmanul urmator

        self.battle_nr+=1             #incrementam nr bataliei
        lungime=len(self.enemy_army_list_at_start)

        if self.battle_nr%2==0:             #pregatim urmatorul tip de soldat ce va fi adaugat armatei dusmane
            self.select_best_unit()

        for i in range(0,lungime):   #crestem armata
            if self.enemy_army_list_at_start[i].nr>0:
                self.enemy_army_list_at_start[i].nr=math.ceil(self.enemy_army_list_at_start[i].nr*1.2)    #crestem nr de soldati cu 20%

            elif self.battle_nr%2==0 and self.enemy_army_list_at_start[i].name==self.enemy_best_unit:
                self.enemy_army_list_at_start[i].nr=1

        #facem upgrade-uri armatei:

        nr_categorii=0                       #cate tipuri de soldati exista in acea armata
        for soldier in self.enemy_army_list_at_start:
            if soldier.nr>0 and soldier.can_be_upgraded==True:
                nr_categorii+=1

        nr_upgrades=math.ceil(1.5*nr_categorii)   #stabilim cate upgrades vom face in aceasta tura

        can_upgrade=list()                        #o lista cu indicii soldatilor(in lista armatei dusmane) ce pot primi upgrade
        for i in range(1,lungime):
            if self.enemy_army_list_at_start[i].nr>0 and self.enemy_army_list_at_start[i].can_be_upgraded:
                can_upgrade.append(i)

        while nr_upgrades>0:
            who=random.choice(can_upgrade)        #alegem random cui ii facem upgrade-uri
            if self.enemy_army_list_at_start[who].nr>0 and self.enemy_army_list_at_start[who].can_be_upgraded:
                nr_upgrades-=1
                self.upgrade(who)


        self.enemy_army_list=copy.deepcopy(self.enemy_army_list_at_start)

        self.morale.your_morale=100
        self.morale.enemy_morale=100            #resetam moralul

        return self.your_war_funds


    def check_for_buttons(self):                #functia determina daca anumite butoane pot sau nu sa fie apasate (in functie de costuri)
        #pt cele de booze,gold...titles, calculam costul pe trupe:
        cost=self.your_army_list[0].nr+self.your_army_list[1].nr*2+self.your_army_list[2].nr*3+self.your_army_list[6].nr*4+self.your_army_list[7].nr*4
        cost+=self.your_army_list[3].nr*6+ self.your_army_list[11].nr*11+ self.your_army_list[13].nr*14+self.your_army_list[18].nr*14+self.your_army_list[12].nr*7
        cost+=self.your_army_list[8].nr*8+self.your_army_list[14].nr*16+self.your_army_list[15].nr*32+self.your_army_list[16].nr*64+self.your_army_list[4].nr*64
        cost+=self.your_army_list[17].nr*128+self.your_army_list[5].nr*128

        if self.your_war_funds>=cost:
            self.booze_button.can_click=True
        else:
            self.booze_button.can_click=False
        if self.your_war_funds>=cost*5:
            self.gold_button.can_click=True
            self.ladies_button.can_click=True
        else:
            self.gold_button.can_click=False
            self.ladies_button.can_click=False
        if self.your_war_funds>=cost*25:
            self.land_button.can_click=True
        else:
            self.land_button.can_click=False
        if self.your_war_funds>=cost*100:
            self.titles_button.can_click=True
        else:
            self.titles_button.can_click=False

        rabble_price=220*(self.your_army_list_at_start[0].nr-self.your_army_list[0].nr)   #daca cumperi Rabble pe teren, pretul e de 4 ori mai mare
        if rabble_price>0 and self.your_war_funds>rabble_price:
            self.rabble_button.can_click=True
        else:
            self.rabble_button.can_click=False

        militia_price=0
        price=2800
        for i in range(1,self.your_army_list_at_start[1].nr+1):
            price*=1.02
            if i>self.your_army_list[1].nr:
                militia_price+=price
        if self.your_war_funds>=militia_price and militia_price>0:
            self.militia_button.can_click=True
        else:
            self.militia_button.can_click=False
        
        archer_price=0
        price=2800
        for i in range(1,self.your_army_list_at_start[2].nr+1):
            price*=1.02
            if i>self.your_army_list[2].nr:
                archer_price+=price
        if self.your_war_funds>=archer_price and archer_price>0:
            self.archers_button.can_click=True
        else:
            self.archers_button.can_click=False

        for b in range(0,len(self.button_list)):
            was_drawn=self.button_list[b].draw()
            if was_drawn==False:
                self.erase_button(b)


    def button_tax(self,nr):
        if nr<=4:
            cost=self.your_army_list[0].nr+self.your_army_list[1].nr*2+self.your_army_list[2].nr*3+self.your_army_list[6].nr*4+self.your_army_list[7].nr*4
            cost+=self.your_army_list[3].nr*6+ self.your_army_list[11].nr*11+ self.your_army_list[13].nr*14+self.your_army_list[18].nr*14+self.your_army_list[12].nr*7
            cost+=self.your_army_list[8].nr*8+self.your_army_list[14].nr*16+self.your_army_list[15].nr*32+self.your_army_list[16].nr*64+self.your_army_list[4].nr*64
            cost+=self.your_army_list[17].nr*128+self.your_army_list[5].nr*128

            if nr==0:   #booze button
                self.your_war_funds-=cost
            elif nr==1 or nr==2:  #gold button and ladies button
                self.your_war_funds=self.your_war_funds-5*cost
            elif nr==3:
                self.your_war_funds=self.your_war_funds-25*cost
            elif nr==4:
                self.your_war_funds=self.your_war_funds-100*cost
        
        elif nr>4:
            if nr==5:
                rabble_price=220*(self.your_army_list_at_start[0].nr-self.your_army_list[0].nr)   #daca cumperi Rabble pe teren, pretul e de 4 ori mai mare
                self.your_army_list[0].nr=self.your_army_list_at_start[0].nr                  #resetam nr de rabble
                self.your_war_funds=self.your_war_funds-rabble_price

            elif nr==6:
                militia_price=0
                price=2800
                for i in range(1,self.your_army_list_at_start[1].nr+1):
                    price*=1.02
                    if i>self.your_army_list[1].nr:
                        militia_price+=price
                        self.your_war_funds=self.your_war_funds-militia_price
                        self.your_army_list[1].nr=self.your_army_list_at_start[1].nr

            elif nr==7:
                archer_price=0
                price=2800
                for i in range(1,self.your_army_list_at_start[2].nr+1):
                    price*=1.02
                    if i>self.your_army_list[2].nr:
                        archer_price+=price
                self.your_war_funds=self.your_war_funds-archer_price
                self.your_army_list[2].nr=self.your_army_list_at_start[2].nr


class Animation:
    def __init__(self):
        self.your_army=pygame.image.load("images\\png\\Battle\\ya.png").convert_alpha()
        self.your_army=pygame.transform.smoothscale( self.your_army,(width_correction(500),height_correction(400)))
        self.enemy_army=pygame.image.load("images\\png\\Battle\\ea.png").convert_alpha()
        self.enemy_army=pygame.transform.smoothscale( self.enemy_army,(width_correction(500),height_correction(400)))

        self.explosion=pygame.image.load("images\\png\\Battle\\explosion.png").convert_alpha()
        self.explosion=pygame.transform.smoothscale( self.explosion,(width_correction(35),height_correction(70)))

    
    def draw_ya(self):
        self.your_army_rect=self.your_army.get_rect()
        self.your_army_rect.center=(width_correction(1400),height_correction(700))
        screen.blit(self.your_army, self.your_army_rect)

    def draw_ea(self):
        self.enemy_army_rect=self.enemy_army.get_rect()
        self.enemy_army_rect.center=(width_correction(320),height_correction(700))
        screen.blit(self.enemy_army, self.enemy_army_rect)

    def erase_ya(self,background):
        screen.blit(background, self.your_army_rect,self.your_army_rect)

    def erase_ea(self,background):
        screen.blit(background, self.enemy_army_rect,self.enemy_army_rect)

    def draw_your_cannonballs(self):
        self.cannonball=pygame.image.load("images\\png\\Battle\\cannonball.png").convert_alpha()
        self.cannonball=pygame.transform.smoothscale(self.cannonball,(width_correction(15),height_correction(15)))
        self.c_rect1=self.cannonball.get_rect()
        self.c_rect2=self.cannonball.get_rect()
        self.c_rect3=self.cannonball.get_rect()
        self.c_rect4=self.cannonball.get_rect()
        self.c_rect5=self.cannonball.get_rect()

        self.c_rect1.center=(width_correction(1400),height_correction(510))
        self.c_rect2.center=(width_correction(1420),height_correction(540))
        self.c_rect3.center=(width_correction(1440),height_correction(580))
        self.c_rect4.center=(width_correction(1460),height_correction(615))
        self.c_rect5.center=(width_correction(1480),height_correction(650))

        screen.blit(self.cannonball, self.c_rect1)
        screen.blit(self.cannonball, self.c_rect2)
        screen.blit(self.cannonball, self.c_rect3)
        screen.blit(self.cannonball, self.c_rect4)
        screen.blit(self.cannonball, self.c_rect5)


    def draw_your_flames(self):
        self.flame=pygame.image.load("images\\png\\Battle\\cannon_flame.png").convert_alpha()
        self.flame=pygame.transform.smoothscale(self.flame,(width_correction(30),height_correction(15)))
        self.f_rect1=self.flame.get_rect()
        self.f_rect2=self.flame.get_rect()
        self.f_rect3=self.flame.get_rect()
        self.f_rect4=self.flame.get_rect()
        self.f_rect5=self.flame.get_rect()

        self.f_rect1.center=(width_correction(1420),height_correction(515))
        self.f_rect2.center=(width_correction(1440),height_correction(545))
        self.f_rect3.center=(width_correction(1460),height_correction(585))
        self.f_rect4.center=(width_correction(1480),height_correction(620))
        self.f_rect5.center=(width_correction(1500),height_correction(655))

        screen.blit(self.flame, self.f_rect1)
        screen.blit(self.flame, self.f_rect2)
        screen.blit(self.flame, self.f_rect3)
        screen.blit(self.flame, self.f_rect4)
        screen.blit(self.flame, self.f_rect5)

    def draw_your_flames_lite(self):
        screen.blit(self.flame, self.f_rect1)
        screen.blit(self.flame, self.f_rect2)
        screen.blit(self.flame, self.f_rect3)
        screen.blit(self.flame, self.f_rect4)
        screen.blit(self.flame, self.f_rect5)

    def erase_your_flames(self,background):
        screen.blit(background,self.f_rect1,self.f_rect1)
        screen.blit(background,self.f_rect2,self.f_rect2)
        screen.blit(background,self.f_rect3,self.f_rect3)
        screen.blit(background,self.f_rect4,self.f_rect4)
        screen.blit(background,self.f_rect5,self.f_rect5)

    def draw_enemy_cannonballs(self):
        self.cannonball=pygame.image.load("images\\png\\Battle\\cannonball.png").convert_alpha()
        self.cannonball=pygame.transform.smoothscale(self.cannonball,(width_correction(15),height_correction(15)))
        self.ec_rect1=self.cannonball.get_rect()
        self.ec_rect2=self.cannonball.get_rect()
        self.ec_rect3=self.cannonball.get_rect()
        self.ec_rect4=self.cannonball.get_rect()
        self.ec_rect5=self.cannonball.get_rect()

        self.ec_rect1.center=(width_correction(320),height_correction(510))
        self.ec_rect2.center=(width_correction(300),height_correction(540))
        self.ec_rect3.center=(width_correction(280),height_correction(580))
        self.ec_rect4.center=(width_correction(260),height_correction(615))
        self.ec_rect5.center=(width_correction(240),height_correction(650))

        screen.blit(self.cannonball, self.ec_rect1)
        screen.blit(self.cannonball, self.ec_rect2)
        screen.blit(self.cannonball, self.ec_rect3)
        screen.blit(self.cannonball, self.ec_rect4)
        screen.blit(self.cannonball, self.ec_rect5)


    def draw_enemy_flames(self):
        self.eflame=pygame.image.load("images\\png\\Battle\\cannon_e_flame.png").convert_alpha()
        self.eflame=pygame.transform.smoothscale(self.eflame,(width_correction(30),height_correction(15)))
        self.ef_rect1=self.eflame.get_rect()
        self.ef_rect2=self.eflame.get_rect()
        self.ef_rect3=self.eflame.get_rect()
        self.ef_rect4=self.eflame.get_rect()
        self.ef_rect5=self.eflame.get_rect()

        self.ef_rect1.center=(width_correction(300),height_correction(515))
        self.ef_rect2.center=(width_correction(280),height_correction(545))
        self.ef_rect3.center=(width_correction(260),height_correction(585))
        self.ef_rect4.center=(width_correction(240),height_correction(620))
        self.ef_rect5.center=(width_correction(220),height_correction(655))

        screen.blit(self.eflame, self.ef_rect1)
        screen.blit(self.eflame, self.ef_rect2)
        screen.blit(self.eflame, self.ef_rect3)
        screen.blit(self.eflame, self.ef_rect4)
        screen.blit(self.eflame, self.ef_rect5)

    def draw_enemy_flames_lite(self):
        screen.blit(self.eflame, self.ef_rect1)
        screen.blit(self.eflame, self.ef_rect2)
        screen.blit(self.eflame, self.ef_rect3)
        screen.blit(self.eflame, self.ef_rect4)
        screen.blit(self.eflame, self.ef_rect5)

    def erase_enemy_flames(self,background):
        screen.blit(background,self.ef_rect1,self.ef_rect1)
        screen.blit(background,self.ef_rect2,self.ef_rect2)
        screen.blit(background,self.ef_rect3,self.ef_rect3)
        screen.blit(background,self.ef_rect4,self.ef_rect4)
        screen.blit(background,self.ef_rect5,self.ef_rect5)


    def erase_cannonballs(self,rects,background):
        for rect in rects:  
            screen.blit(background,rect,rect)
        screen.blit(self.your_army,self.your_army_rect)
        screen.blit(self.enemy_army,self.enemy_army_rect)



    def your_cannon_anim(self,background,useless_string):
        self.draw_your_cannonballs()
        self.draw_your_flames()
        cannonballs=[self.c_rect1,self.c_rect2,self.c_rect3,self.c_rect4,self.c_rect5]
        for j in range(0,20):
            self.erase_cannonballs(rects=[self.c_rect1,self.c_rect2,self.c_rect3,self.c_rect4,self.c_rect5],background=background)
            self.draw_your_flames_lite()
            x=0
            for i in range(0,5):
                y=random.randint(-10,20)
                cannonballs[i].left-=width_correction(50+y)
                if j<10:
                    cannonballs[i].top-=height_correction(10)
                else:
                    cannonballs[i].top+=height_correction(10+int(x/2))
                    x+=5
                screen.blit(self.cannonball,cannonballs[i])
            time.sleep(0.03)
        for i in range(0,5):
            center=cannonballs[i].center
            cannonballs[i]=self.explosion.get_rect()
            cannonballs[i].center=center
            screen.blit(self.explosion,cannonballs[i])
        time.sleep(0.25)
        self.erase_your_flames(background)
        self.erase_cannonballs(cannonballs,background)


    def enemy_cannon_anim(self,background,useless_string):
        self.draw_enemy_cannonballs()
        self.draw_enemy_flames()
        cannonballs=[self.ec_rect1,self.ec_rect2,self.ec_rect3,self.ec_rect4,self.ec_rect5]
        for j in range(0,20):
            self.erase_cannonballs(rects=[self.ec_rect1,self.ec_rect2,self.ec_rect3,self.ec_rect4,self.ec_rect5],background=background)
            self.draw_enemy_flames_lite()
            x=0
            for i in range(0,5):
                y=random.randint(-10,20)
                cannonballs[i].left+=width_correction(50+y)
                if j<10:
                    cannonballs[i].top-=height_correction(10)
                else:
                    cannonballs[i].top+=height_correction(10+int(x/2))
                    x+=5
                screen.blit(self.cannonball,cannonballs[i])
            time.sleep(0.03)
        for i in range(0,5):
            center=cannonballs[i].center
            cannonballs[i]=self.explosion.get_rect()
            cannonballs[i].center=center
            screen.blit(self.explosion,cannonballs[i])
        time.sleep(0.25)
        self.erase_enemy_flames(background)
        self.erase_cannonballs(cannonballs,background)




    def draw_your_arrows(self):
        self.arrow=pygame.image.load("images\\png\\Battle\\fire_arrow1.png").convert_alpha()
        self.arrow=pygame.transform.smoothscale(self.arrow,(width_correction(40),height_correction(40)))
        self.a_rect1=self.arrow.get_rect()
        self.a_rect2=self.arrow.get_rect()
        self.a_rect3=self.arrow.get_rect()
        self.a_rect4=self.arrow.get_rect()
        self.a_rect5=self.arrow.get_rect()
        self.a_rect6=self.arrow.get_rect()
        self.a_rect7=self.arrow.get_rect()
        self.a_rect8=self.arrow.get_rect()
        self.a_rect9=self.arrow.get_rect()
        self.a_rect10=self.arrow.get_rect()
        self.a_rect11=self.arrow.get_rect()
        self.a_rect12=self.arrow.get_rect()

        self.a_rect1.center=(width_correction(1310),height_correction(550))
        self.a_rect2.center=(width_correction(1340),height_correction(580))
        self.a_rect3.center=(width_correction(1360),height_correction(610))
        self.a_rect4.center=(width_correction(1340),height_correction(630))
        self.a_rect5.center=(width_correction(1340),height_correction(650))
        self.a_rect6.center=(width_correction(1390),height_correction(690))
        self.a_rect7.center=(width_correction(1410),height_correction(730))
        self.a_rect8.center=(width_correction(1450),height_correction(720))
        self.a_rect9.center=(width_correction(1480),height_correction(790))
        self.a_rect10.center=(width_correction(1525),height_correction(800))
        self.a_rect11.center=(width_correction(1550),height_correction(800))
        self.a_rect12.center=(width_correction(1590),height_correction(800))

        screen.blit(self.arrow, self.a_rect1)
        screen.blit(self.arrow, self.a_rect2)
        screen.blit(self.arrow, self.a_rect3)
        screen.blit(self.arrow, self.a_rect4)
        screen.blit(self.arrow, self.a_rect5)
        screen.blit(self.arrow, self.a_rect6)
        screen.blit(self.arrow, self.a_rect7)
        screen.blit(self.arrow, self.a_rect8)
        screen.blit(self.arrow, self.a_rect9)
        screen.blit(self.arrow, self.a_rect10)
        screen.blit(self.arrow, self.a_rect11)
        screen.blit(self.arrow, self.a_rect12)


    def your_arrow_anim(self,background,useless_string):
        self.draw_your_arrows()
        arrows=[self.a_rect1,self.a_rect2,self.a_rect3,self.a_rect4,self.a_rect5,self.a_rect6,self.a_rect7,self.a_rect8,self.a_rect9,self.a_rect10,self.a_rect11,self.a_rect12]
        rotated_image=self.arrow
        for j in range(0,20):
            self.erase_cannonballs(rects=arrows,background=background)
            x=0
            rotated_image = pygame.transform.rotate(rotated_image, 5)
            for i in range(0,12):

                left=arrows[i].left
                top=arrows[i].top
                arrows[i]=rotated_image.get_rect()
                arrows[i].left=left
                arrows[i].top=top

                arrows[i].left-=width_correction(50+int(x/2))
                if j<10:
                    arrows[i].top-=height_correction(10)
                else:
                    arrows[i].top+=height_correction(10)
                    x+=5
                screen.blit(rotated_image,arrows[i])
            time.sleep(0.03)
        self.erase_cannonballs(arrows,background)


    def draw_enemy_arrows(self):
        self.earrow=pygame.image.load("images\\png\\Battle\\fire_arrow2.png").convert_alpha()
        self.earrow=pygame.transform.smoothscale(self.earrow,(width_correction(40),height_correction(40)))
        self.ea_rect1=self.earrow.get_rect()
        self.ea_rect2=self.earrow.get_rect()
        self.ea_rect3=self.earrow.get_rect()
        self.ea_rect4=self.earrow.get_rect()
        self.ea_rect5=self.earrow.get_rect()
        self.ea_rect6=self.earrow.get_rect()
        self.ea_rect7=self.earrow.get_rect()
        self.ea_rect8=self.earrow.get_rect()
        self.ea_rect9=self.earrow.get_rect()
        self.ea_rect10=self.earrow.get_rect()
        self.ea_rect11=self.earrow.get_rect()
        self.ea_rect12=self.earrow.get_rect()

        self.ea_rect1.center=(width_correction(410),height_correction(550))
        self.ea_rect2.center=(width_correction(390),height_correction(580))
        self.ea_rect3.center=(width_correction(370),height_correction(610))
        self.ea_rect4.center=(width_correction(390),height_correction(630))
        self.ea_rect5.center=(width_correction(390),height_correction(650))
        self.ea_rect6.center=(width_correction(340),height_correction(690))
        self.ea_rect7.center=(width_correction(320),height_correction(730))
        self.ea_rect8.center=(width_correction(280),height_correction(720))
        self.ea_rect9.center=(width_correction(250),height_correction(790))
        self.ea_rect10.center=(width_correction(205),height_correction(800))
        self.ea_rect11.center=(width_correction(170),height_correction(800))
        self.ea_rect12.center=(width_correction(130),height_correction(800))

        screen.blit(self.earrow, self.ea_rect1)
        screen.blit(self.earrow, self.ea_rect2)
        screen.blit(self.earrow, self.ea_rect3)
        screen.blit(self.earrow, self.ea_rect4)
        screen.blit(self.earrow, self.ea_rect5)
        screen.blit(self.earrow, self.ea_rect6)
        screen.blit(self.earrow, self.ea_rect7)
        screen.blit(self.earrow, self.ea_rect8)
        screen.blit(self.earrow, self.ea_rect9)
        screen.blit(self.earrow, self.ea_rect10)
        screen.blit(self.earrow, self.ea_rect11)
        screen.blit(self.earrow, self.ea_rect12)


    def enemy_arrow_anim(self,background,useless_string):
        self.draw_enemy_arrows()
        arrows=[self.ea_rect1,self.ea_rect2,self.ea_rect3,self.ea_rect4,self.ea_rect5,self.ea_rect6,self.ea_rect7,self.ea_rect8,self.ea_rect9,self.ea_rect10,self.ea_rect11,self.ea_rect12]
        rotated_image=self.earrow
        for j in range(0,20):
            self.erase_cannonballs(rects=arrows,background=background)
            x=0
            rotated_image = pygame.transform.rotate(rotated_image, -5)
            for i in range(0,12):

                left=arrows[i].left
                top=arrows[i].top
                arrows[i]=rotated_image.get_rect()
                arrows[i].left=left
                arrows[i].top=top

                arrows[i].left+=width_correction(50+int(x/2))
                if j<10:
                    arrows[i].top-=height_correction(10)
                else:
                    arrows[i].top+=height_correction(10)
                    x+=5
                screen.blit(rotated_image,arrows[i])
            time.sleep(0.03)
        self.erase_cannonballs(arrows,background)


    def your_cavcharge(self,background,useless_string):
        self.your_cav=pygame.image.load("images\\png\\Battle\\your_cavcharge.png").convert_alpha()
        self.your_cav=pygame.transform.smoothscale(self.your_cav,(width_correction(450),height_correction(150)))
        self.your_cav_Rect=self.your_cav.get_rect()
        self.your_cav_Rect.center=(width_correction(1200),height_correction(815))
        screen.blit(self.your_cav,self.your_cav_Rect)
        time.sleep(0.03)
        for j in range(0,20):
            screen.blit(background,self.your_cav_Rect,self.your_cav_Rect)
            screen.blit(self.your_army,self.your_army_rect)
            screen.blit(self.enemy_army,self.enemy_army_rect)

            self.your_cav_Rect.left-=width_correction(50)
            screen.blit(self.your_cav,self.your_cav_Rect)
            time.sleep(0.03)

        screen.blit(background,self.your_cav_Rect,self.your_cav_Rect)
        screen.blit(self.your_army,self.your_army_rect)
        screen.blit(self.enemy_army,self.enemy_army_rect)


    def enemy_cavcharge(self,background,useless_string):
        self.enemy_cav=pygame.image.load("images\\png\\Battle\\enemy_cavcharge.png").convert_alpha()
        self.enemy_cav=pygame.transform.smoothscale(self.enemy_cav,(width_correction(450),height_correction(150)))
        self.enemy_cav_Rect=self.enemy_cav.get_rect()
        self.enemy_cav_Rect.center=(width_correction(520),height_correction(815))
        screen.blit(self.enemy_cav,self.enemy_cav_Rect)
        time.sleep(0.03)
        for j in range(0,20):
            screen.blit(background,self.enemy_cav_Rect,self.enemy_cav_Rect)
            screen.blit(self.your_army,self.your_army_rect)
            screen.blit(self.enemy_army,self.enemy_army_rect)

            self.enemy_cav_Rect.left+=width_correction(40)
            screen.blit(self.enemy_cav,self.enemy_cav_Rect)
            time.sleep(0.03)

        screen.blit(background,self.enemy_cav_Rect,self.enemy_cav_Rect)
        screen.blit(self.your_army,self.your_army_rect)
        screen.blit(self.enemy_army,self.enemy_army_rect)