
import numpy as np
import pygame 
import defs as d
import gameObject as go
import colision as col
import tests as test





def run():
    
    pygame.init()

    screen = pygame.display.set_mode([d.WIDTH, d.HEIGHT])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Cannon physics")
    '''
    objects = test.testStaticCircles()
    objects = test.testCircleOnCircle()
    objects = test.testSquareAndCircles()
    objects = test.testSquares()
    objects = test.testSquares2()
    objects = test.testCannon()
    objects = test.testCircleOnCircle2()
    
    ''' 
    objects = test.testCircleOnCircle()
    
    
    
    

    deltaTime = 0

    if(d.SLOW_MODE == False):
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
        
            col.colisionCheckClassic(objects)

        

        



            #update celog ekrana
            pygame.display.update()
    else:
        running = True
        while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if (pygame.key.get_pressed()[pygame.K_SPACE] == True):
                        
                        deltaTime = 0.02
                        print("Lenght of frame: " , deltaTime )
    

                        # Kad se zatvori prozor
                

                        # Bela pozadina
                        screen.fill((255, 255, 120))

        
                        for o in objects:
                            o.move(screen,deltaTime)
        
                        col.colisionCheckClassic(objects)

        

        



                        #update celog ekrana
                        pygame.display.update()

               


        

    # Done! Time to quit.
    pygame.quit()
