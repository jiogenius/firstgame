import os
import pygame

import GameComponent
import graphic
import animation

pygame.init()

screen = pygame.display.set_mode((1000,800))
running = True
mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")
cam = graphic.cam([0,0],"cam")
Entities = []
Blocks = [GameComponent.GameObject([0,0])]
clock = pygame.time.Clock()
FPS = 60  # 고정할 FPS 값

def main():
    global running, screen, assetPath, clock ,FPS
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

        cam.draw(screen, animation.animation(pygame.image.load(os.path.join(assetPath,"test_animation.png")),32,20))
        font = pygame.font.SysFont(None, 30)
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()

        # FPS 고정
        clock.tick(FPS)



if __name__ == "__main__":
    main()