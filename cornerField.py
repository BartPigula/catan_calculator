from field import Field


class CornerField(Field):
    neighbour_count = 3

    def __init__(self, number, resource, position, is_desert=False):
        if position not in (1, 3, 12, 19, 17, 8):
            raise Exception("Typed position is not in corner")
        super().__init__(number, resource, position, is_desert)
        self.neighbourhood()

    def neighbourhood(self):
        neighbours = {
            1: (2, 5, 4),
            3: (7, 6, 2),
            12: (16, 11, 7),
            19: (18, 15, 16),
            17: (13, 14, 18),
            8: (4, 9, 13)
        }
        self.neighbours = neighbours[self.position]
