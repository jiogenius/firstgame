import os
import pygame

import GameComponent
import graphic
import animation
import load_function
import setting

pygame.init()

screen = pygame.display.set_mode((1600,800), pygame.RESIZABLE)#스크린 정의
surface = pygame.Surface((10000,8000))#서페이스 정의
running = True
mainFolderPath = os.path.dirname(os.path.abspath(__file__))#메인 파일 경로
assetPath=os.path.join(mainFolderPath,"asset") #에셋 폴더 경로
cam = graphic.cam([0,0]) #카메라 정의
Entities = [] #엔티티 리스트
Blocks = [GameComponent.GameObject([0,0])] #블록 리스트
clock = pygame.time.Clock() # 클럭 정의
FPS = 60  # 고정할 FPS 값
load_function.load() # 에셋 로드
test = animation.Animation("test2", 128, 10) # 애니메이션 객체 생성
#test2 = animation.Animation("image", 128, 10) # 두번째 애니메이션 객체 생성

def main():
    global running, screen, assetPath, clock ,FPS
    zoom_step = setting.setting.get("cameraSetting")["zoomStep"] # 줌 단계 설정
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get(): # 이벤트 처리
            if event.type == pygame.QUIT: # 창 닫기 이벤트
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                   cam.Zoom(zoom_step)
                elif event.y < 0:
                    cam.Zoom(-zoom_step)
        if keys[pygame.K_w]:
            cam.move([0,-10])
        if keys[pygame.K_s]:
            cam.move([0,10])
        if keys[pygame.K_d]:
            cam.move([10,0])
        if keys[pygame.K_a]:
            cam.move([-10,0])

        cam.surface.fill((255, 255, 255))
        cam.draw_image(test.get_current_image(), [5000, 5000]) # 애니메이션 이미지 그리기
        test.next()
        #test2.next()
        cam.drawToScreen(screen) # 카메라 서페이스를 스크린에 그리기
        #print(f"x:{cam.Rect.x} y:{cam.Rect.y} zoom:{cam.zoom} width:{cam.Rect.width} height:{cam.Rect.height}")
        pygame.display.flip()

        # FPS 고정
        clock.tick(FPS)



if __name__ == "__main__":
    main()