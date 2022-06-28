class Ratings:
    def __init__(self, rating):
        assert rating >= 1 and rating <= 10
        self.rating = rating

    def __str__(self):
        closed_circles = "•"*self.rating
        open_circles = "○"*(10-self.rating)
        return closed_circles + open_circles
