import pygame
import os

screen = pygame.display.set_mode((1000, 800))  # 스크린 정의
running = True
mainFolderPath = os.path.dirname(os.path.abspath(__file__))  # 메인 파일 경로
assetPath = os.path.join(mainFolderPath, "asset")  # 에셋 폴더 경로

while running:
    for event in pygame.event.get():  # 이벤트 처리
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            running = False

    screen.fill((255, 255, 255))  # 화면 초기화

    pygame.display.flip()  # 화면 업데이트