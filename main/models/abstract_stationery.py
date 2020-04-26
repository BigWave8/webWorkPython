from abc import ABC


class AbstractStationery(ABC):

    def __init__(self, price_in_hryvnia, color, producer, target_age):
        self.price_in_hryvnia = price_in_hryvnia
        self.color = color
        self.producer = producer
        self.target_age = target_age

    def __str__(self):
        return "price: %d, color: %s, producer: %s, target age: %d" % (
            self.price_in_hryvnia, self.color, self.producer, self.target_age)