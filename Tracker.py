class Tracker:
    def __init__(self, date, coffee, coffee_dose, total_water, grind_size, time_weight):
        self.date = date
        self.coffee = coffee
        self.dose = coffee_dose
        self.total_water = total_water
        self.grind_size = grind_size
        self.time_weight = time_weight

    def get_date(self):
        return self.date

    def get_ratio(self):
        return self.total_water/self.dose

    def get_coffee(self):
        return self.coffee

    def get_dose(self):
        return self.dose

    def get_water(self):
        return self.total_water

    def set_date(self, date):
        self.date = date

    def set_water(self, water):
        self.total_water = water

    def set_coffee(self, coffee):
        self.coffee = coffee

    def set_dose(self, dose):
        self.dose = dose
