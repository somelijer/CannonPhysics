
import numpy as np
import pygame 
import defs as d
import gameObject as go
import colision as col
import tests as test



def run():
    
    pygame.init()

    screen = pygame.display.set_mode([d.WIDTH, d.HEIGHT])
    pygame.display.set_caption("Cannon physics")

    tests = []
    t = test.testStaticCirclesOnGround
    tests.append(t)
    t = test.testCircleOnCircle
    tests.append(t)
    t = test.testSquareAndCircles
    tests.append(t)
    t = test.testCircleOnCircle
    tests.append(t)
    t = test.testSquares
    tests.append(t)
    t = test.testSquares2
    tests.append(t)
    t = test.testCannon
    tests.append(t)
    t = test.testCircleOnCircle2
    tests.append(t)
    t = test.testLotsOfCircles
    tests.append(t)
    t = test.testLotsOfCircles2
    tests.append(t)
    t = test.testPointDetection
    tests.append(t)
    t = test.testPolyCirc
    tests.append(t)
    t = test.testDroppingReck
    tests.append(t)
    
    
    
    
    i = 0
    objects = tests[i]().copy()
    running = True
    clock = pygame.time.Clock()
    while(running):

        toggle = True
        for event in pygame.event.get():

            screen.fill((255, 255, 120))
            for o in objects:
                o.move(screen,0.00001)
            font = pygame.font.Font(pygame.font.get_default_font(), 20)
            text = font.render("pocetak -> SPACE | Drugi test -> LEFT/RIGHT | Slow mode -> S | Colision -> C", True,(0, 0, 0))
            slm = "Slow mode: " + ( "ON" if d.SLOW_MODE else "OFF")
            text2 = font.render(slm, True,(0, 0, 0))
            col = "Colision: " + ( "OFF" if d.COLISION_OFF else "ON")
            text3 = font.render(col, True,(0, 0, 0))

            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect.center = (d.WIDTH / 2, 30)
            textRect2.center = (d.WIDTH / 4,d.HEIGHT - 30)
            textRect3.center = (d.WIDTH *3/ 4,d.HEIGHT - 30)

            screen.blit(text, textRect)
            screen.blit(text2, textRect2)
            screen.blit(text3, textRect3)
            pygame.display.update()



            if event.type == pygame.QUIT:
                running = False
            if (pygame.key.get_pressed()[pygame.K_SPACE] == True):
                clock = pygame.time.Clock()
                if(d.SLOW_MODE == False):
                     running = regularModeLoop(clock,screen,objects,running)
                else:
                     running = slowModeLoop(clock,screen,objects,running)
            if (pygame.key.get_pressed()[pygame.K_LEFT] == True):
                i -= 1
                i  = i % len(tests)
                objects = tests[i]().copy()
            if (pygame.key.get_pressed()[pygame.K_RIGHT] == True):
                i += 1
                i  = i % len(tests)
                objects = tests[i]().copy()
            if (pygame.key.get_pressed()[pygame.K_c] == True and toggle):
                if(d.COLISION_OFF == True):
                    d.COLISION_OFF = False
                else:
                    d.COLISION_OFF = True
                toggle = False
                clock.tick(1)
            if (pygame.key.get_pressed()[pygame.K_s] == True and toggle):
               if(d.SLOW_MODE == True):
                    d.SLOW_MODE = False
               else:
                    d.SLOW_MODE = True
               clock.tick(1)
               toggle = False
        



    pygame.quit()





def regularModeLoop(clock,screen,objects,running):
    while running:

            # Tera da igrica radi na maksimalno dati broj fps
            deltaTime = clock.tick(d.FPS) / 1000
            print("Lenght of frame: " , deltaTime )
    

            # Kad se zatvori prozor
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if (pygame.key.get_pressed()[pygame.K_ESCAPE] == True):
                    return running


            # pozadina
            screen.fill((255, 255, 120))

        
            for o in objects:
                o.move(screen,deltaTime)
        
            col.colisionCheckClassic(objects)

        

        



            #update celog ekrana
            pygame.display.update()
    return running


def slowModeLoop(clock,screen,objects,running):
    while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if (pygame.key.get_pressed()[pygame.K_ESCAPE] == True):
                        return running
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
    return running