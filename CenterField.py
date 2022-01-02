import Field


class CenterField(Field):
    neighbour_count = 6

    def __init__(self, number, resource, position, is_desert=False):
        super().__init__(number, resource, position, is_desert)

    def neighbourhood(self, number):
        pass
