from field import Field


class SideField(Field):
    neighbour_count = 4

    def __init__(self, number, resource, position, is_desert=False):
        if position not in (2, 7, 16, 18, 13, 4):
            raise Exception("Typed position is not on side")
        super().__init__(number, resource, position, is_desert)
        self.neighbourhood()

    def neighbourhood(self):
        neighbours = {
            2: (1, 5, 6, 3),
            7: (3, 6, 11, 12),
            16: (12, 11, 15, 19),
            18: (17, 14, 15, 19),
            13: (8, 9, 14, 17),
            4: (1, 5, 9, 8)
        }
        self.neighbours = neighbours[self.position]
