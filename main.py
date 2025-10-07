import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot


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

    # Intializing Drawable and Updatable, asteroids into Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Player and AsteroidField initialization
    MainPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    ENEMY_AsteroidField = AsteroidField()

    # Screen displayment and !GAMELOOP!
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000, rect=None, special_flags=0)

        updatable.update(dt)

        # Collision checks
        for asteroid in asteroids:
            if asteroid.check_collisions(MainPlayer) == True:
                raise sys.exit("Game over!")
            else:
                continue

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collisions(shot) == True:
                    asteroid.kill()
                    shot.kill
                    break
                else:
                    continue

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        # setting fps and calculating delta time
        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()
