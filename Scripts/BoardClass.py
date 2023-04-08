from io import BytesIO
from base64 import b64decode
import pygame
import PlayerClass
from BinaryImages import star


class Board:
    def __init__(self, win, sw, sh):
        self.win = win
        self.sw = sw
        self.sh = sh

        # Offsets for proper board display
        self.offset1 = 28
        self.offset2 = 35
        self.offset3 = 64

        # Circle radius for circle behind the discs initial positions
        self.circle_radius = 20

        # Color pallet for the board
        self.red = (230, 50, 50)
        self.green = (50, 230, 50)
        self.yellow = (230, 230, 50)
        self.blue = (0, 120, 250)

        # Disc Colors
        self.red_disc_color = (200, 0, 0)
        self.green_disc_color = (0, 200, 0)
        self.yellow_disc_color = (200, 200, 0)
        self.blue_disc_color = (0, 0, 200)

        # Disc radius
        self.disc_radius = 14

        # Used to initialise the players
        self.initial_pos_lists = None
        # Used to store all the players
        self.Players = None

        # Loading the Star Image
        self.star_img = self.load_star_img()

        # Safe Positions in board for a disc
        self.safe_positions = [(210, 504), (47, 261), (290, 97), (453, 341),
                               (79, 341), (210, 129), (421, 261), (290, 472)]

    @staticmethod
    def load_star_img():
        # Decoding the Star Binary Image which is imported from BinaryImages.py
        decoded_img = BytesIO(b64decode(star))
        # Loading the star image
        img = pygame.image.load(decoded_img)
        # Resizing the Star Image
        star_img = pygame.transform.scale(img, (33, 33))

        return star_img

    def load_players(self):
        # Initialising the Players
        player_red = PlayerClass.Player(self.win, self.red_disc_color, self.disc_radius,
                                        self.initial_pos_lists[0])
        player_green = PlayerClass.Player(self.win, self.green_disc_color, self.disc_radius,
                                          self.initial_pos_lists[1])
        player_yellow = PlayerClass.Player(self.win, self.yellow_disc_color, self.disc_radius,
                                           self.initial_pos_lists[2])
        player_blue = PlayerClass.Player(self.win, self.blue_disc_color, self.disc_radius,
                                         self.initial_pos_lists[3])

        self.Players = [player_red, player_green, player_yellow, player_blue]

        return self.Players

    def current_status(self):
        # Status variable will store the disc positions player wise
        status = {}
        for player in self.Players:
            status[player] = []
            for disc in player.discs:
                # Storing the current position, current id and movement bool of all discs
                # under each individual players
                status[player].append((disc.current_pos, disc.current_id, disc.movement))

        return status

    def display(self):
        sw = self.sw
        sh = self.sh

        self.win.fill((0, 0, 0))
        pygame.draw.rect(self.win, (240, 240, 240), (0, (sh-sw)//2, sw, sw))

        # Drawing the Squares
        # Red Square
        pygame.draw.rect(self.win, self.red, (0, (sh-sw)//2 + (6.2*sw)//10, (3.8*sw)//10, (3.8*sw)//10))
        # Green Square
        pygame.draw.rect(self.win, self.green, (0, (sh-sw)//2, (3.8*sw)//10, (3.8*sw)//10))
        # Yellow Square
        pygame.draw.rect(self.win, self.yellow, ((6.2*sw)//10, (sh-sw)//2, (3.8*sw)//10, (3.8*sw)//10))
        # Blue Square
        pygame.draw.rect(self.win, self.blue, ((6.2*sw)//10, int((sh-sw)//2 + (6.2*sw)//10), (3.8*sw)//10, (3.8*sw)//10))

        # Drawing the white squares
        # For Red Player
        pygame.draw.rect(self.win, (255, 255, 255), (self.offset1,
                                                     (sh-sw)//2 + (6.2*sw)//10 + self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1))
        # For Green Player
        pygame.draw.rect(self.win, (255, 255, 255), (self.offset1,
                                                     (sh-sw)//2 + self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1))
        # For Yellow Player
        pygame.draw.rect(self.win, (255, 255, 255), ((6.2*sw)//10 + self.offset1,
                                                     (sh-sw)//2 + self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1,
                                                     (3.8 * sw)//10 - 2*self.offset1))
        # For Blue Player
        pygame.draw.rect(self.win, (255, 255, 255), (int((6.2*sw)//10 + self.offset1),
                                                     (sh-sw)//2 + (6.2*sw)//10 + self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1,
                                                     (3.8*sw)//10 - 2*self.offset1))

        # Drawing the Triangles
        # Red Triangle
        pygame.draw.polygon(self.win, self.red, [((3.8*sw)//10, (sh-sw)//2 + (6.2*sw)//10),
                                                 (sw//2, sh//2),
                                                 ((6.2*sw)//10, (sh-sw)//2 + (6.2*sw)//10)])
        # Green Triangle
        pygame.draw.polygon(self.win, self.green, [((3.8*sw)//10, (sh-sw)//2 + (6.2*sw)//10),
                                                   (sw//2, sh//2),
                                                   ((3.8*sw)//10, (sh-sw)//2 + (3.8*sw)//10)])
        # Yellow Triangle
        pygame.draw.polygon(self.win, self.yellow, [((6.2*sw)//10, (sh-sw)//2 + (3.8*sw)//10),
                                                    (sw//2, sh//2),
                                                    ((3.8*sw)//10, (sh-sw)//2 + (3.8*sw)//10)])
        # Blue Triangle
        pygame.draw.polygon(self.win, self.blue, [((6.2*sw)//10, (sh-sw)//2 + (3.8*sw)//10),
                                                  (sw//2, sh//2),
                                                  ((6.2*sw)//10, (sh-sw)//2 + (6.2*sw)//10)])

        # Drawing the L-shaped Areas
        # Red
        pygame.draw.polygon(self.win, self.red, [((4.6*sw)//10, (sh-sw)//2 + (6.2*sw)//10),
                                                 ((5.4*sw)//10, (sh-sw)//2 + (6.2*sw)//10),
                                                 ((5.4*sw)//10, sh - (sh-sw)//2 - (1/6)*(3.8*sw)//10),
                                                 ((3.8*sw)//10, sh - (sh-sw)//2 - (1/6)*(3.8*sw)//10),
                                                 ((3.8*sw)//10, sh - (sh-sw)//2 - (1/3)*(3.8*sw)//10),
                                                 ((4.6*sw)//10, sh - (sh-sw)//2 - (1/3)*(3.8*sw)//10)])
        # Green
        pygame.draw.polygon(self.win, self.green, [((3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2),
                                                   ((3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2),
                                                   ((1/6)*(3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2),
                                                   ((1/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                                                   ((1/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                                                   ((1/3)*(3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2)])
        # Yellow
        pygame.draw.polygon(self.win, self.yellow, [((5.4*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                                                    ((4.6*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                                                    ((4.6*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2),
                                                    ((6.2*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2),
                                                    ((6.2*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2),
                                                    ((5.4*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2)])
        # Blue
        pygame.draw.polygon(self.win, self.blue, [((6.2*sw)//10, (5.4*sw)//10 + (sh-sw)//2),
                                                  ((6.2*sw)//10, (4.6*sw)//10 + (sh-sw)//2),
                                                  ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2),
                                                  ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2),
                                                  ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2),
                                                  ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2)])

        # Drawing the Circles
        self.draw_circles()
        # Drawing the Stars
        self.draw_stars()
        # Drawing the Lines
        self.draw_lines()

    def draw_stars(self):
        # All the star positions
        star_positions = [(194, 488), (30, 245), (273, 81), (436, 325),
                          (63, 325), (194, 113), (404, 245), (274, 456)]

        # Displaying the star images
        for pos in star_positions:
            self.win.blit(self.star_img, pos)

    def draw_circles(self):
        sw = self.sw
        sh = self.sh

        # Red Circle Positions
        red_pos_1 = (self.offset1 + self.offset2, int((sh - sw) // 2 + (6.2 * sw) // 10 + self.offset1 + self.offset2))
        red_pos_2 = (self.offset1 + self.offset2 + self.offset3,
                     int((sh - sw) // 2 + (6.2 * sw) // 10 + self.offset1 + self.offset2))
        red_pos_3 = (self.offset1 + self.offset2,
                     int((sh - sw) // 2 + (6.2 * sw) // 10 + self.offset1 + self.offset2 + self.offset3))
        red_pos_4 = (self.offset1 + self.offset2 + self.offset3,
                     int((sh - sw) // 2 + (6.2 * sw) // 10 + self.offset1 + self.offset2 + self.offset3))
        # Red Circles
        pygame.draw.circle(self.win, self.red, red_pos_1, self.circle_radius)
        pygame.draw.circle(self.win, self.red, red_pos_2, self.circle_radius)
        pygame.draw.circle(self.win, self.red, red_pos_3, self.circle_radius)
        pygame.draw.circle(self.win, self.red, red_pos_4, self.circle_radius)

        # Green Circle Positions
        green_pos_1 = (self.offset1 + self.offset2, (sh - sw) // 2 + self.offset1 + self.offset2)
        green_pos_2 = (self.offset1 + self.offset2 + self.offset3, (sh - sw) // 2 + self.offset1 + self.offset2)
        green_pos_3 = (self.offset1 + self.offset2, (sh - sw) // 2 + self.offset1 + self.offset2 + self.offset3)
        green_pos_4 = (self.offset1 + self.offset2 + self.offset3, (sh - sw) // 2 + self.offset1 + self.offset2 + self.offset3)
        # Green Circles
        pygame.draw.circle(self.win, self.green, green_pos_1, self.circle_radius)
        pygame.draw.circle(self.win, self.green, green_pos_2, self.circle_radius)
        pygame.draw.circle(self.win, self.green, green_pos_3, self.circle_radius)
        pygame.draw.circle(self.win, self.green, green_pos_4, self.circle_radius)

        # Yellow Circle Positions
        yellow_pos_1 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2, (sh - sw) // 2 + self.offset1 + self.offset2)
        yellow_pos_2 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2 + self.offset3,
                        (sh - sw) // 2 + self.offset1 + self.offset2)
        yellow_pos_3 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2,
                        (sh - sw) // 2 + self.offset1 + self.offset2 + self.offset3)
        yellow_pos_4 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2 + self.offset3,
                        (sh - sw) // 2 + self.offset1 + self.offset2 + self.offset3)
        # Yellow Circles
        pygame.draw.circle(self.win, self.yellow, yellow_pos_1, self.circle_radius)
        pygame.draw.circle(self.win, self.yellow, yellow_pos_2, self.circle_radius)
        pygame.draw.circle(self.win, self.yellow, yellow_pos_3, self.circle_radius)
        pygame.draw.circle(self.win, self.yellow, yellow_pos_4, self.circle_radius)

        # Blue Circle Positions
        blue_pos_1 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2,
                      (sh - sw) // 2 + int((6.2 * sw) // 10) + self.offset1 + self.offset2)
        blue_pos_2 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2 + self.offset3,
                      (sh - sw) // 2 + int((6.2 * sw) // 10) + self.offset1 + self.offset2)
        blue_pos_3 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2,
                      (sh - sw) // 2 + int((6.2 * sw) // 10) + self.offset1 + self.offset2 + self.offset3)
        blue_pos_4 = (int((6.2 * sw) // 10) + self.offset1 + self.offset2 + self.offset3,
                      (sh - sw) // 2 + int((6.2 * sw) // 10) + self.offset1 + self.offset2 + self.offset3)
        # Blue Circles
        pygame.draw.circle(self.win, self.blue, blue_pos_1, self.circle_radius)
        pygame.draw.circle(self.win, self.blue, blue_pos_2, self.circle_radius)
        pygame.draw.circle(self.win, self.blue, blue_pos_3, self.circle_radius)
        pygame.draw.circle(self.win, self.blue, blue_pos_4, self.circle_radius)

        red_positions = [red_pos_1, red_pos_2, red_pos_3, red_pos_4]
        green_positions = [green_pos_1, green_pos_2, green_pos_3, green_pos_4]
        yellow_positions = [yellow_pos_1, yellow_pos_2, yellow_pos_3, yellow_pos_4]
        blue_positions = [blue_pos_1, blue_pos_2, blue_pos_3, blue_pos_4]

        if self.initial_pos_lists is None:
            self.initial_pos_lists = [red_positions, green_positions, yellow_positions, blue_positions]

    def draw_lines(self):
        sw = self.sw
        sh = self.sh

        # Big lines
        # Vertical
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (sh-sw)//2), ((3.8*sw)//10, sh - (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10, (sh-sw)//2), ((6.2*sw)//10, sh - (sh-sw)//2))
        # Horizontal
        pygame.draw.line(self.win, (0, 0, 0), (0, (3.8*sw)//10 + (sh-sw)//2), (sw, (3.8*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), (0, (6.2*sw)//10 + (sh-sw)//2), (sw, (6.2*sw)//10 + (sh-sw)//2))

        # Medium Lines
        # For Yellow
        pygame.draw.line(self.win, (0, 0, 0), ((4.6*sw)//10, (sh-sw)//2), ((4.6*sw)//10, (3.8*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((5.4*sw)//10, (sh-sw)//2), ((5.4*sw)//10, (3.8*sw)//10 + (sh-sw)//2))
        # For Red
        pygame.draw.line(self.win, (0, 0, 0), ((4.6*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((4.6*sw)//10, sw + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((5.4*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((5.4*sw)//10, sw + (sh-sw)//2))
        # For Green
        pygame.draw.line(self.win, (0, 0, 0), (0, (4.6*sw)//10 + (sh-sw)//2), ((3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), (0, (5.4*sw)//10 + (sh-sw)//2), ((3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2))
        # For Blue
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10, (4.6*sw)//10 + (sh-sw)//2), (sw, (4.6*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10, (5.4*sw)//10 + (sh-sw)//2), (sw, (5.4*sw)//10 + (sh-sw)//2))

        # Center Lines
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (3.8*sw)//10 + (sh-sw)//2))

        # Short Lines
        # b/w Red and Green
        pygame.draw.line(self.win, (0, 0, 0), ((1/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((1/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((1/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((1/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((1/2)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((1/2)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((2/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((2/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((5/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((5/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))

        # b/w Yellow and Green
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (1/2)*(3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10, (1/2)*(3.8*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (2/3)*(3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10, (2/3)*(3.8*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, (5/6)*(3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10, (5/6)*(3.8*sw)//10 + (sh-sw)//2))

        # b/w Yellow and Blue
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10 + (1/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10 + (1/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10 + (1/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10 + (1/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10 + (1/2)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10 + (1/2)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2),
                         ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))

        # b/w Red and Blue
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, sh - (1/6)*(3.8*sw)//10 - (sh-sw)//2),
                         ((6.2*sw)//10, sh - (1/6)*(3.8*sw)//10 - (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, sh - (1/3)*(3.8*sw)//10 - (sh-sw)//2),
                         ((6.2*sw)//10, sh - (1/3)*(3.8*sw)//10 - (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, sh - (1/2)*(3.8*sw)//10 - (sh-sw)//2),
                         ((6.2*sw)//10, sh - (1/2)*(3.8*sw)//10 - (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, sh - (2/3)*(3.8*sw)//10 - (sh-sw)//2),
                         ((6.2*sw)//10, sh - (2/3)*(3.8*sw)//10 - (sh-sw)//2))
        pygame.draw.line(self.win, (0, 0, 0), ((3.8*sw)//10, sh - (5/6)*(3.8*sw)//10 - (sh-sw)//2),
                         ((6.2*sw)//10, sh - (5/6)*(3.8*sw)//10 - (sh-sw)//2))
