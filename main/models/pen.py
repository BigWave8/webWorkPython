from lab11.main.models.abstract_stationery import AbstractStationery


class Pen(AbstractStationery):

    def __init__(self, price_in_hryvnia, color, producer, target_age,
                 thickness_of_rod_in_millimeters):
        super().__init__(price_in_hryvnia, color, producer, target_age)
        self.thickness_of_rod_in_millimeters = thickness_of_rod_in_millimeters

    def __str__(self):
        return super().__str__() + ", thickness: %d" % self.thickness_of_rod_in_millimeters
