import random
import ship
import battle_field


class Player:
    def __init__(self):
        self.used_coordinates = []  # хранить координаты куда я стрелял, чтобы не повторяться.
        self.wounded_ship_coordinates = []  # хранить координаты раненого корабля, чтобы скорее убить.
        self.shoot_direction = []  # хранить направления, в которые можно стрелять, чтобы скорее убить раненого
        self.dont_shoot_to_this_direction = []  # куда ужа не имеет смысла стрелять (раню вверх\вниз, то лево\право нет)

    def name_generator(self):
        names = ['Капитан Джек Воробей', 'Аквамен', 'Адмирал', 'Капитан Немо', 'Бездна', 'Ихтиандр', 'Морское чудище',
                 'Пират', 'Русалочка', 'Годзилла', 'Ктулху', 'Глубоководный', 'Немор', 'Нептун', 'Водяной']
        self.name = random.choice(names)

    def name_creation(self):
        print('Введите имя (и нажмите Enter): ')
        entered_name = input()
        if entered_name == '':
            print('У тебя должно же быть какое-то имя, вспомни его')
            Player.name_creation(self)
        else:
            self.name = entered_name

    def player_ships(self):
        self.my_ships = []
        self.ship0 = ship.Ship('однопалубный')
        self.my_ships.append(self.ship0)
        self.ship1 = ship.Ship('однопалубный')
        self.my_ships.append(self.ship1)
        self.ship2 = ship.Ship('однопалубный')
        self.my_ships.append(self.ship2)
        self.ship3 = ship.Ship('однопалубный')
        self.my_ships.append(self.ship3)
        self.ship4 = ship.Ship('двухпалубный')
        self.my_ships.append(self.ship4)
        self.ship5 = ship.Ship('двухпалубный')
        self.my_ships.append(self.ship5)
        self.ship6 = ship.Ship('двухпалубный')
        self.my_ships.append(self.ship6)
        self.ship7 = ship.Ship('трёхпалубный')
        self.my_ships.append(self.ship7)
        self.ship8 = ship.Ship('трёхпалубный')
        self.my_ships.append(self.ship8)
        self.ship9 = ship.Ship('четырёхпалубный')
        self.my_ships.append(self.ship9)
        self.live_ones = [self.ship0, self.ship1, self.ship2, self.ship3]
        self.live_twos = [self.ship4, self.ship5, self.ship6]
        self.live_threes = [self.ship7, self.ship8]
        self.live_fours = [self.ship9]

    def player_live_ships_update(self):
        for s in self.my_ships:
            if s.ship_status == ship.Ship.ship_all_statuses[2]:
                if s.ship_type == ship.Ship.ship_all_types[0]: self.live_ones.pop()
                elif s.ship_type == ship.Ship.ship_all_types[1]: self.live_twos.pop()
                elif s.ship_type == ship.Ship.ship_all_types[2]: self.live_threes.pop()
                else: self.live_fours.pop()

    def player_available_ships(self):
        # доступные корабли для ручной расстановки
        self.list_ones = [self.ship0, self.ship1, self.ship2, self.ship3]
        self.list_twos = [self.ship4, self.ship5, self.ship6]
        self.list_threes = [self.ship7, self.ship8]
        self.list_fours = [self.ship9]
        self.player_available_ship_count = len(self.my_ships)
        self.player_updated_ships()

    def player_updated_ships(self):
        # обновление информации о доступных кораблях для ручной расстановки
        print('количество однопалубных:', len(self.list_ones))
        print('количество двухпалубных:', len(self.list_twos))
        print('количество трёхпалубных:', len(self.list_threes))
        print('количество четырёхпалубных:', len(self.list_fours))
        print('всего осталось разместить кораблей:', self.player_available_ship_count)

    def player_set_ship(self):
        set_ship_type, xy = input().split()
        self.temp_ship_type = set_ship_type
        self.temp_xy = xy

    def player_save_ship(self):
        self.player_set_ship()
        if self.temp_ship_type == '1' and self.list_ones:
            for i in self.list_ones:
                i.ship_xy = self.temp_xy
                break
            self.list_ones.pop()
            self.player_available_ship_count -= 1
        if self.temp_ship_type == '2' and self.list_twos:
            for i in self.list_twos:
                i.ship_xy = self.temp_xy
                break
            self.list_twos.pop()
            self.player_available_ship_count -= 1
        if self.temp_ship_type == '3' and self.list_threes:
            for i in self.list_threes:
                i.ship_xy = self.temp_xy
                break
            self.list_threes.pop()
            self.player_available_ship_count -= 1
        if self.temp_ship_type == '4' and self.list_fours:
            for i in self.list_fours:
                i.ship_xy = self.temp_xy
                break
            self.list_fours.pop()
            self.player_available_ship_count -= 1

    def player_has_opponent_field(self):
        self.opponent_field = battle_field.BattleField()

    def player_random_ship_location(self):
        self.my_field = battle_field.BattleField()
        for i in self.my_ships[::-1]:  # от больших кораблей к меньшим, чтобы большим было больше места для расстановки
            while i.ship_used == 0:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                temp_directions = []
                if self.my_field.cell_empty(x, y) and not self.my_field.cell_near_ship(x, y):
                    if self.my_field.can_build_to_top(x, y, i.ship_len):
                        temp_directions.append(ship.Ship.ship_all_directions[2])

                    if self.my_field.can_build_to_bottom(x, y, i.ship_len):
                        temp_directions.append(ship.Ship.ship_all_directions[3])

                    if self.my_field.can_build_to_left(x, y, i.ship_len):
                        temp_directions.append(ship.Ship.ship_all_directions[0])

                    if self.my_field.can_build_to_right(x, y, i.ship_len):
                        temp_directions.append(ship.Ship.ship_all_directions[1])

                    if not temp_directions:
                        continue

                    i.ship_direction = random.choice(temp_directions)
                    if i.ship_direction == ship.Ship.ship_all_directions[0]:
                        for ship_part in range(i.ship_len):
                            if i.ship_len == 1:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship1
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                            elif i.ship_len == 2:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship2
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                y -= 1
                            elif i.ship_len == 3:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship3
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                y -= 1
                            else:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship4
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                y -= 1
                        i.ship_used = 1

                    elif i.ship_direction == ship.Ship.ship_all_directions[1]:
                        for ship_part in range(i.ship_len):
                            if i.ship_len == 1:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship1
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                            elif i.ship_len == 2:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship2
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                y += 1
                            elif i.ship_len == 3:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship3
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                y += 1
                            else:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship4
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                y += 1
                        i.ship_used = 1

                    elif i.ship_direction == ship.Ship.ship_all_directions[2]:
                        for ship_part in range(i.ship_len):
                            if i.ship_len == 1:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship1
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                            elif i.ship_len == 2:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship2
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                x -= 1
                            elif i.ship_len == 3:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship3
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                x -= 1
                            else:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship4
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                x -= 1
                        i.ship_used = 1

                    # для bottom
                    else:
                        for ship_part in range(i.ship_len):
                            if i.ship_len == 1:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship1
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                            elif i.ship_len == 2:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship2
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                x += 1
                            elif i.ship_len == 3:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship3
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                x += 1
                            else:
                                self.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_ship4
                                self.my_field.create_cell_near_ship(x, y)
                                i.ship_coordinates.append(str(x) + str(y))
                                x += 1
                        i.ship_used = 1

        '''
        нижний цикл для того, чтобы после генерации кораблей игроку выводить его нормальное поле только с кораблями
        без нулей. 
        '''
        for m in range(len(self.my_field.sea_field)):
            for n in range(len(self.my_field.sea_field)):
                if self.my_field.sea_field[m][n] == battle_field.BattleField.cell_type_near_ship:
                    self.my_field.sea_field[m][n] = battle_field.BattleField.cell_type_empty

    def show_player_random_ships_on_field(self):
        print('    1    2    3    4    5    6    7    8    9    10')
        print('-' * 55)
        x_axis = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        while x_axis:
            for d in self.my_field.sea_field:
                print(x_axis[0], d)
                x_axis.pop(0)
