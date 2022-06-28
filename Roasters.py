class Roaster:
    def __init__(self, name, location, coffee=None):
        self.name = name
        self.location = location
        self.coffee = coffee

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_coffees(self):
        return self.coffees

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def remove_coffee(self, remove_this_coffee):
        assert isinstance(remove_this_coffee, "Roasted_Coffee")
        coffee_lst_len = len(self.coffee)
        self.coffee = [coffee_bag for coffee_bag in self.coffee if coffee_bag is not remove_this_coffee]
        return f"Sucessfully removed: {remove_this_coffee.get_name()}" if self.coffee < coffee_lst_len else f"The coffee was is not a part of the roaster collection"

    def add_coffee(self, add_coffee):
        assert isinstance(add_coffee, "Roasted_Coffee")
        self.coffee.append(add_coffee)
        
