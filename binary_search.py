import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 850
HEIGHT = 200
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Binary Search Visualization')
clock = pygame.time.Clock()

# Generate a sorted list with random numbers ensuring 58 is included
numbers = sorted(random.sample(range(1, 100), 19) + [58])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found_index = -1
search_complete = False

# Define colors for gradient effect 
COLOR_START = (255, 153, 204)  
COLOR_END = (143, 190, 250)  

def interpolate_color(start_color, end_color, value):
    r = start_color[0] + int((end_color[0] - start_color[0]) * value)
    g = start_color[1] + int((end_color[1] - start_color[1]) * value)
    b = start_color[2] + int((end_color[2] - start_color[2]) * value)
    return (r, g, b)

def binary_search_step():
    global left, right, mid, found_index, search_complete
    if left <= right and not search_complete:
        mid = (left + right) // 2
        if numbers[mid] == 58:
            found_index = mid
            search_complete = True
        elif numbers[mid] < 58:
            left = mid + 1
        else:
            right = mid - 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Perform one step of binary search
    binary_search_step()

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

        # Draw the box with gradient effect
        if not search_complete and (left <= i <= right):
            color = (255, 0, 0)  # Red for currently processed box
        elif i == found_index and search_complete:
            color = (0, 255, 0)  # Green if 58 is found

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
