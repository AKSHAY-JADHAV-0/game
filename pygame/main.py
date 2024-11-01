import pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame Window")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # White background
    pygame.display.flip()

pygame.quit()

