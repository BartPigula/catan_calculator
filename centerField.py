from field import Field


class CenterField(Field):
    neighbour_count = 6

    def __init__(self, number, resource, position, is_desert=False):
        if position not in (5, 6, 9, 10, 11, 14, 15):
            raise Exception("Typed position is not in center")
        super().__init__(number, resource, position, is_desert)
        self.neighbourhood()

    def neighbourhood(self):
        neighbours = {
            5: (1, 2, 6, 10, 9, 4),
            6: (2, 3, 7, 11, 10, 5),
            9: (4, 5, 10, 14, 13, 8),
            10: (5, 6, 11, 15, 14, 9),
            11: (6, 7, 12, 16, 15, 10),
            14: (9, 10, 15, 18, 17, 13),
            15: (10, 11, 16, 19, 18, 14)
        }
        self.neighbours = neighbours[self.position]
