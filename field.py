class Field:
    desert = False

    def __init__(self, number, resource, position, is_desert=False):
        if any((number > 12, number < 2)):
            raise Exception("number must be bigger than 1 and smaller than 13")
        if resource not in ["wood", "wheat", "brick", "stone", "sheep", "desert"]:
            raise Exception("Resource should be one of: wood, wheat, brick, stone, sheep, desert")
        if is_desert:
            self.desert = True
        if any((position < 1, position > 19)):
            raise Exception("Wrong position, must be in range from 1 to 19")
        self.number = number
        self.resource = resource
        self.calc_probability()
        self.position = position

    def calc_probability(self):
        probabilities = {
            2: (1 / 36),
            3: (1 / 18),
            4: (1 / 12),
            5: (1 / 9),
            6: (5 / 36),
            7: (1 / 6),
            8: (5 / 36),
            9: (1 / 9),
            10: (1 / 12),
            11: (1 / 18),
            12: (1 / 36)
        }
        self.chance = probabilities[self.number]

    def __str__(self):
        return f"{self.resource} with number {self.number}, probability: {self.chance}"

    def set_desert(self):
        self.desert = True
