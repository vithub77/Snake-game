class Snake:
    _id = 1

    def __init__(self, cx, cy):
        self.id = Snake._id
        self.current_coordinates = [cx, cy]
        self.before_coordinates = [None, None]
        self.tail = None
        Snake._id += 1

    def add_tail(self):
        if self.tail is None:
            self.tail = Snake(self.before_coordinates[0], self.before_coordinates[1])
        else:
            runner = self
            while runner.tail:
                runner = runner.tail
            runner.tail = Snake(runner.before_coordinates[0], runner.before_coordinates[1])

    def get_coordinates(self):
        return self.current_coordinates

    def update_coordinates(self, crd):
        if self.tail is None or self.id == 1:
            self.before_coordinates[:] = self.current_coordinates[:]
            self.current_coordinates[0] += crd[0]
            self.current_coordinates[1] += crd[1]
        runner = self
        while runner.tail:
            runner.tail.before_coordinates[:] = runner.tail.current_coordinates[:]
            runner.tail.current_coordinates[:] = runner.before_coordinates[:]
            runner = runner.tail

    def get_snake(self):
        runner = self
        while runner:
            yield runner
            runner = runner.tail
