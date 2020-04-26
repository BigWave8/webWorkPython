class Marker:

    def __init__(self, price_in_hryvnia, color, producer, target_age, basic):
        super().__init__(price_in_hryvnia, color, producer, target_age)
        self.basic = basic

    def __str__(self):
        return super().__str__() + ", basic: %s" % self.basic