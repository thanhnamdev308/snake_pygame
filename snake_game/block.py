WINDOW_SIDE = 840
BLOCK_SIDE = 40


class Block:
    """
    A block on the grid
    """

    def __init__(self, x: int = 200, y: int = 200) -> None:
        self.x = x
        self.y = y

    def move_right(self):
        self.x = (self.x + BLOCK_SIDE) % WINDOW_SIDE

    def move_left(self):
        self.x = (self.x - BLOCK_SIDE) % WINDOW_SIDE

    def move_down(self):
        self.y = (self.y + BLOCK_SIDE) % WINDOW_SIDE

    def move_up(self):
        self.y = (self.y - BLOCK_SIDE) % WINDOW_SIDE
