import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Initialize snake
snake = [(width // 2, height // 2)]
snake_direction = "RIGHT"

# Initial food position
food_position = (
    round(random.randrange(0, width - snake_block) / 10.0) * 10.0,
    round(random.randrange(0, height - snake_block) / 10.0) * 10.0,
)

# Score
score = 0

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    # Move the snake
    x, y = snake[0]
    if snake_direction == "LEFT":
        x -= snake_block
    elif snake_direction == "RIGHT":
        x += snake_block
    elif snake_direction == "UP":
        y -= snake_block
    elif snake_direction == "DOWN":
        y += snake_block

    # Check if snake has collided with the boundaries
    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    # Check if snake has collided with itself
    for segment in snake[1:]:
        if x == segment[0] and y == segment[1]:
            game_over = True

    # Check if snake has eaten the food
    if x == food_position[0] and y == food_position[1]:
        food_position = (
            round(random.randrange(0, width - snake_block) / 10.0) * 10.0,
            round(random.randrange(0, height - snake_block) / 10.0) * 10.0,
        )
        score += 1
    else:
        snake.pop()

    # Update snake position
    snake.insert(0, (x, y))

    # Draw background
    display.fill(white)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(display, black, [segment[0], segment[1], snake_block, snake_block])

    # Draw food
    pygame.draw.rect(display, red, [food_position[0], food_position[1], snake_block, snake_block])

    # Display score
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, black)
    display.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
