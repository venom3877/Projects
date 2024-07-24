import pygame
import time
import random

pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# set window dimensions
width = 600
height = 400

# create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# set the clock
clock = pygame.time.Clock()

# set the font
font_style = pygame.font.SysFont(None, 30)

# define the snake size and speed
snake_block = 10
snake_speed = 15

# define the function to display the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# display the message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# define the main function
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

       our_snake(snake_block, snake_List)
