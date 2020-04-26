from lab11.main.models.abstract_stationery import AbstractStationery
from lab11.main.models.pen import Pen


class StationaryManager:

    def __init__(self, stationery_list):
        self.stationery_list = stationery_list

    def add_stationery(self, stationery: AbstractStationery):
        self.stationery_list.append(stationery)

    def add_stationeries(self, stationeries: list):
        self.stationery_list.extend(stationeries)

    def find_by_target_age(self, target_age):
        """
        >>> for stationery in stationery_manager.find_by_target_age(8) : print(stationery)
        price: 8, color: black, producer: Scholz, target age: 8, thickness: 2
        price: 20, color: black, producer: farri, target age: 8, thickness: 2
        """
        return list(filter(lambda stationery: stationery.target_age == target_age, self.stationery_list))

    def find_by_price(self, price):
        """
        >>> for stationery in stationery_manager.find_by_price(20) : print(stationery)
        price: 20, color: black, producer: farri, target age: 8, thickness: 2
        """
        return list(filter(lambda stationery: stationery.price_in_hryvnia == price, self.stationery_list))

    def find_by_producer(self, producer):
        """
        >>> for stationery in stationery_manager.find_by_producer("farri") : print(stationery)
        price: 20, color: black, producer: farri, target age: 8, thickness: 2
        """
        return list(filter(lambda stationery: stationery.producer == producer, self.stationery_list))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, extraglobs={'stationery_manager': StationaryManager([Pen(8, "black", "Scholz", 8, 2),
                                                                                       Pen(2, "purple", "Scholz", 18,
                                                                                           3),
                                                                                       Pen(123, "red", "buromax", 30,
                                                                                           4),
                                                                                       Pen(20, "black", "farri", 8,
                                                                                           2)])})
