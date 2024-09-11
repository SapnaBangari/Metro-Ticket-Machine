class Station:
    '''Models each station'''
    def __init__(self, name, distance, cost):
        self.name = name
        self.distance = distance 
        self.cost = cost


class Stations:
    '''Models the stations'''
    def __init__(self):
        self.stations = [
            Station(name="DILSHAD GARDEN", distance=50, cost=50),
            Station(name="SHAHDARA", distance=26, cost=30),
            Station(name="SEELAMPUR", distance=56, cost=60),
            Station(name="RITHALA", distance=30, cost=40),
            Station(name="KASHMIRI GATE", distance=40, cost=40),
            Station(name="NOIDA SECTOR 15", distance=5, cost=10),
            Station(name="MAYUR VIHAR PHASE-I", distance=10, cost=10),
            Station(name="CHANDNI CHAWK", distance=40, cost=30),
            Station(name="NOIDA SECTOR 62", distance=10, cost=10),
            Station(name="DELHI AIRPORT", distance=47, cost=40)
        ]


    def get_stations(self):
        '''Return all the stations'''
        options = ""
        for station in self.stations:
            options = options + f"\n{station.name}, Cost: {station.cost}"
        return options

    def find_station(self, station_name):
        '''Searches the station and return it, if not found return None'''
        for station in self.stations:
            if station.name == station_name:
                return station
        






