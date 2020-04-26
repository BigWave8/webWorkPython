from lab11.main.managers.sort_type import SortType
from lab11.main.managers.stationary_manager import StationaryManager
from lab11.main.models.pen import Pen


class StationeryManagerUtils:

    @staticmethod
    def sort_by_price(stationery_list, sort_reverse=SortType.ASCENDING):
        """
        >>> for stationery in StationeryManagerUtils.sort_by_price(stationeries): print(stationery)
        price: 2, color: purple, producer: Scholz, target age: 18, thickness: 3
        price: 8, color: black, producer: Scholz, target age: 8, thickness: 2
        price: 20, color: black, producer: farri, target age: 8, thickness: 2
        price: 123, color: red, producer: buromax, target age: 30, thickness: 4
        """
        stationery_list.sort(key=lambda stationery: stationery.price_in_hryvnia, reverse=sort_reverse.value)
        return stationery_list

    @staticmethod
    def sort_by_target_age(stationery_list, sort_reverse=SortType.ASCENDING):
        """
        >>> for stationery in StationeryManagerUtils.sort_by_target_age(stationeries): print(stationery)
        price: 20, color: black, producer: farri, target age: 8, thickness: 2
        price: 8, color: black, producer: Scholz, target age: 8, thickness: 2
        price: 2, color: purple, producer: Scholz, target age: 18, thickness: 3
        price: 123, color: red, producer: buromax, target age: 30, thickness: 4
        """
        stationery_list.sort(key=lambda stationery: stationery.target_age, reverse=sort_reverse.value)
        return stationery_list

    @staticmethod
    def sort_by_producer(stationery_list, sort_reverse=SortType.ASCENDING):
        """
        >>> for stationery in StationeryManagerUtils.sort_by_producer(stationeries): print(stationery)
        price: 123, color: red, producer: buromax, target age: 30, thickness: 4
        price: 20, color: black, producer: farri, target age: 8, thickness: 2
        price: 2, color: purple, producer: Scholz, target age: 18, thickness: 3
        price: 8, color: black, producer: Scholz, target age: 8, thickness: 2
        """
        stationery_list.sort(key=lambda stationery: stationery.producer.lower(), reverse=sort_reverse.value)
        return stationery_list


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, extraglobs={'stationeries': [Pen(8, "black", "Scholz", 8, 2),
                                                               Pen(2, "purple", "Scholz", 18, 3),
                                                               Pen(123, "red", "buromax", 30, 4),
                                                               Pen(20, "black", "farri", 8, 2)]})