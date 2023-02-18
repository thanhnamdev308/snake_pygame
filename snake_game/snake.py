from block import Block

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


class Snake:
    """
    This class represent Snake
    """

    def __init__(self) -> None:
        self.head = Block()
        self.body = []
        self.alive = True
        self.growing = False
        self.direction = RIGHT
        self.size = 0

    def update_body(self, prev_head_block: Block) -> None:
        """ Update body along with head position and
        current snake size

        Args:
            prev_head_block (Block): the previous head block
                                     to check if the snake die
        """

        # Check if the snake die already
        for block in self.body:
            if (block.x == prev_head_block.x) and (block.y == prev_head_block.y):
                self.alive = False

        # If not, move the body along with the head
        self.body.append(prev_head_block)

        # Delete the tail block if snake is not growing (by eating food)
        if not self.growing:
            self.body.pop(0)
        else:
            # Otherwise grow one block
            self.size += 1
            self.growing = False

    def move_right(self):
        prev_head_block = Block(self.head.x, self.head.y)
        self.head.move_right()
        self.update_body(prev_head_block)

    def move_left(self):
        prev_head_block = Block(self.head.x, self.head.y)
        self.head.move_left()
        self.update_body(prev_head_block)

    def move_down(self):
        prev_head_block = Block(self.head.x, self.head.y)
        self.head.move_down()
        self.update_body(prev_head_block)

    def move_up(self):
        prev_head_block = Block(self.head.x, self.head.y)
        self.head.move_up()
        self.update_body(prev_head_block)

    def run(self) -> None:
        if self.direction == RIGHT:
            self.move_right()
        if self.direction == LEFT:
            self.move_left()
        if self.direction == UP:
            self.move_up()
        if self.direction == DOWN:
            self.move_down()
