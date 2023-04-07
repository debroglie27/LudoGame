import DiscClass


class Player:
    def __init__(self, win, color, radius, initial_pos_list):
        self.window = win
        self.color = color
        self.radius = radius
        self.initial_pos_list = initial_pos_list

        self.discs = []

        self.selected_disc_id = -1

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

    def check_disc_movements(self, dice_roll_val):
        for disc in self.discs:
            if disc.movement and (disc.current_id + dice_roll_val) <= disc.max_current_id:
                return True

        return False

    def check_any_disc_at_start(self):
        for disc in self.discs:
            if disc.current_pos in self.initial_pos_list:
                return True

        return False
