import Tasting_Notes, Rating
class Roasted_Coffee:
    def __init__(name, roaster, country, region, farm, altitude, species, varietal, process, roast_level, tasting_notes, flavor_catagories, rating):
        assert isinstance(roaster, "Roaster")
        for note in tasting_notes:
            assert isinstance(note, 

        self.name = name
        self.roaster = Roasters(roaster)
        self.origin = {"Country": country, "Region": region, "Farm": farm}
        self.altitude = altitude
        self.coffee_plant = {"Species":species, "Varietal":varietal}
        self.process = process
        self.roast_level = roast_level
        self.tasting_notes = tasting_notes
        self.rating = Rating(rating)

    # Return the various properties of the roasted coffee
    def get_name(self):
        return self.name

    def get_roaster(self):
        return self.roaster

    def get_origin(self):
        return self.origin
    
    def get_altitude(self):
        return self.altitude

    def get_plant_type(self):
        return self.coffee_plant

    def get_roast_level(self):
        return self.roast_level

    def get_process(self):
        return self.process

    def get_tasting_notes(self):
        return self.tasting_notes

    def get_flavor_catagories(self):
        return [notes.get_flavor() for notes in tasting_notes]

    def get_rating(self):
        return self.rating
    
    # Set the various properties of the roasted coffee
    def set_name(self, name):
        self.name = name

    def set_roaster(self, roaster_name):
        self.roaster = Roaster(roaster_name)

    def set_origin(self, key, value):
        self.origin[key] = value
    
    def set_altitude(self, altitude):
        self.altitude = altitude

    def set_plant_type(self, key, value):
        self.coffee_plant[key] = value

    def set_roast_level(self, roast_level):
        self.roast_level = roast_level

    def set_process(self, process):
        self.process = process

    def set_tasting_notes(self, tasting_notes):
        self.tasting_notes = tasting_notes

    def set_rating(self, rating):
        self.rating = Rating(rating)
