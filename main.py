import os
import pygame

import GameComponent
import graphic
import animation
import load_function

pygame.init()

screen = pygame.display.set_mode((1000,800))#스크린 정의
surface = pygame.Surface((10000,8000))#서페이스 정의
running = True
mainFolderPath = os.path.dirname(os.path.abspath(__file__))#메인 파일 경로
assetPath=os.path.join(mainFolderPath,"asset") #에셋 폴더 경로
cam = graphic.cam([0,0],"cam") #카메라 정의
Entities = [] #엔티티 리스트
Blocks = [GameComponent.GameObject([0,0])] #블록 리스트
clock = pygame.time.Clock() # 클럭 정의
FPS = 60  # 고정할 FPS 값
load_function.load() # 에셋 로드
test = animation.animation("test2",128,10) # 애니메이션 객체 생성

def main():
    global running, screen, assetPath, clock ,FPS
#    zoom = 1.0  # 줌 비율 (1.0 = 100%)
#    zoom_step = 0.1 # 줌 단계 (0.1 = 10% 증가/감소)
    while running:
        for event in pygame.event.get(): # 이벤트 처리
            if event.type == pygame.QUIT: # 창 닫기 이벤트
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cam.move([0,10])
                if event.key == pygame.K_s:
                    cam.move([0,-10])
                if event.key == pygame.K_d:
                    cam.move([-10,0])
                if event.key == pygame.K_a:
                   cam.move([10,0])
#            elif event.type == pygame.MOUSEWHEEL:
#                if event.y > 0:
#                    zoom += zoom_step
#                elif event.y < 0 and zoom > zoom_step:
#                    zoom -= zoom_step

        screen.fill((255,255,255))

        cam.draw(screen, test)
        test.next()

        pygame.display.flip()

        # FPS 고정
        clock.tick(FPS)



if __name__ == "__main__":
    main()