import itertools


class Map:
    def __init__(self, fields):
        self.fields = fields
        self.assign_resource_place()
        self.choose_winners()

    # calculate mean probability for given town placements
    def get_wages(self, resources):
        wages = []
        for element in resources:
            prob0 = self.spot_probability(element[0])
            prob1 = self.spot_probability(element[1])
            wages.append(prob0 + prob1 / 2)
        return wages

    def spot_probability(self, spot):
        probability = 0
        for position in spot:
            field = self.get_certain_field(position)
            chance = getattr(field, "chance")
            probability += chance
        probability = probability / 3
        return probability

    # choose the most probable placement
    def choose_winners(self):
        possible_places = self.all_resources()
        wages = self.get_wages(possible_places)
        winner = possible_places[0]
        highest_prob = wages[0]
        for index, wage in enumerate(wages):
            if wage > highest_prob:
                winner = possible_places[index]
                highest_prob = wage
        print(
            f"Mathematically, the best places for towns are {winner[0]},{winner[1]} with average probability equal to {highest_prob}")

    # get potential placements which assure having all possible resources (except desert)
    def all_resources(self):
        potential_places = []
        target_resources = ["wood", "sheep", "stone", "brick", "wheat"]
        temporary_resources = self.spot_resources
        temporary_spots = self.town_spots
        for index1, spot1 in enumerate(temporary_spots):
            spot1_resources = temporary_resources[index1]
            del temporary_resources[index1]
            del temporary_spots[index1]
            for index2, spot2 in enumerate(temporary_spots):
                current_resources = spot1_resources + temporary_resources[index2]
                if all(x in target_resources for x in current_resources):
                    potential_places.append([spot1, spot2])
        potential_places = self.remove_duplicates(potential_places)
        return potential_places

    @staticmethod
    def remove_duplicates(positions):
        # removing field such as [[4,1,5],[4,5,1]]
        for index, element in enumerate(positions):
            perms = [list(elem) for elem in itertools.permutations(element[1])]
            if element[0] in perms:
                del positions[index]
        # removing same fields throughout whole list
        for perm_index, element in enumerate(positions):
            perm0 = [list(elem) for elem in itertools.permutations(element[0])]
            perm1 = [list(elem) for elem in itertools.permutations(element[1])]
            length = len(positions)
            del_index = perm_index + 1
            while del_index != length:
                if ((positions[del_index][0] in perm0) and (positions[del_index][1] in perm1) or (
                        positions[del_index][1] in perm0) and (positions[del_index][0] in perm1)):
                    del positions[del_index]
                    length = len(positions)
                else:
                    del_index += 1
        return positions

    # get all possible places for towns (excluding edges)
    def places_for_living(self):
        self.town_spots = []
        for iterator in range(4, 8):
            temp_field = self.get_certain_field(iterator)
            self.town_spots += self.divide_trios(getattr(temp_field, "neighbours"),
                                                 iterator,
                                                 getattr(temp_field, "neighbour_count"))
        for iterator in range(13, 17):
            temp_field = self.get_certain_field(iterator)
            self.town_spots += self.divide_trios(getattr(temp_field, "neighbours"),
                                                 iterator,
                                                 getattr(temp_field, "neighbour_count"))

    # divide field's neighbours for trios
    @staticmethod
    def divide_trios(neighbours, position, count):
        trios = []
        if count == 6:
            for i in range(count):
                if i == count - 1:
                    trios.append([position, neighbours[i], neighbours[0]])
                else:
                    trios.append([position, neighbours[i], neighbours[i + 1]])
        else:
            for i in range(count - 1):
                trios.append([position, neighbours[i], neighbours[i + 1]])
        return trios

    def get_certain_field(self, pos):
        for field in self.fields:
            if getattr(field, "position") == pos:
                return field

    # check resources available at different places
    def assign_resource_place(self):
        self.places_for_living()
        self.spot_resources = []
        for spot in self.town_spots:
            self.spot_resources.append([
                self.get_certain_field(spot[0]).resource,
                self.get_certain_field(spot[1]).resource,
                self.get_certain_field(spot[2]).resource,
            ])
