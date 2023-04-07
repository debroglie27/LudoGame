import pygame
import GameManager


def run_game():
    run = True
    while run:
        # If any event occurs
        for event in pygame.event.get():
            # Clicking the Close Button on window
            if event.type == pygame.QUIT:
                run = False
            # Clicking Left Mouse Button (event.button = 1 for Left Mouse Button)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # getting the Mouse Cursor Position
                mouse_pos = pygame.mouse.get_pos()

                # Roll Dice if its rolling time and mouse position is on the dice
                if gameManager.roll and gameManager.dice.box_collider_list[gameManager.turn].collidepoint(mouse_pos):
                    gameManager.dice_roll_logic()

                # Move disc if it's not rolling time and mouse is over a disc
                elif not gameManager.roll and gameManager.Players[gameManager.turn].collide_point(mouse_pos):
                    gameManager.disc_move_logic()

        # If 3 Players Win
        if gameManager.game_over:
            # Delay so that they know the game is over
            pygame.time.delay(3000)
            run = False

    pygame.quit()


if __name__ == "__main__":
    # Initialising the pygame module
    pygame.init()

    # Declaring the Game Manager
    gameManager = GameManager.GameManager()

    # Running the Game
    run_game()
