
import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    #player score
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
    
    #opponent score 
    if ball.right >= WIDTH:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.colliderect(player) and ball_speed_x > 0 :
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 10: #to prevent the collision
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1
                
    if ball.colliderect(opponent) and ball_speed_x < 0:
        if abs(ball.right - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 10: #to prevent the collision
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1
        
        
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT    

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT    

def ball_restart():
    global ball_speed_y, ball_speed_x, score_time
    
    current_time = pygame.time.get_ticks()
    ball.center = (WIDTH/2, HEIGHT/2) 

    if current_time - score_time < 700:
        number_three = game_font.render("3",False,light_grey)
        screen.blit(number_three, (WIDTH/2 -10,HEIGHT/2 +20))    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False,light_grey)
        screen.blit(number_two, (WIDTH/2 -10,HEIGHT/2 +20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,light_grey)
        screen.blit(number_one, (WIDTH/2 -10,HEIGHT/2 +20))
    
    
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None



#general setup
pygame.init()
clock = pygame.time.Clock()

#main window
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PONG')

#game rectangles
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 -15, 20, 20)
player = pygame.Rect(WIDTH-20,HEIGHT/2 -70,10, 140)
opponent = pygame.Rect(10, HEIGHT/2 -70, 10, 140)

#colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#game variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
ball_moving = False
score_time = True

#score text
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 26)

#score timer
score_time = True

while True:
    for event in pygame.event.get():    #handling input
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:    #checks if any key on keyboard is pressed down
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7    
    
    #game logic
    ball_animation()
    player_animation()
    opponent_animation()
    
    #visuals        
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (WIDTH/2,0), (WIDTH/2, HEIGHT))
    
    if score_time:
        ball_restart()
    
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (330,220))
    
    opponent_text =game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (295,220))
    
    
    pygame.display.flip()
    clock.tick(60)      


