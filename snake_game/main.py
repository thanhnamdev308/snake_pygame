"""
Functions to run game and 
main function of the project
"""
import pygame
import time
from snake import Snake
from block import Block
from random import randint

# Init pygame
pygame.init()

# The window will contain 400 blocks of 40x40
WINDOW_SIDE: int = 840
BLOCK_SIDE: int = 40

# Declare game window
WINDOW_SIZE: tuple = WINDOW_SIDE, WINDOW_SIDE  # width, height
window = pygame.display.set_mode(WINDOW_SIZE)
# Fill window color (to match image)
window.fill("#151515")

# Init font
font = pygame.font.Font(None, 30)

# Declare parameter to generate position for Food
# Food position need to be range from (0,0) to (20*20, 20*20) to be in the window
FOOD_COORDINATE_RANGE = int((WINDOW_SIDE / BLOCK_SIDE) - 1)
FOOD_RADIUS = int((BLOCK_SIDE / 2))

# Declare FPS
FPS: int = 8  # Frame per second

# Declare start screen and end screen images
start_screen_image_link = "images/start_screen.png"
end_screen_image_link = "images/end_screen.png"


def clear_window() -> None:
    """
    Clear the pygame window
    """

    # Fill window color that match image
    window.fill("#151515")


def draw_block(x: int, y: int, mode: str) -> None:
    """
    Draw a block at position (x, y)
    """

    if mode == "head":
        rect = pygame.Rect(x, y, BLOCK_SIDE, BLOCK_SIDE)
        pygame.draw.rect(window, ("yellowgreen"), rect)
    elif mode == "body":
        rect = pygame.Rect(x, y, BLOCK_SIDE, BLOCK_SIDE)
        pygame.draw.rect(window, ("white"), rect)
    elif mode == "food":
        center: tuple = ((x + FOOD_RADIUS), (y + FOOD_RADIUS))
        # make the food smaller than snake block for good look
        pygame.draw.circle(window, ("coral"), center, FOOD_RADIUS - 7)


def gen_new_food(food: Block, snake: Snake) -> None:
    """
    Generate new food at random position
    """

    new_x = 0
    new_y = 0
    new_pos_not_valid = True
    while new_pos_not_valid:
        new_pos_not_valid = False
        new_x = randint(0, FOOD_COORDINATE_RANGE) * BLOCK_SIDE
        new_y = randint(0, FOOD_COORDINATE_RANGE) * BLOCK_SIDE

        if (new_x == snake.head.x) and (new_y == snake.head.y):
            new_pos_not_valid = True

        for block in snake.body:
            if (new_x == block.x) and (new_y == block.y):
                new_pos_not_valid = True

    food.x = new_x
    food.y = new_y


def update_food(food: Block) -> None:
    """
    Update food position on screen
    """

    draw_block(food.x, food.y, "food")


def update_snake(snake: Snake) -> None:
    """
    Update snake head and body position on screen
    """

    for block in snake.body:
        draw_block(block.x, block.y, "body")

    draw_block(snake.head.x, snake.head.y, "head")


def draw_start_screen():
    """
    Function to draw start screen
    """

    # Fill window color (to match image)
    window.fill("#151515")

    # Set the image to be at the center of the window
    image = pygame.image.load(start_screen_image_link)
    rect = image.get_rect()
    rect.center = (WINDOW_SIDE / 2, WINDOW_SIDE / 2)

    # Load image
    window.blit(image, rect)
    pygame.display.update()

    # Wait for user to press any key
    exit_screen = False
    while not exit_screen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                exit_screen = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()


def draw_end_screen(snake: Snake):
    """
    Function to draw start screen
    """

    # Fill window color (to match image)
    window.fill("#151515")

    # Draw score
    draw_score(snake)

    # Set the image to be at the center of the window
    image = pygame.image.load(end_screen_image_link)
    rect = image.get_rect()
    rect.center = (WINDOW_SIDE / 2, WINDOW_SIDE / 2)

    # Load image
    window.blit(image, rect)
    pygame.display.update()

    # Wait for user to press any key
    exit_screen = False
    while not exit_screen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                exit_screen = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()


def draw_score(snake: Snake) -> None:
    """
    Function to draw player score on screen
    """

    text = font.render(f"Score = {snake.size}", True, "white")
    rect = text.get_rect()
    rect.center = (WINDOW_SIDE / 2, 20)
    window.blit(text, rect)


def run_game():
    """
    Game loop
    """

    # Fill window color (to match image)
    window.fill("#151515")

    # Init clock for rendering movement
    clock = pygame.time.Clock()

    # Init snake
    snake = Snake()

    # Init food
    food = Block()
    gen_new_food(food, snake)

    while snake.alive:
        # Update
        clock.tick(FPS)
        clear_window()
        update_snake(snake)
        update_food(food)
        draw_score(snake)
        pygame.display.update()

        # Run the snake
        snake.run()

        # Listen to keyboard event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if snake.direction != "right" or snake.size == 0:
                    snake.direction = "left"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if snake.direction != "left" or snake.size == 0:
                    snake.direction = "right"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if snake.direction != "down" or snake.size == 0:
                    snake.direction = "up"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if snake.direction != "up" or snake.size == 0:
                    snake.direction = "down"
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Snake eat
        if (snake.head.x == food.x) and (snake.head.y == food.y):
            gen_new_food(food, snake)
            snake.growing = True

    time.sleep(1)
    draw_end_screen(snake)


def main():
    """
    Main function
    """

    # Init the window
    pygame.display.set_caption("Snake pygame")

    draw_start_screen()

    while True:
        run_game()


if __name__ == "__main__":
    main()
