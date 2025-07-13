import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 전체 월드 surface (예시: 배경)
world_surface = pygame.Surface((2000, 1600))
world_surface.fill((50, 50, 80))
pygame.draw.circle(world_surface, (255, 0, 0), (1000, 800), 100)

# 카메라 초기 상태
base_width = 800
base_height = 600
zoom = 1.0
min_zoom = 0.5
max_zoom = 2.0
camera_rect = pygame.Rect(600, 500, base_width, base_height)

camera_speed = 10  # 카메라 이동 속도

running = True
while running:
    keys = pygame.key.get_pressed()

    # 카메라 이동 (WASD or 화살표)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        camera_rect.x -= camera_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        camera_rect.x += camera_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        camera_rect.y -= camera_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        camera_rect.y += camera_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEWHEEL:
            # 줌 전 중심 기억
            center = camera_rect.center

            # 줌 변경
            zoom += 0.1 * event.y
            zoom = max(min_zoom, min(max_zoom, zoom))

            # 줌 비율에 따라 크기 재설정
            new_w = int(base_width / zoom)
            new_h = int(base_height / zoom)
            camera_rect.width = new_w
            camera_rect.height = new_h
            camera_rect.center = center  # 중심 유지


    # 카메라 시야 잘라서 스케일링
    cut_rect = camera_rect.clip(world_surface.get_rect())
    visible_surface = world_surface.subsurface(cut_rect)
    scaled_surface = pygame.transform.scale(visible_surface, screen.get_size())

    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()