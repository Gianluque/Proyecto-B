import pygame
from pygame.locals import *
import os
import sys
import serial
import binascii


print(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))


puerto = serial.Serial(port='COM8', baudrate=115200,bytesize=serial.EIGHTBITS,timeout=10 )


try:
    puerto.isOpen()
    print("Puerto abierto.")
except:
   exit()


pygame.init()

win = pygame.display.set_mode((800,350))
pygame.display.set_caption('API_1')

class player (object):
    def __init__ (self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumpCount = 0
        self.moveCount = 0
        self.hitbox = (self.x+4,self.y+10,90,40)
    def draw(self,win):
        if self.moveCount +1 >= 7:
            self.moveCount = 0
        if keys [pygame.K_SPACE] and u == 1 and self.y > vel :
            win.blit(up[self.moveCount//3],(self.x,self.y))
            self.moveCount += 1
        else:
            win.blit(fly[self.moveCount//3],(self.x,self.y))
            self.moveCount += 1
        self.hitbox = (self.x+4,self.y+10,90,40)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
    def hit(self):
        run = False



#print(os.getcwd()) 
x = 50
y = 50
width = 96
height = 64
vel = 5
facing = 1
score = 0
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius 
        self.color = color
        self.facing = facing
        self.vel = 15*facing
        self.hitbox = (self.x,self.y)
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.hitbox = (self.x,self.y)
        #pygame.draw.circle(win,(255,0,0),(self.hitbox[0],self.hitbox[1]),self.radius,1)
        #pygame.draw.circle(win, (255,0,0), (self.x,self.y), 3, 1)


class obstacle(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius 
        self.color = color
        self.facing = facing
        self.vel = -10*facing
        self.hitbox = (self.x,self.y)
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.hitbox = (self.x,self.y)
        #pygame.draw.circle(win,(255,0,0),(self.hitbox[0],self.hitbox[1]),self.radius,1)
    def hit(self):
        print(score)



def serialGet(port):
    
    array=[]
    if port.isOpen:
        #puerto.flushInput()
        i=10
        while i:
            array.append(format(ord(port.read()), 'b'))
            i=i-1

    mask = 100000000

    for x in (0,1,2,3,4,5,6,7,8,9):
        aux1=int(array[x])
        aux2=mask+aux1
        array[x]=format(aux2)


    i=0
    j=1
    while j:
        aux = array[i]

        if not (aux[:2]=="10"):
            i+=1
            
        else:
            j=0

    a=array[i]
    i+=1
    b=array[i]
    i+=1
    c=array[i]
    i+=1
    d=array[i]
    i+=1
    e=array[i]

    ch1 = e[5] + a[-7:] + e[6] + b[-7:]

    ch2 = e[7] + c[-7:] + e[8] + d[-7:]

    d1 = e[2]
    d2 = e[3]
    dig1=int(d1)
    dig2=int(d2)
    jump=int(ch1,2)
    shoot=int(ch2,2)
    print(jump)
    #print(shoot)

    return(jump,shoot,dig1,dig2)



regular = [pygame.image.load(os.path.join('images', 'tile000.png')),pygame.image.load(os.path.join('images', 'tile001.png')),pygame.image.load(os.path.join('images', 'tile002.png')),pygame.image.load(os.path.join('images', 'tile003.png')), pygame.image.load(os.path.join('images', 'tile004.png')),pygame.image.load(os.path.join('images', 'tile005.png'))]
up = [pygame.image.load(os.path.join('images','up0.png')), pygame.image.load(os.path.join('images','up1.png')), pygame.image.load(os.path.join('images','up2.png')), pygame.image.load(os.path.join('images','up3.png')), pygame.image.load(os.path.join('images','up4.png')), pygame.image.load(os.path.join('images','up5.png'))]

music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

isJump = False
moveCount = 0
jumpCount = 0
u = 1
neg = -1
bg = pygame.image.load(os.path.join('images','background2.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()
keys = pygame.key.get_pressed()



fly = [pygame.image.load(os.path.join('images','tile000.png')).convert(), pygame.image.load(os.path.join('images','tile001.png')), pygame.image.load(os.path.join('images','tile002.png')), pygame.image.load(os.path.join('images','tile003.png')), pygame.image.load(os.path.join('images','tile004.png')), pygame.image.load(os.path.join('images','tile005.png')), pygame.image.load(os.path.join('images','tile006.png')), pygame.image.load(os.path.join('images','tile007.png'))]
up = [pygame.image.load(os.path.join('images','up0.png')), pygame.image.load(os.path.join('images','up1.png')), pygame.image.load(os.path.join('images','up2.png')), pygame.image.load(os.path.join('images','up3.png')), pygame.image.load(os.path.join('images','up4.png')), pygame.image.load(os.path.join('images','up5.png')), pygame.image.load(os.path.join('images','up4.png')), pygame.image.load(os.path.join('images','up5.png'))]



def redrawWindow():
    global moveCount
    win.blit(bg,(bgX,0))
    win.blit(bg,(bgX2,0))
    ship.draw(win)
    text = font.render('Score: '+ str(score), 1, (255, 255, 255))
    
    for bullet in bullets:
        bullet.draw(win)
    for stone in stones:
        stone.draw(win)
    win.blit(text,(600,30))

    
    pygame.display.update()


while True:
    clock.tick(27)
    score = 0
    speed = 60
    run = True
    jc = 10 

    ship = player(50,100,96,64)
    bullets = []

    stones = []
    stoneLoop=0


    #mainLoop
    font = pygame.font.SysFont('comicsans',30,True)
    while run :
        clock.tick(27)
        if stoneLoop >= 0:
            stoneLoop +=1
        if stoneLoop >10:
            stoneLoop =0    


        #PAUSELOOP    


        for bullet in bullets:
        
            
            for stone in stones:
                if bullet.y - bullet.radius >stone.y-stone.radius and bullet.y + bullet.radius < stone.y + stone.radius:
                    #print('hit yyyyy')
                    if bullet.x + bullet.radius >stone.x-stone.radius:
                        #print('hitx1')
                        #hitSound.play()
                        
                        #score +=1
                        #print('x2')
                        if bullet.x<800+bullet.radius and stone.x-stone.radius<850:
                            stone.hit()
                            bullets.pop(bullets.index(bullet))
                            #print('bulletpop')
                            stones.pop(stones.index(stone))
                            score += 1
                            #print('stonepop')

            if bullet.x <800:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        for stone in stones:
            if stone.x-stone.radius < ship.hitbox[0]+90 and stone.x+stone.radius>ship.hitbox[0] :
                '''
                #pygame.time.delay(1000)
                #print('ship x=')
                #print(ship.hitbox[0])
                print('ship y=')
                print(ship.hitbox[1])
                #print('stone x=')
                #print(stone.x)
                print('stone y=')
                print(stone.y)
                print('stone.radius=')
                print(stone.radius)
                '''




                #print(ship.hitbox[0]+90'>>>'stone.x-stone.radius 'and'ship.hitbox[0]+90-96 '<<<'stone.x+stone.radius)  
                
                if stone.y+stone.radius>ship.hitbox[1] and stone.y -stone.radius<ship.hitbox[1]+45:
                    '''
                    print('hity')
                    print(stone.y+stone.radius)
                    print('>')
                    print(ship.hitbox[1])
                    print ('and')
                    print(stone.y-stone.radius)
                    print('<')
                    print(ship.hitbox[1]+45)
                    '''
                    #ship.hit()
                    #pygame.time.delay(1000)
                    run = False



            if stone.x >0:
                    stone.x += stone.vel
            else:
                stones.pop(stones.index(stone))



        redrawWindow()
        keys = pygame.key.get_pressed()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
        

        #SERIALINPUTDECONTROLES
        shoot=0
        jump=0
        enter=0
        select=0

        (shoot,jump,enter,select)=serialGet(puerto)

        






        #A CAMBIAR POR SERIAL INPUT
        if jump>=2:
            ship.jumpCount = 40
            if ship.y > 0 +20:
                
                if ship.jumpCount == 0:
                    ship.jumpCount = 40

                if ship.jumpCount >= 0:
                    ship.y -= (ship.jumpCount+50) * 0.5
                    ship.jumpCount -= 1

        if shoot>=1:
            if len(bullets) < 70:
                bullets.append(projectile(round(ship.x+ship.width//2+31), round(ship.y + ship.height//2+7), 3, (255, 247, 80),facing))       

        if ship.y < 350 - 70:                                
            ship.y += 10
        
        if len(stones) < 0 and stoneLoop == 0:
                stones.append(obstacle(round(900), round(ship.y + ship.height//2+7), 9, (4, 4, 247),facing))       
        
            

        bgX -= 1.4
        bgX2 -= 1.4

        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        #PAUSELOOP
        while enter == 1:
                shoot=0
                jump=0
                enter=0
                select=0
                (shoot,jump,enter,select)=serialGet(puerto)

        #EXITCOND
        if select==1:
            run=False

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()

    font = pygame.font.SysFont('comicsans',80,True)
    run=True
    while run:
        shoot=0
        jump=0
        enter=0
        select=0
                
        #print('sss')
        win.blit(bg,(bgX,0))
        win.blit(bg,(bgX2,0))
        
        text = font.render('Score: '+ str(score), 1, (255, 255, 255))
        Restart = font.render('RESTART:ENTER\nEXIT:SELECT ', 1, (255, 255, 255))
        (shoot,jump,enter,select)=serialGet(puerto)
        win.blit(text,(350,175))
        win.blit(Restart,(100,100))
        if select == 1:
            run=False
        
        if enter ==1:
            break

        


        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False


    if run==False:
        break
    clock.tick(speed)


