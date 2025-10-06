import pygame
from constants import *


def main():
    # Starting sequence
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Screen initialisation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Screen displayment
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000, rect=None, special_flags=0)
        pygame.display.flip()


if __name__ == "__main__":
    main()
