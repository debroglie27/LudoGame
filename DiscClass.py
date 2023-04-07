import pygame


class Disc:
    def __init__(self, win, color, radius, initial_position, _id):
        self.window = win
        self.color = color
        self.radius = radius

        self.initial_pos = initial_position
        self.current_pos = initial_position

        self.movement = False

        self.disc_id = _id
        self.current_id = 0
        self.max_current_id = 56

        self.box_collider = pygame.Rect(self.current_pos[0] - self.radius, self.current_pos[1] - self.radius,
                                        2*self.radius, 2*self.radius)

    def update(self):
        # Colored Disc
        pygame.draw.circle(self.window, self.color, self.current_pos, self.radius)
        # Border Circle
        pygame.draw.circle(self.window, (0, 0, 0), self.current_pos, self.radius, width=1)
        # Inner Circle
        pygame.draw.circle(self.window, (0, 0, 0), self.current_pos, self.radius - 5, width=1)

        self.box_collider = pygame.Rect(self.current_pos[0] - self.radius, self.current_pos[1] - self.radius,
                                        2*self.radius, 2*self.radius)

    def respawn(self):
        self.current_pos = self.initial_pos
        self.movement = False
        self.current_id = 0
