from random import randint


class Food:
    count = 2
    flag = 3
    _food = set()

    def __init__(self, box_size):
        self._box_size = box_size
        self.cooking()

    def cooking(self):
        if len(self._food) < self.count:
            self._food.add((randint(1, self._box_size[0]), (randint(2, self._box_size[1]))))

    def get_food(self):
        return [i for i in self._food]

    def del_food(self, food):
        self._food.discard(food)


