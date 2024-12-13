import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        # Simply return if the radius of the asteroid is the smallest. No need to split this guy.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        
        child_one_vectors = self.velocity.rotate(angle)
        child_two_vectors = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        child_one_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        child_two_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        
        child_one_asteroid.velocity = child_one_vectors * 1.2
        child_two_asteroid.velocity = child_two_vectors * 1.2
        
