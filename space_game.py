import pygame 
import random 
import sys
import keyboard

#initialization of game engine
pygame.init()

#initialization of the game screen and screen related attibutes
screen_resolution = (800, 1000)
screen = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("gulaguli_khela")

bg = pygame.image.load("bg.jpg")
score = 0
enemy_speed = 7
player_movement = 30

clock = pygame.time.Clock()
game_speed = 40
level = 50
game_over = False


#player attributes
player = pygame.image.load("player.png")
x_co = 368
y_co = 900
player_position = [x_co, y_co]

#enemy attributes
enemy = pygame.image.load("enemy.png")
ey_co = 1
enemy_position = [random.randint(0, 750), ey_co]

positions = [enemy_position]

def generate_enemies(positions): 
    delay = random.random()
    global score

    if len(positions) < 10 and delay < .2: 
        for _ in range(random.randint(3, 10)): 
            enemy_position = [random.randint(0, 750), random.randint(-250, 20)]
            positions.append(enemy_position)

    for indexx, enemy_position in enumerate(positions): 
        screen.blit(enemy, enemy_position)

        if enemy_position[1]>=0 and enemy_position[1] < 980: 
            enemy_position[1] += enemy_speed

        else:
            positions.pop(indexx)


    return positions


def is_collision(player_position, positions): 

    for enemy_position in positions: 
        if detect_collision(player_position, enemy_position): 
            return True


def detect_collision(player_position, enemy_position): 

    if (player_position[0] in range(enemy_position[0], enemy_position[0] + 58)) and (player_position[1] in range(enemy_position[1], enemy_position[1] + 65)):
        
        return True


while not game_over:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            sys.exit()
        
        if event.type == pygame.KEYDOWN: 
            
            if event.key == pygame.K_LEFT and x_co >= 10: 
                x_co -= player_movement 

            elif event.key == pygame.K_RIGHT and x_co <= 720: 
                x_co += player_movement 

            elif event.key == pygame.K_UP and y_co >= 10: 
                y_co -= player_movement 

            elif event.key == pygame.K_DOWN and y_co <= 880: 
                y_co += player_movement 
     
            player_position = [x_co, y_co]

    score += 1
    screen.blit(bg, (0, 0))
    label = pygame.font.SysFont("Agency FB", 30).render(f"Score: {int((score *2)/game_speed)}", 1, (231, 76, 60))
    screen.blit(label, (700, 20))
    
    if is_collision(player_position, generate_enemies(positions)):

        with open("score.txt", "r") as file1: 
            highscore = int(file1.read()) 
        if (highscore > (int(score/(game_speed / 2)))):

            print(f"GAME OVER! Your score is {int(score/(game_speed / 2))}.\nHighscore: {highscore}.")
            break

        else: 
            print(f"NEW HIGHSORE {str(int(((score * 2)/game_speed)))}.")
            with open("score.txt", "w") as file1: 
                file1.write(str(int((score*2)/game_speed)))
            
            break

    screen.blit(player, player_position)
        
    if (score / 30) > level: 
        level += 50
        game_speed += 10

    clock.tick(game_speed)
    pygame.display.update()

pygame.display.quit()
print("Press anykey to exit.")
keyboard.read_key()