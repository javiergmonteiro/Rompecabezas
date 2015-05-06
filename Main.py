

import pygame
from math import pi
 

pygame.init()
 

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
BROWN = (192, 136,   3)
 

size = [400, 400]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Puzzle")
 

done = False
clock = pygame.time.Clock()

class Bloque(pygame.sprite.Sprite):
	
	def __init__(self, pos,image):
		pygame.sprite.Sprite.__init__(self)
		pieza=pygame.image.load(image)
		self.image = pieza
		self.rect = pieza.get_rect()
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.pos = pos
	
		
posicionesx=[75,139,203,267]
posicionesy=[75,139,203,267]

bloque1=Bloque((75,75),"Piezas/1.png")
bloque2=Bloque((139,75),"Piezas/2.png")	
bloque3=Bloque((203,75),"Piezas/3.png")
bloque4=Bloque((267,75),"Piezas/4.png")
bloque5=Bloque((75,139),"Piezas/5.png")
bloque6=Bloque((139,139),"Piezas/6.png")
bloque7=Bloque((203,139),"Piezas/7.png")
bloque8=Bloque((267,139),"Piezas/8.png")	
bloque9=Bloque((75,203),"Piezas/9.png")
bloque10=Bloque((139,203),"Piezas/10.png")
bloque11=Bloque((203,203),"Piezas/11.png")
bloque12=Bloque((267,203),"Piezas/12.png")
bloque13=Bloque((75,267),"Piezas/13.png")
bloque14=Bloque((139,267),"Piezas/14.png")
bloque15=Bloque((203,267),"Piezas/15.png")


lista=[]
lista.append(bloque1)
lista.append(bloque2)
lista.append(bloque3)
lista.append(bloque4)
lista.append(bloque5)
lista.append(bloque6)
lista.append(bloque7)
lista.append(bloque8)
lista.append(bloque9)
lista.append(bloque10)
lista.append(bloque11)
lista.append(bloque12)
lista.append(bloque13)
lista.append(bloque14)
lista.append(bloque15)


	



imagenplaneta=pygame.image.load("planeta-tierra.jpg")



while not done:
 
    
    clock.tick(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True
             
    
	screen.fill(WHITE)
	
	screen.blit(bloque1.image,bloque1.pos)
	screen.blit(bloque2.image,bloque2.pos)
	screen.blit(bloque3.image,bloque3.pos)
	screen.blit(bloque4.image,bloque4.pos)
	screen.blit(bloque5.image,bloque5.pos)
	screen.blit(bloque6.image,bloque6.pos)
	screen.blit(bloque7.image,bloque7.pos)
	screen.blit(bloque8.image,bloque8.pos)
	screen.blit(bloque9.image,bloque9.pos)
	screen.blit(bloque10.image,bloque10.pos)
	screen.blit(bloque11.image,bloque11.pos)
	screen.blit(bloque12.image,bloque12.pos)
	screen.blit(bloque13.image,bloque13.pos)
	screen.blit(bloque14.image,bloque14.pos)
	screen.blit(bloque15.image,bloque15.pos)
	
	rectangulo=pygame.draw.rect(screen, BROWN, [74,74,256,257], 5)
	
	
    
   
    pygame.display.flip()
 

pygame.quit()
