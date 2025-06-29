import pygame

pygame.init()

# 기본 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 더미용 이미지 서피스 (예: 맵, 배경 등)
original_surface = pygame.Surface((1600, 1200))  # 더 큰 월드
original_surface.fill((50, 50, 100))  # 배경색
pygame.draw.circle(original_surface, (255, 0, 0), (800, 600), 100)  # 원 하나

zoom = 1.0  # 줌 비율 (1.0 = 100%)
zoom_step = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 휠로 줌인/아웃
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom += zoom_step
            elif event.y < 0 and zoom > zoom_step:
                zoom -= zoom_step

    # 원본 이미지를 줌 비율에 맞게 스케일링
    scaled_width = int(original_surface.get_width() * zoom)
    scaled_height = int(original_surface.get_height() * zoom)
    scaled_surface = pygame.transform.smoothscale(original_surface, (scaled_width, scaled_height))

    # 화면 중앙에 맞춰서 그리기
    x_offset = (scaled_surface.get_width() - WIDTH) // 2
    y_offset = (scaled_surface.get_height() - HEIGHT) // 2
    view = scaled_surface.subsurface((x_offset, y_offset, WIDTH, HEIGHT))

    screen.blit(view, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()