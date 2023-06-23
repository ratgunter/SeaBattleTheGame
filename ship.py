class Ship:
    ship_all_types = ['однопалубный', 'двухпалубный', 'трёхпалубный', 'четырёхпалубный']
    ship_all_statuses = ['целый', 'ранен', 'убит']
    ship_all_directions = ['влево', 'вправо', 'вверх', 'вниз']

    def __init__(self, ship_type):
        self.ship_type = ship_type
        self.ship_coordinates = []
        self.ship_direction = []
        self.ship_status = Ship.ship_all_statuses[0]
        self.ship_used = 0
        if self.ship_type == Ship.ship_all_types[0]:
            self.ship_lives = 1
            self.ship_len = 1
        if self.ship_type == Ship.ship_all_types[1]:
            self.ship_lives = 2
            self.ship_len = 2
        if self.ship_type == Ship.ship_all_types[2]:
            self.ship_lives = 3
            self.ship_len = 3
        if self.ship_type == Ship.ship_all_types[3]:
            self.ship_lives = 4
            self.ship_len = 4

    def ship_was_used(self):
        self.ship_used = 1

    def ship_was_wounded(self):
        self.ship_lives -= 1
        self.ship_status = Ship.ship_all_statuses[1]

    def ship_killed(self):
        if self.ship_lives == 0:
            self.ship_status = Ship.ship_all_statuses[2]
            return True
