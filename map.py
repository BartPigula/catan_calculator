class Map:
    def __init__(self, fields):
        self.fields = fields
        self.assign_resource_place()
        res = self.all_resources()
        print("test")

    # calculate mean probability for given town placements
    def get_wages(self):
        pass

    # choose the most probable placement
    def choose_winners(self):
        pass

    # get potential placements which assure having all possible resources (except desert)
    def all_resources(self):
        potential_places = []
        target_resources = ["wood", "sheep", "stone", "brick", "wheat"]
        for index1, spot1 in enumerate(self.town_spots):
            spot1_resources = self.spot_resources[index1]
            temporary_spots = self.town_spots
            temporary_spots.remove(spot1)
            for index2, spot2 in enumerate(temporary_spots):
                temporary_resources = spot1_resources + self.spot_resources[index2]
                # DOESNT WORK, BETTER CHECKING WHETHER ALL RESOURCES ARE IN CHOSEN PLACES
                if all(x in target_resources for x in temporary_resources):
                    potential_places.append([spot1, spot2])
        return potential_places

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
                trios.append((position, neighbours[i], neighbours[i + 1]))
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
