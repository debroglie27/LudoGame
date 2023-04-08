from io import BytesIO
from base64 import b64decode
import pygame
import random
from BinaryImages import dice_binary_images


class Dice:
    def __init__(self, win):
        self.win = win

        # Dice positions based on whose turn it is
        dice_pos_red = (143, 550)
        dice_pos_green = (143, 0)
        dice_pos_yellow = (307, 0)
        dice_pos_blue = (307, 550)

        self.dice_pos = [dice_pos_red, dice_pos_green, dice_pos_yellow, dice_pos_blue]

        # Loading all the images
        self.dice_img_list = self.load_dice_images()

        # Loading the Dice Box Colliders
        self.box_collider_list = self.load_box_collider()

    @staticmethod
    def load_dice_images():
        dice_img_list = []
        for dice_binary_img in dice_binary_images:
            # Decoding the Binary Image
            decoded_dice_img = BytesIO(b64decode(dice_binary_img))
            # Loading a image
            dice_img = pygame.image.load(decoded_dice_img)
            # Resizing the Image
            resized_dice_img = pygame.transform.scale(dice_img, (50, 50))

            # Appending the dice image in dice image list
            dice_img_list.append(resized_dice_img)

        return dice_img_list

    def load_box_collider(self):
        # box collider of dice for red's turn
        box_collider_red = pygame.Rect(self.dice_pos[0][0], self.dice_pos[0][1], 50, 50)
        # box collider of dice for green's turn
        box_collider_green = pygame.Rect(self.dice_pos[1][0], self.dice_pos[1][1], 50, 50)
        # box collider of dice for yellow's turn
        box_collider_yellow = pygame.Rect(self.dice_pos[2][0], self.dice_pos[2][1], 50, 50)
        # box collider of dice for blue's turn
        box_collider_blue = pygame.Rect(self.dice_pos[3][0], self.dice_pos[3][1], 50, 50)

        return box_collider_red, box_collider_green, box_collider_yellow, box_collider_blue

    def update(self, val, turn):
        # Displaying the dice image based on val and turn
        self.win.blit(self.dice_img_list[val], self.dice_pos[turn])

    def roll(self, turn):
        # Generating random integer from 1 to 6, both included
        val = random.randint(1, 6)
        # Update the dice image to display the roll val generated
        self.update(val, turn)

        return val
