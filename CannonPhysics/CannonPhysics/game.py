
import numpy as np
import pygame 
import defs as d
import gameObject as go





def run():
    
    pygame.init()

    screen = pygame.display.set_mode([d.WIDTH, d.HEIGHT])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Cannon physics")

    objects = []
    for i in range(1,4):
        circle = go.Circle(d.WIDTH / 2 ,d.HEIGHT / 2,i*10)
        objects.append(circle)

    for i in range(1,4):
        reck = go.Rectangle(d.WIDTH * i / 6 ,d.HEIGHT / 4,40 * i,20 * i, np.pi * (i-1)/3)
        objects.append(reck)
    
    
    

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

        #update celog ekrana
        pygame.display.update()


        

    # Done! Time to quit.
    pygame.quit()
