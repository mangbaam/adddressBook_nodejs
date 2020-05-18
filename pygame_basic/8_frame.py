import pygame
###################################################################################
# 기본 초기화 ( 반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Mangs Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 ( 배경 화면, 게임 이미지, 좌표, 속도, 폰트 등 )

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정

    # 2. 이벤트 처리 ( 기보드, 마우스 등 )
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는지 확인
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트 발생 여부 확인
            running = False             # 게임이 진행 중이 아님

    # 3. 게임 캐릭터 위치 정의


    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 게임 화면 다시 그리기!!


# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()