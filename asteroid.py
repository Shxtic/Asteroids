import random
import pygame
from typing import override
from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            new_trajectory = random.uniform(20, 50)
            vector1 = self.velocity.rotate(new_trajectory)
            vector2 = self.velocity.rotate((-new_trajectory))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = vector1 * 1.2
            new_asteroid2.velocity = vector2 * 1.2
            self.kill()
