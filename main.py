import pygame
from constants import *
from player import *


def main():
    # Starting sequence
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Screen initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player initialization
    MainPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Screen displayment and !GAMELOOP!
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000, rect=None, special_flags=0)
        MainPlayer.draw(screen)
        pygame.display.flip()
        # setting fps and calculating delta time
        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()
