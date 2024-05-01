import pygame
import math
import time

#Name: Glenn Noronha
#Date: 04/10/2024

pygame.init()

screen_width, screen_height = 1000, 1000
center = (screen_width // 2, screen_height // 2)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
step_size = 40

screen = pygame.display.set_mode((screen_width, screen_height))

running = True

def draw_number(screen, number, position, color=white, font_size=20):
    font = pygame.font.Font(None, font_size)
    text = font.render(str(number), True, color)
    screen.blit(text, position)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def up(x, y):
    return x, y - step_size

def down(x, y):
    return x, y + step_size

def right(x, y):
    return x + step_size, y

def left(x, y):
    return x - step_size, y

def find_position(num):
    global center # get the center coordinates
    x_, y_ = center[0], center[1]
    move_sequence = [right, up, left, down]
    # Initialize variables for tracking movement
    current_move = 0  # Index of the current movement in the move_sequence
    steps_to_move = 1  # Number of steps to move in the current direction
    steps_moved = 0  # Counter for the number of steps moved in the current direction
    change_direction = 0  # Counter for changing direction after moving in a direction twice

    # Loop through numbers from 1 to num
    for n in range(1, num + 1):
        if n > 1:  # Skip the initial position (1, 1)
            # Move to the next position based on the current movement in the sequence
            x_, y_ = move_sequence[current_move](x_, y_)
            steps_moved += 1  # Increment the steps moved counter
            if steps_moved == steps_to_move:  # Check if it's time to change direction
                current_move = (current_move + 1) % 4  # Update the current movement
                steps_moved = 0  # Reset the steps moved counter
                change_direction += 1  # Increment the direction change counter
                if change_direction % 2 == 0:  # Check if it's time to increase steps to move
                    steps_to_move += 1  # Increase the steps to move in the same direction

    return x_, y_

runner = 0

while running and runner < 600:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    runner += 1
    if runner == 1:
        screen.fill(black)
    x, y = find_position(runner)
    if is_prime(runner):
        draw_number(screen, runner, (x, y), color=blue)
    else:
        draw_number(screen, runner, (x, y))
    pygame.display.flip()
    time.sleep(0.01)

pygame.quit()
