import random

from centerField import CenterField
from cornerField import CornerField
from sideField import SideField
from map import Map


def create_fields(fields, number, resource, position):
    if position in (5, 6, 9, 10, 11, 14, 15):
        fields.append(CenterField(number, resource, position))
    elif position in (1, 3, 12, 19, 17, 8):
        fields.append(CornerField(number, resource, position))
    else:
        fields.append(SideField(number, resource, position))
    return fields


if __name__ == '__main__':
    # creating fields list
    resources = [
        "wood", "wood", "wood", "wood", "brick", "brick", "brick", "stone", "stone", "stone", "desert", "sheep",
        "sheep", "sheep", "sheep", "wheat", "wheat", "wheat", "wheat"]
    random.shuffle(resources)
    numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    random.shuffle(numbers)
    seven_index = [index for index, p in enumerate(numbers) if p == 7]
    desert_index = [index for index, p in enumerate(resources) if p == "desert"]
    numbers[seven_index[-1]], numbers[desert_index[-1]] = numbers[desert_index[-1]], numbers[seven_index[-1]]
    resources = tuple(resources)
    numbers = tuple(numbers)
    fields = []
    for pos in range(1, 20):
        fields = create_fields(fields, numbers[pos - 1], resources[pos - 1], pos)
        if resources[pos - 1] == "desert":
            fields[pos - 1].set_desert()

    current_map = Map(fields)
    print("test")
