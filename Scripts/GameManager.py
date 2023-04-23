import DiceClass
import PathClass
import BoardClass
import pygame


class GameManager:
    def __init__(self):
        # Initialising the pygame module
        pygame.init()

        # Screen Width and Height
        self.screen_width = 500
        self.screen_height = 600
        # Window Caption
        pygame.display.set_caption("Ludo Game")
        # Window Screen
        self.win = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Signifies whose turn it is to roll dice -- 0 means Player Red's turn
        self.turn = 0
        # Signifies the dice roll value and also the index for displaying dice images
        self.val = 0
        # Signifies whether its dice roll time or not
        self.roll = True
        # Signifies whether the game is over or not
        self.game_over = False

        # Delay (in ms)
        self.delay = 1400

        # Initialising the Board Class
        self.board = BoardClass.Board(self.win, self.screen_width, self.screen_height)

        # Displaying the Board
        self.board.display()

        # Initialising the dice
        self.dice = DiceClass.Dice(self.win)
        self.dice.update(self.val, self.turn)

        # Loading the Players
        self.Players = self.board.load_players()

        # Saving the Current Status in the status_list
        self.status_index = 0
        self.status_list = [{}, {}, {}]

        # Save the Status of all the discs
        self.save_status()

        # Disc to Eliminate
        self.disc_to_eliminate = None

        # Initialising the path class which stores all the information
        # regarding which path the disc would follow
        self.disc_path = PathClass.Path()

        # First Update so that game screen is visible
        self.update()

    def update(self):
        """
        Updates the game board along with the Players and dice.
        """
        # Displaying the Game Board
        self.board.display()

        # Updating the Player's Discs
        for index in range(0, 4):
            self.Players[index].update()

        # Updating the player's discs, whose turn it is, last
        self.Players[self.turn].update()

        # Updating the dice accordingly
        self.dice.update(self.val, self.turn)

        # Updating the screen display
        pygame.display.update()

    def dice_roll_logic(self):
        """
        Takes care of the logic needed when rolling a die.
        """
        # Getting the dice roll value
        self.val = self.dice.roll(self.turn)

        # Checking whether all player's discs have reached home
        if self.Players[self.turn].check_all_player_discs_reached_home():
            # Skipping the player's turn because the player has already won
            self.turn = (self.turn + 1) % 4
            return

        # Storing the dice roll values for player whose turn it was
        self.Players[self.turn].store_dice_roll_values(self.val)

        # Update so that player can see the dice roll
        self.update()

        # Checking whether 3 consecutive sixes
        if self.check_3_consecutive_six():
            # Delay so that the player can see the last six on 3 consecutive sixes
            pygame.time.delay(self.delay)
            # Restores the status of player before rolling 3 consecutive six
            self.restore_status()
            return

        # Checking whether the Player Can move any of its disc according to the dice roll
        if self.Players[self.turn].check_any_disc_moves_possible(self.val):
            self.roll = False
        else:
            # Delay so that the player can notice the roll result
            pygame.time.delay(self.delay)

            self.turn = (self.turn + 1) % 4
            self.val = 0

            # Update so that dice goes to next player
            self.update()

    def disc_move_logic(self):
        """
        Takes care of the logic when player moves a disc.
        """
        # The selected disc to be moved
        disc_selected = self.Players[self.turn].discs[self.Players[self.turn].selected_disc_id]

        # Will enter when selected disc is at start and dice roll value = 6
        if self.Players[self.turn].check_disc_at_start(disc_selected) and self.val == 6:
            # Selected disc moves to the starting position and here current_index is 0
            disc_selected.current_pos = self.disc_path.path_lists[self.turn][disc_selected.current_index]
            # Selected disc's movement ability is made True which was initially False
            disc_selected.movement = True

            # Now we can roll the dice
            self.roll = True
            self.val = 0

        elif disc_selected.movement:
            # Selected disc's current id and current position gets updated
            disc_selected.current_index = disc_selected.current_index + self.val
            disc_selected.current_pos = self.disc_path.path_lists[self.turn][disc_selected.current_index]

            # Enter if selected disc has reached Home
            if disc_selected.current_index == disc_selected.max_current_index:
                disc_selected.movement = False
                # Giving another rolling chance for making the disc go Home
                self.roll = True
                self.val = 0
                # Update so that the changes are visible on the screen
                self.update()

                if self.check_game_over():
                    self.game_over = True

                return

            # Checking whether the selected disc eliminated some other disc
            elimination_bool = self.check_elimination(disc_selected)
            if elimination_bool:
                # Restart the eliminated disc
                self.disc_to_eliminate.respawn()

            # If dice roll not 6 and no elimination took place then we are going to change turn
            if self.val != 6 and not elimination_bool:
                self.turn = (self.turn + 1) % 4

            # Now we can roll the dice
            self.roll = True
            self.val = 0

        # Update so that the changes are visible on the screen
        self.update()

        # Save the Status of all the discs
        self.save_status()

    def check_elimination(self, disc_selected):
        """
        :param disc_selected:

        Returns True if disc_selected eliminates any opponent disc,
        otherwise Returns False.
        """
        if disc_selected.current_pos in self.board.safe_positions:
            return False

        for player in self.Players:
            count = 0
            for disc in player.discs:
                # Same color disc will never eliminate each other so continue
                if disc.color == disc_selected.color:
                    continue

                # Different color disc will eliminate each other only if their positions are same
                if disc_selected.current_pos == disc.current_pos:
                    self.disc_to_eliminate = disc
                    count += 1

            # Making sure there is only one opponent disc to eliminate, otherwise no elimination
            if count == 1:
                return True

        return False

    def check_3_consecutive_six(self):
        """
        Returns True if player has rolled six 3 times in a row,
        otherwise False.
        """
        if self.Players[self.turn].dice_rolls == [6, 6, 6]:
            return True
        else:
            return False

    def check_game_over(self):
        """
        Returns True if 3 players won the game, otherwise False.
        """
        count_list = [0, 0, 0, 0]
        for index, player in enumerate(self.Players):
            for disc in player.discs:
                if disc.current_index != disc.max_current_index:
                    count_list[index] += 1

        if count_list.count(4) == 3:
            return True
        else:
            return False

    def save_status(self):
        """
        Saves status of the board.
        """
        # Saving Status of every disc
        self.status_list[self.status_index] = self.board.current_status()
        self.status_index = (self.status_index + 1) % 3

    def restore_status(self):
        """
        Restores status of the board where it was 3 dice moves ago.
        """
        restore_status_index = self.status_index
        # Incrementing status index so that it starts storing new statuses not from the current status
        self.status_index = (self.status_index + 1) % 3
        restore_status = self.status_list[restore_status_index]

        # Restoring the current position, current id and movement bool of all discs under all players
        for player in self.Players:
            player_discs_restore_val = restore_status[player]
            for index, disc in enumerate(player.discs):
                disc.current_pos = player_discs_restore_val[index][0]
                disc.current_index = player_discs_restore_val[index][1]
                disc.movement = player_discs_restore_val[index][2]

        # Reinitialising the dice rolls and dice roll index of the player throwing 3 consecutive six
        self.Players[self.turn].dice_rolls = [0, 0, 0]
        self.Players[self.turn].dice_roll_index = 0

        # Player will lose its turn after 3 consecutive sixes
        self.turn = (self.turn + 1) % 4
        self.val = 0

        # Update so that the changes are visible on the screen
        self.update()
