import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 850
HEIGHT = 200
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Linear Search Visualization')
clock = pygame.time.Clock()

# Generate a list with random numbers ensuring 42 is included
numbers = random.sample(range(1, 100), 19) + [70]
random.shuffle(numbers)

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False

# Define colors for gradient effect
COLOR_START = (255, 255, 108)
COLOR_END = (255, 119, 192)

def interpolate_color(start_color, end_color, value):
    r = start_color[0] + int((end_color[0] - start_color[0]) * value)
    g = start_color[1] + int((end_color[1] - start_color[1]) * value)
    b = start_color[2] + int((end_color[2] - start_color[2]) * value)
    return (r, g, b)

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 70:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Perform linear search
    linear_search()

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw the numbers and boxes
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = HEIGHT // 2
        width = 30
        height = 30

        # Determine color based on gradient
        value = i / len(numbers)
        color = interpolate_color(COLOR_START, COLOR_END, value)

        # Highlight the correct number in green
        if i == found_index and search_complete:
            color = (0, 255, 0)
        elif i == current_index and not search_complete:
            color = (255, 0, 0)

        # Draw the box with gradient effect
        pygame.draw.rect(window, color, (x, y, width, height))
        pygame.draw.rect(window, (0, 0, 0), (x, y, width, height), 2)  # Add border for better visibility

        # Draw the number inside the box
        font = pygame.font.Font(None, 24)
        text_surface = font.render(str(number), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        window.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(2)  # Adjust frame rate for animation speed

pygame.quit()
