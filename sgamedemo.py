import pygame
import random

pygame.mixer.init()

pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
pink = (255, 50, 255)
black = (0, 0, 0)
green =(20, 230, 0)
yellow =(210,230,10)

# Creating Game window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Backgroud image
bgimg1 = pygame.image.load("welpic.jpeg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.image.load("GOVER.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()
bgimg3 = pygame.image.load("winner.jpeg")
bgimg3 = pygame.transform.scale(bgimg3, (screen_width, screen_height)).convert_alpha()
bgimg4 = pygame.image.load("snake.webp")
bgimg4 = pygame.transform.scale(bgimg4, (screen_width, screen_height)).convert_alpha()

# Game title
pygame.display.set_caption("SnakeGame")
pygame.display.update()

clock = pygame.time.Clock()
# noinspection PyTypeChecker
font = pygame.font.SysFont(None, 25)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    pygame.mixer.music.load("gtune3.mpeg")
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(bgimg1, (0, 0))
        text_screen("WELCOME TO SNAKE GAME ❤ :) 🥰 ",red, 250, 100)
        text_screen("PLAY --> CLICK ENTER",red, 280, 130)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    gameloop()

            pygame.display.update()
            clock.tick(60)


# # Function for level_up 2
def level_up2():
    level = 1
    for score in range(100,200):
        if score >= 100 or score <= 199:
            level += 1
            return str(level)

# Function for level_up 3
def level_up3():
    level = 2
    for score in range(200, 400):
        if score >= 200 or score <=399 :
            level += 1
            return str(level)

# Function for level_up 4
def level_up4():
    level = 3
    for score in range(400, 800):
        if score >= 400 or score <= 799:
            level += 1
            return str(level)

# Function for level_up 5
def level_up5():
    level = 4
    for score in range(800,2000):
        if score >= 800 or score <= 2000:
            level += 1
            return str(level)


#Winner Function
def winner():
    winner1 = False
    exit_game = False
    pygame.mixer.music.load("gtune3.mpeg")
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(bgimg3, (0, 0))
        text_screen("You Are The Winner :) 🥰 ", white, 250, 90)
        text_screen("PLAY AGAIN --> CLICK ENTER", white, 230, 120)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome()

            pygame.display.update()
            clock.tick(60)


# Game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 10
    snake_y = 200
    velocity_x = 0
    velocity_y = 0
    level = 1
    snake_list = []
    snake_length = 1
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    # noinspection PyTypeChecker
    food_x = random.randint(20, screen_width / 2)
    # noinspection PyTypeChecker
    food_y = random.randint(20, screen_height / 2)
    init_velocity = 2
    score = 0
    snake_size = 10
    fps = 60
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("SCORE:" + str(score), white, 350, 320)
            text_screen("PLAY AGAIN --> CLICK ENTER",white, 270,350)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Cheat code
                    if event.key == pygame.K_q:
                        score += 50

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                    pygame.mixer.music.load("beep-03.wav")
                    pygame.mixer.music.play()
                    score += 10
                    # noinspection PyTypeChecker
                    food_x = random.randint(20, screen_width / 2)
                    # noinspection PyTypeChecker
                    food_y = random.randint(20, screen_height / 2)
                    snake_length += 2
                    if score >= 100:
                        level_up2()
                        level = level_up2()
                        level_up3()
                        if score >= 200:
                            level = level_up3()
                            level_up4()
                            if score >= 400:
                                level = level_up4()
                                level_up5()
                                if score >= 800:
                                    level = level_up5()
                                    if score >= 2000:
                                        winner()
                                        break



                    if score>int(highscore):
                        highscore = score


            gameWindow.fill(black)
            gameWindow.blit(bgimg4, (0,0))
            text_screen("Level-"+str(level ), yellow, 10, 10)
            text_screen("Score: " + str(score) + " Highscore: " + str(highscore), yellow, 570, 10)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[: -1]:
                game_over = True
                pygame.mixer.music.load("gtone1.mpeg")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("gtone1.mpeg")
                pygame.mixer.music.play()
            plot_snake(gameWindow, green, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
    
welcome()
