from lab11.main.models.abstract_stationery import AbstractStationery


class Pensil(AbstractStationery):

    def __init__(self, price_in_hryvnia, color, producer, target_age, hardeness_of_slate):
        super().__init__(price_in_hryvnia, color, producer, target_age)
        self.hardeness_of_slate = hardeness_of_slate

    def __str__(self):
        return super().__str__() + ", hardeness: %d" % self.hardeness_of_slate