import DiscClass


class Player:
    def __init__(self, win, color, radius, initial_pos_list):
        self.window = win
        self.color = color
        self.radius = radius
        self.initial_pos_list = initial_pos_list

        self.discs = []

        self.selected_disc_id = None

        for _id, initial_pos in enumerate(self.initial_pos_list):
            disc = DiscClass.Disc(self.window, self.color, self.radius, initial_pos, _id)
            self.discs.append(disc)

        self.dice_roll_index = 0
        self.dice_rolls = [0, 0, 0]

    def update(self):
        for disc in self.discs:
            disc.update()

    def collide_point(self, mouse_pos):
        for disc in self.discs:
            if disc.box_collider.collidepoint(mouse_pos):
                self.selected_disc_id = disc.disc_id
                return True

        return False

    def check_all_player_discs_reached_home(self):
        for disc in self.discs:
            if disc.current_index != disc.max_current_index:
                return False

        return True

    def check_any_disc_moves_possible(self, dice_roll_val):
        # Bool value representing whether any disc, for that particular player, is at starting position
        anyDiscAtStart = self.check_any_disc_at_start()
        # Bool value representing whether any disc, for that particular player, can move or not
        anyDiscWhichCanMove = self.check_any_disc_can_move(dice_roll_val)

        if (dice_roll_val == 6 and anyDiscAtStart) or anyDiscWhichCanMove:
            return True
        else:
            return False

    def check_any_disc_can_move(self, dice_roll_val: int) -> bool:
        """
        :param dice_roll_val:

        Returns True if any player discs has 'movement' bool variable
        as True and the disc has area to move to, otherwise False.
        """
        for disc in self.discs:
            if disc.movement and (disc.current_index + dice_roll_val) <= disc.max_current_index:
                return True

        return False

    def check_any_disc_at_start(self):
        for disc in self.discs:
            if disc.current_pos in self.initial_pos_list:
                return True

        return False

    @staticmethod
    def check_disc_at_start(disc_to_be_checked):
        if disc_to_be_checked.current_index == 0:
            return True
        else:
            return False

    def store_dice_roll_values(self, dice_roll_val):
        self.dice_rolls[self.dice_roll_index] = dice_roll_val
        self.dice_roll_index = (self.dice_roll_index + 1) % 3
