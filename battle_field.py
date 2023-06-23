class BattleField:
    cell_type_empty = ' '
    cell_type_ship1 = '1'
    cell_type_ship2 = '2'
    cell_type_ship3 = '3'
    cell_type_ship4 = '4'
    cell_type_wounded_or_killed = 'Х'
    cell_type_near_ship = '0'
    cell_type_no_ship_after_shoot = 'М'

    def __init__(self):
        self.sea_field = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def show_sea_field(self):
        print('    1    2    3    4    5    6    7    8    9    10')
        print('-' * 55)
        x_axis = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        while x_axis:
            for i in self.sea_field:
                print(x_axis[0], i)
                x_axis.pop(0)

    def cell_empty(self, x, y):
        if self.sea_field[x][y] == BattleField.cell_type_empty:
            return True

    def cell_near_ship(self, x, y):
        if self.sea_field[x][y] == BattleField.cell_type_near_ship:
            return True

    def cell_with_ship(self, x, y):
        if self.sea_field[x][y] in [BattleField.cell_type_ship1, BattleField.cell_type_ship2,
                                    BattleField.cell_type_ship3, BattleField.cell_type_ship4]:
            return True

    def cell_no_ship_after_shoot(self, x, y):
        if self.sea_field[x][y] == BattleField.cell_type_no_ship_after_shoot:
            return True

    def cell_with_wounded_or_killed_ship(self, x, y):
        if self.sea_field[x][y] == BattleField.cell_type_wounded_or_killed:
            return True

    def cell_near_border(self, x, y):
        if x == 0 or x == 9 or y == 0 or y == 9:
            return True

    def cell_top_left_corner(self, x, y):
        if x == 0 and y == 0:
            return True

    def cell_top_right_corner(self, x, y):
        if x == 0 and y == 9:
            return True

    def cell_bottom_left_corner(self, x, y):
        if x == 9 and y == 0:
            return True

    def cell_bottom_right_corner(self, x, y):
        if x == 9 and y == 9:
            return True

    def cell_top_x(self, x):
        if x == 0:
            return True

    def cell_bottom_x(self, x):
        if x == 9:
            return True

    def cell_left_y(self, y):
        if y == 0:
            return True

    def cell_right_y(self, y):
        if y == 9:
            return True

    def create_cell_near_ship(self, x, y):
        if not self.cell_near_border(x, y):
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_top_left_corner(x, y):
            for i in range(x, x+2):
                for j in range(y, y+2):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_top_right_corner(x, y):
            for i in range(x, x+2):
                for j in range(y-1, y+1):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_bottom_left_corner(x, y):
            for i in range(x-1, x+1):
                for j in range(y, y+2):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_bottom_right_corner(x, y):
            for i in range(x-1, x+1):
                for j in range(y-1, y+1):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_top_x(x):
            for i in range(x, x+2):
                for j in range(y-1, y+2):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_left_y(y):
            for i in range(x-1, x+2):
                for j in range(y, y+2):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        elif self.cell_bottom_x(x):
            for i in range(x-1, x+1):
                for j in range(y-1, y+2):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

        # для y == 9
        else:
            for i in range(x-1, x+2):
                for j in range(y-1, y+1):
                    if not self.cell_with_ship(i, j) and not self.cell_with_wounded_or_killed_ship(i, j):
                        self.sea_field[i][j] = BattleField.cell_type_near_ship

    def can_build_to_left(self, x, y, length):
        while self.cell_empty(x, y) and not self.cell_near_ship(x, y):
            if length == 1:
                return True
            if y - length >= -1:
                y -= 1
                length -= 1
            else:
                break
        return False

    def can_build_to_right(self, x, y, length):
        while self.cell_empty(x, y) and not self.cell_near_ship(x, y):
            if length == 1:
                return True
            if y + length <= 10:
                y += 1
                length -= 1
            else:
                break
        return False

    def can_build_to_bottom(self, x, y, length):
        while self.cell_empty(x, y) and not self.cell_near_ship(x, y):
            if length == 1:
                return True
            if x + length <= 10:
                x += 1
                length -= 1
            else:
                break
        return False

    def can_build_to_top(self, x, y, length):
        while self.cell_empty(x, y) and not self.cell_near_ship(x, y):
            if length == 1:
                return True
            if x - length >= -1:
                x -= 1
                length -= 1
            else:
                break
        return False

    def can_shoot_to_top(self, x, y):
        # может ли бот стрелять вверх, чтобы убить раненого
        if not self.cell_top_x(x) and not self.cell_top_left_corner(x, y) and not self.cell_top_right_corner(x, y):
            if (not self.cell_near_ship(x-1, y) and not self.cell_no_ship_after_shoot(x-1, y)
                    and not self.cell_with_wounded_or_killed_ship(x-1, y)):
                return True
        else:
            return False

    def can_shoot_to_bottom(self, x, y):
        # может ли бот стрелять вниз, чтобы убить раненого
        if (not self.cell_bottom_x(x) and not self.cell_bottom_left_corner(x, y)
                and not self.cell_bottom_right_corner(x, y)):
            if (not self.cell_near_ship(x+1, y) and not self.cell_no_ship_after_shoot(x+1, y)
                    and not self.cell_with_wounded_or_killed_ship(x+1, y)):
                return True
        else:
            return False

    def can_shoot_to_left(self, x, y):
        # может ли бот стрелять влево, чтобы убить раненого
        if not self.cell_left_y(y) and not self.cell_top_left_corner(x, y) and not self.cell_bottom_left_corner(x, y):
            if (not self.cell_near_ship(x, y-1) and not self.cell_no_ship_after_shoot(x, y-1)
                    and not self.cell_with_wounded_or_killed_ship(x, y-1)):
                return True
        else:
            return False

    def can_shoot_to_right(self, x, y):
        # может ли бот стрелять вправо, чтобы убить раненого
        if (not self.cell_right_y(y) and not self.cell_top_right_corner(x, y)
                and not self.cell_bottom_right_corner(x, y)):
            if (not self.cell_near_ship(x, y+1) and not self.cell_no_ship_after_shoot(x, y+1)
                    and not self.cell_with_wounded_or_killed_ship(x, y+1)):
                return True
        else:
            return False
