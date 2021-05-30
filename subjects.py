from random import randint


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


class Snake:
    def __init__(self):
        self.direction = 'right'  # right, left, up, down
        self.old_direction = 'right'
        self.body = []
        self.body.append(Cell(25, 14))
        self.head = self.body[0]
        self.old_tip = Cell(1, 1)

    def add_cell(self):
        self.body.append(Cell(1, 1))

    def move(self):
        if self.direction == 'right':
            self.body.insert(0, Cell(self.head.x + 1, self.head.y))
        elif self.direction == 'up':
            self.body.insert(0, Cell(self.head.x, self.head.y - 1))
        elif self.direction == 'left':
            self.body.insert(0, Cell(self.head.x - 1, self.head.y))
        else:
            self.body.insert(0, Cell(self.head.x, self.head.y + 1))
        self.head = self.body[0]
        self.old_tip = self.body[-1]
        self.body.pop(-1)

    def update_direction(self):
        self.old_direction = self.direction

    def hit(self):
        # Проверка на стену
        if self.head.x > 50 or self.head.x < 3 or self.head.y > 18 or self.head.y < 9:
            return True
        # Проверка на тело
        if self.head in self.body[1:]:
            return True
        return False

    def render(self):
        for i in range(1, len(self.body)):
            print('\033[{};{}H█'.format(self.body[i].y, self.body[i].x))
        print('\033[{};{}H '.format(self.old_tip.y, self.old_tip.x))
        print('\033[{};{}H▓'.format(self.head.y, self.head.x))
        print('\033[19;2H')


class Food(Cell):
    def __init__(self, snake):
        super().__init__(randint(3, 50), randint(9, 18))
        while self in snake.body:
            self.x = randint(3, 50)
            self.y = randint(9, 18)

    def render(self):
        print('\033[{};{}HF'.format(self.y, self.x))
