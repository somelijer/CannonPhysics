from turtle import circle
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
    for i in range(1,7):
        circle = go.Circle(d.WIDTH / (i+1) ,d.HEIGHT / 2,i*10)
        objects.append(circle)
    
    

    deltaTime = 0

    running = True
    while running:

        # Tera da igrica radi na maksimalno dati broj fps
        deltaTime = clock.tick(d.FPS) / 1000
    

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
