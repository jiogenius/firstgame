import os
import pygame

import GameComponent
import graphic

pygame.init()

screen = pygame.display.set_mode((1000,800))
running = True
mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")
cam = graphic.cam([0,0],"cam")
Entities = []
Blocks = [GameComponent.GameObject([0,0])]

def main():
    global running, screen, assetPath
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cam.move([0,10])
                if event.key == pygame.K_s:
                    cam.move([0,-10])
                if event.key == pygame.K_d:
                    cam.move([10,0])
                if event.key == pygame.K_a:
                   cam.move([-10,0])

        screen.fill((255,255,255))

        cam.draw()
        pygame.display.flip()