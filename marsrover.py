class Rover(object):
    left_movements = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    right_movements = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y += 1
        if self.direction == 'S':
            self.y -= 1
        if self.direction == 'E':
            self.x += 1
        if self.direction == 'W':
            self.x -= 1

    def turn(self, dir):
        # if dir == 'L' and self.direction == 'N':
        #     self.direction = 'W'
        # elif dir == 'L' and self.direction == 'W':
        #     self.direction = 'S'
        # elif dir == 'L' and self.direction == 'S':
        #     self.direction = 'E'
        # elif dir == 'L' and self.direction == 'E':
        #     self.direction = 'N'
        if dir == 'L':
            self.direction = self.left_movements[self.direction]
        if dir == 'R':
            self.direction = self.right_movements[self.direction]

    def execute(self, instruction_string):
        for i in list(instruction_string):
            if i == 'M':
                self.move()
            else:
                self.turn(i)
