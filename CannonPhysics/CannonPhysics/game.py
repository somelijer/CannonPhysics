
import numpy as np
import pygame 
import defs as d
import gameObject as go
import colision as col





def run():
    
    pygame.init()

    screen = pygame.display.set_mode([d.WIDTH, d.HEIGHT])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Cannon physics")

    objects = []
    
    #for i in range(1,4):
    #    circle = go.Circle(d.WIDTH * i / 6 ,d.HEIGHT / 2,i*10)
     #   objects.append(circle)
    
    i = 1
    reck1 = go.Rectangle(d.WIDTH / 2  ,d.HEIGHT * i /3,40 * i,20 * i, np.pi * (i-1)/3)
    objects.append(reck1)

    i = 2
    reck2 = go.Rectangle(d.WIDTH / 2  ,d.HEIGHT * i /3,40 * i,20 * i, np.pi * (i-1)/3)
    objects.append(reck2)
    

    deltaTime = 0

    running = True
    while running:

        # Tera da igrica radi na maksimalno dati broj fps
        deltaTime = clock.tick(d.FPS) / 1000
        print("Lenght of frame: " , deltaTime )
    

        # Kad se zatvori prozor
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bela pozadina
        screen.fill((255, 255, 120))

        
        for o in objects:
            o.move(screen,deltaTime)

        if( col.GJK( reck1.points , reck2.points , reck1.pos * d.PIXEL_PER_METER , reck2.pos * d.PIXEL_PER_METER ) ):
            reck1.colisionColor()
            reck2.colisionColor()
        else:
            reck1.normalColor()
            reck2.normalColor()

        



        #update celog ekrana
        pygame.display.update()


        

    # Done! Time to quit.
    pygame.quit()
