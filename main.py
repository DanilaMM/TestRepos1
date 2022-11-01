class building:
    year = None
    city = None

    def __init__(self, year, city ):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year", self.year, "City", self.city)

class School(building):
    pass

house = building(2000 , "Moscow")
house2 = building(1999 , "Moscow")
house3 = building(2001 , "Moscow")
house3.get_info()






