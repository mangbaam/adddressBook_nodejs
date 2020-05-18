import pygame
import random
###################################################################################
# 기본 초기화 ( 반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 ( 배경 화면, 게임 이미지, 좌표, 속도, 폰트 등 )
background = pygame.image.load("background.png")

character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.6
enemy_speed = 0.5 * (1 + character_speed//1)

enemy = pygame.image.load("ddong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = -enemy_height

game_font = pygame.font.Font(None, 40)

score = 0

status = None

#total_time = 10
#start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(120) # 게임 화면의 초당 프레임 수 설정

    #print("fps : "+str(clock.get_fps()))


    # 2. 이벤트 처리 ( 기보드, 마우스 등 )
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는지 확인
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트 발생 여부 확인
            running = False             # 게임이 진행 중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    enemy_y_pos += enemy_speed * dt

    # 경계값 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    # 3. 게임 캐릭터 위치 정의

    # 똥 피함
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = -enemy_height
        score += 1


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = int(character_x_pos)
    character_rect.top = int(character_y_pos)

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌 발생")
        status = "collision"
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 점수 표시
    print_score = game_font.render(str(int(score)), True, (255, 255, 255))
    screen.blit(print_score, (10, 10))



    pygame.display.update() # 게임 화면 다시 그리기!!


# 잠시 대기
# pygame.time.delay(2000)  # 2초 정도 대기 (ms)

# 게임 종료 text
end_text = "GAME END"
the_end = game_font.render(end_text, True, (255, 255, 255))
the_end_rect = the_end.get_rect().size
the_end_width = the_end_rect[0]
the_end_height = the_end_rect[1]

screen.blit(the_end, (screen_width / 2 - the_end_width / 2, screen_height / 2 - the_end_height / 2))
pygame.display.update()




# pygame 종료
pygame.quit()