import random
import battle_field
import prepare_game
import ship

if prepare_game.game_mode == 1:
    who_is_shooting = prepare_game.gamer
    who_is_waiting = prepare_game.bot
else:
    who_is_shooting = prepare_game.bot
    who_is_waiting = prepare_game.bot2
round = 1
round_with_kills = []


def whose_turn(player1):
    if prepare_game.game_mode == 1:
        if player1 == prepare_game.gamer:
            who_is_shooting = prepare_game.bot
            who_is_waiting = prepare_game.gamer
        else:
            who_is_shooting = prepare_game.gamer
            who_is_waiting = prepare_game.bot
        return who_is_shooting, who_is_waiting
    else:
        if player1 == prepare_game.bot:
            who_is_shooting = prepare_game.bot2
            who_is_waiting = prepare_game.bot
        else:
            who_is_shooting = prepare_game.bot
            who_is_waiting = prepare_game.bot2
        return who_is_shooting, who_is_waiting


def convert_xy_to_abc123(x, y):
    if x == 0: x = 'А'
    elif x == 1: x = 'Б'
    elif x == 2: x = 'В'
    elif x == 3: x = 'Г'
    elif x == 4: x = 'Д'
    elif x == 5: x = 'Е'
    elif x == 6: x = 'Ж'
    elif x == 7: x = 'З'
    elif x == 8: x = 'И'
    elif x == 9: x = 'К'

    if y == 0: y = 1
    elif y == 1: y = 2
    elif y == 2: y = 3
    elif y == 3: y = 4
    elif y == 4: y = 5
    elif y == 5: y = 6
    elif y == 6: y = 7
    elif y == 7: y = 8
    elif y == 8: y = 9
    elif y == 9: y = 10
    return x, y


def shoot_nothing(who_is_shooting, who_is_waiting, x, y, game_mode, shoot_direction=[]):
    if shoot_direction == 'влево':
        y = y - 1
    elif shoot_direction == 'вправо':
        y = y + 1
    elif shoot_direction == 'вверх':
        x = x - 1
    elif shoot_direction == 'вниз':
        x = x + 1
    else:
        x = x
        y = y

    if shoot_direction:
        if len(who_is_waiting.wounded_ship_coordinates) > 1:  # чтобы при следующей попытке добить корабль ->
            del who_is_waiting.wounded_ship_coordinates[-1]  # ->бот стрелял с первой раненой клетки
        who_is_shooting.dont_shoot_to_this_direction.append(shoot_direction)
        who_is_shooting.used_coordinates.append(str(x) + str(y))
    who_is_shooting.shoot_direction = []
    who_is_shooting.opponent_field.sea_field[x][y] = battle_field.BattleField.cell_type_no_ship_after_shoot
    x, y = convert_xy_to_abc123(x, y)
    print('%s стреляет с координатами %s%s и мажет на поле соперника' % (who_is_shooting.name, x, y))
    who_is_shooting.opponent_field.show_sea_field()
    print()
    if game_mode == 1:
        if who_is_waiting == prepare_game.gamer:
            input('жми Enter для продолжения...')
            print('%s, вот твои корабли:' % who_is_waiting.name)
            who_is_waiting.my_field.show_sea_field()
            input('жми Enter для продолжения...')
        else:
            input('жми Enter для продолжения...')
    else:
        print('У игрока', who_is_waiting.name, 'поле не изменилось, так как соперник промахнулся')
        who_is_waiting.my_field.show_sea_field()
    print()
    return False


def shoot_killed(who_is_shooting, who_is_waiting, x, y, ship_index, game_mode, shoot_direction=[]):
    if shoot_direction == 'влево':
        y = y - 1
    elif shoot_direction == 'вправо':
        y = y + 1
    elif shoot_direction == 'вверх':
        x = x - 1
    elif shoot_direction == 'вниз':
        x = x + 1
    else:
        x = x
        y = y

    if shoot_direction:
        who_is_shooting.used_coordinates.append(str(x) + str(y))
    who_is_shooting.dont_shoot_to_this_direction = []
    who_is_waiting.wounded_ship_coordinates = []
    who_is_shooting.shoot_direction = []
    who_is_waiting.player_live_ships_update()
    who_is_shooting.opponent_field.sea_field[x][y] = battle_field.BattleField.cell_type_wounded_or_killed
    for c in who_is_waiting.my_ships[ship_index].ship_coordinates:
        who_is_shooting.opponent_field.create_cell_near_ship(int(c[0]), int(c[1]))
    who_is_waiting.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_wounded_or_killed
    who_is_waiting.my_ships.pop(ship_index)
    x, y = convert_xy_to_abc123(x, y)
    print('%s стреляет с координатами %s%s и уничтожает корабль на поле соперника' % (who_is_shooting.name, x, y))
    who_is_shooting.opponent_field.show_sea_field()
    print()
    if game_mode == 1:
        if who_is_waiting == prepare_game.gamer:
            input('жми Enter для продолжения...')
            print('%s, вот твои корабли:' % who_is_waiting.name)
            who_is_waiting.my_field.show_sea_field()
            input('жми Enter для продолжения...')
        else:
            input('жми Enter для продолжения...')
    else:
        print('%s теряет корабль c координатами %s%s' % (who_is_waiting.name, x, y))
        who_is_waiting.my_field.show_sea_field()
    print()
    round_with_kills.append(round)  # чисто для отладки, можно смело удалять
    return True


def shoot_wounded(who_is_shooting, who_is_waiting, x, y, game_mode, shoot_direction=[]):
    if shoot_direction == 'влево':
        y = y - 1
    elif shoot_direction == 'вправо':
        y = y + 1
    elif shoot_direction == 'вверх':
        x = x - 1
    elif shoot_direction == 'вниз':
        x = x + 1
    else:
        x = x
        y = y
    if shoot_direction:
        who_is_shooting.used_coordinates.append(str(x) + str(y))
    who_is_shooting.shoot_direction = []
    who_is_waiting.wounded_ship_coordinates.append(str(x) + str(y))
    who_is_shooting.opponent_field.sea_field[x][y] = battle_field.BattleField.cell_type_wounded_or_killed
    who_is_waiting.my_field.sea_field[x][y] = battle_field.BattleField.cell_type_wounded_or_killed
    x, y = convert_xy_to_abc123(x, y)
    print('%s стреляет с координатами %s%s и ранит корабль на поле соперника' % (who_is_shooting.name, x, y))
    who_is_shooting.opponent_field.show_sea_field()
    print()
    if game_mode == 1:
        if who_is_waiting == prepare_game.gamer:
            input('жми Enter для продолжения...')
            print('%s, вот твои корабли:' % who_is_waiting.name)
            who_is_waiting.my_field.show_sea_field()
            input('жми Enter для продолжения...')
        else:
            input('жми Enter для продолжения...')
    else:
        print('%s имеет раненый корабль c координатами %s%s' % (who_is_waiting.name, x, y))
        who_is_waiting.my_field.show_sea_field()
    print()
    return True


def shoot_try_to_destroy(who_is_shooting, who_is_waiting, x, y, game_mode):
    while not who_is_shooting.shoot_direction:
        x = int(who_is_waiting.wounded_ship_coordinates[-1][0])  # -1 чтобы в этой попытке добить корабль бот начал
        y = int(who_is_waiting.wounded_ship_coordinates[-1][1])  # стрелять с последней раненой координатой
        if (who_is_shooting.opponent_field.can_shoot_to_left(x, y)
                and 'влево' not in who_is_shooting.dont_shoot_to_this_direction):
            who_is_shooting.shoot_direction.append('влево')
        if (who_is_shooting.opponent_field.can_shoot_to_right(x, y)
                and 'вправо' not in who_is_shooting.dont_shoot_to_this_direction):
            who_is_shooting.shoot_direction.append('вправо')
        if (who_is_shooting.opponent_field.can_shoot_to_top(x, y)
                and 'вверх' not in who_is_shooting.dont_shoot_to_this_direction):
            who_is_shooting.shoot_direction.append('вверх')
        if (who_is_shooting.opponent_field.can_shoot_to_bottom(x, y)
                and 'вниз' not in who_is_shooting.dont_shoot_to_this_direction):
            who_is_shooting.shoot_direction.append('вниз')
        if not who_is_shooting.shoot_direction:
            del who_is_waiting.wounded_ship_coordinates[-1]
            continue
    who_is_shooting.shoot_direction = random.choice(who_is_shooting.shoot_direction)
    if who_is_shooting.shoot_direction == 'влево':
        if who_is_waiting.my_field.cell_with_ship(x, y - 1):
            who_is_shooting.dont_shoot_to_this_direction.append('вверх')
            who_is_shooting.dont_shoot_to_this_direction.append('вниз')
            for s in who_is_waiting.my_ships:
                if s.ship_status != ship.Ship.ship_all_statuses[1]:
                    continue
                else:
                    ship_index = who_is_waiting.my_ships.index(s)
                    s.ship_was_wounded()
                    if s.ship_killed():
                        if shoot_killed(who_is_shooting, who_is_waiting, x, y, ship_index, game_mode, who_is_shooting.shoot_direction):
                            return True
                    else:
                        if shoot_wounded(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction):
                            return True
        elif (who_is_waiting.my_field.cell_empty(x, y - 1)
              and not who_is_shooting.opponent_field.cell_near_ship(x, y - 1)):
            shoot_nothing(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction)

    if who_is_shooting.shoot_direction == 'вправо':
        if who_is_waiting.my_field.cell_with_ship(x, y + 1):
            who_is_shooting.dont_shoot_to_this_direction.append('вверх')
            who_is_shooting.dont_shoot_to_this_direction.append('вниз')
            for s in who_is_waiting.my_ships:
                if s.ship_status != ship.Ship.ship_all_statuses[1]:
                    continue
                else:
                    ship_index = who_is_waiting.my_ships.index(s)
                    s.ship_was_wounded()
                    if s.ship_killed():
                        if shoot_killed(who_is_shooting, who_is_waiting, x, y, ship_index, game_mode, who_is_shooting.shoot_direction):
                            return True
                    else:
                        if shoot_wounded(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction):
                            return True
        elif (who_is_waiting.my_field.cell_empty(x, y + 1)
              and not who_is_shooting.opponent_field.cell_near_ship(x, y + 1)):
            shoot_nothing(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction)

    if who_is_shooting.shoot_direction == 'вверх':
        if who_is_waiting.my_field.cell_with_ship(x - 1, y):
            who_is_shooting.dont_shoot_to_this_direction.append('влево')
            who_is_shooting.dont_shoot_to_this_direction.append('вправо')
            for s in who_is_waiting.my_ships:
                if s.ship_status != ship.Ship.ship_all_statuses[1]:
                    continue
                else:
                    ship_index = who_is_waiting.my_ships.index(s)
                    s.ship_was_wounded()
                    if s.ship_killed():
                        if shoot_killed(who_is_shooting, who_is_waiting, x, y, ship_index, game_mode, who_is_shooting.shoot_direction):
                            return True
                    else:
                        if shoot_wounded(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction):
                            return True
        elif (who_is_waiting.my_field.cell_empty(x - 1, y)
              and not who_is_shooting.opponent_field.cell_near_ship(x - 1, y)):
            shoot_nothing(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction)

    if who_is_shooting.shoot_direction == 'вниз':
        if who_is_waiting.my_field.cell_with_ship(x + 1, y):
            who_is_shooting.dont_shoot_to_this_direction.append('влево')
            who_is_shooting.dont_shoot_to_this_direction.append('вправо')
            for s in who_is_waiting.my_ships:
                if s.ship_status != ship.Ship.ship_all_statuses[1]:
                    continue
                else:
                    ship_index = who_is_waiting.my_ships.index(s)
                    s.ship_was_wounded()
                    if s.ship_killed():
                        if shoot_killed(who_is_shooting, who_is_waiting, x, y, ship_index, game_mode, who_is_shooting.shoot_direction):
                            return True
                    else:
                        if shoot_wounded(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction):
                            return True
        elif (who_is_waiting.my_field.cell_empty(x + 1, y)
              and not who_is_shooting.opponent_field.cell_near_ship(x + 1, y)):
            shoot_nothing(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction)

def shoot(who_is_shooting, who_is_waiting, x, y, game_mode):
    if game_mode == 2 or who_is_shooting == prepare_game.bot:
        while (str(x) + str(y) in who_is_shooting.used_coordinates
               or who_is_shooting.opponent_field.cell_near_ship(x, y)):
            who_is_shooting.used_coordinates.append(str(x) + str(y))
            x = random.randint(0, 9)
            y = random.randint(0, 9)
    who_is_shooting.used_coordinates.append(str(x) + str(y))
    if who_is_waiting.my_field.cell_with_ship(x, y):
        for s in who_is_waiting.my_ships:
            for c in s.ship_coordinates:
                if str(x) + str(y) in c:
                    ship_index = who_is_waiting.my_ships.index(s)
                    s.ship_was_wounded()
                    if s.ship_killed():
                        if shoot_killed(who_is_shooting, who_is_waiting, x, y, ship_index, game_mode, who_is_shooting.shoot_direction):
                            return True
                    else:
                        if shoot_wounded(who_is_shooting, who_is_waiting, x, y, game_mode, who_is_shooting.shoot_direction):
                            return True
    elif who_is_waiting.my_field.cell_empty(x, y) and not who_is_shooting.opponent_field.cell_near_ship(x, y):
        shoot_nothing(who_is_shooting, who_is_waiting, x, y, game_mode)


while who_is_waiting.my_ships and who_is_shooting.my_ships:
    print('\033[3;30;42mРаунд номер:', round, '\033[0m')
    if prepare_game.game_mode == 2:
        if who_is_shooting == prepare_game.bot or who_is_shooting == prepare_game.bot2:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            print('%s, вот сколько кораблей осталось у соперника %s:' % (who_is_shooting.name, who_is_waiting.name))
            if who_is_waiting.live_ones:
                print(' ' * 10, 'количество однопалубных.....%s' % len(who_is_waiting.live_ones))
            if who_is_waiting.live_twos:
                print(' ' * 10, 'количество двухпалубных.....%s' % len(who_is_waiting.live_twos))
            if who_is_waiting.live_threes:
                print(' ' * 10, 'количество трёхпалубных.....%s' % len(who_is_waiting.live_threes))
            if who_is_waiting.live_fours:
                print(' ' * 10, 'количество четырёхпалубных..%s' % len(who_is_waiting.live_fours))
            print()
    else:
        if prepare_game.game_mode == 1 and who_is_shooting == prepare_game.bot:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        else:
            user_x = ''
            user_y = ''
            gamer_cant_shoot_with_coordinates = True
            while gamer_cant_shoot_with_coordinates:
                who_is_shooting.opponent_field.show_sea_field()
                print('%s, вот сколько кораблей осталось у соперника %s:' % (who_is_shooting.name, who_is_waiting.name))
                if who_is_waiting.live_ones:
                    print(' ' * 10, 'количество однопалубных.....%s' % len(who_is_waiting.live_ones))
                if who_is_waiting.live_twos:
                    print(' ' * 10, 'количество двухпалубных.....%s' % len(who_is_waiting.live_twos))
                if who_is_waiting.live_threes:
                    print(' ' * 10, 'количество трёхпалубных.....%s' % len(who_is_waiting.live_threes))
                if who_is_waiting.live_fours:
                    print(' ' * 10, 'количество четырёхпалубных..%s' % len(who_is_waiting.live_fours))
                print()
                print('%s, укажи первую координату для стрельбы (А, Б, В, Г, Д, Е, Ж, З, И, К):' % prepare_game.gamer.name)
                while user_x not in ('а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К'):
                    user_x = input()
                    if user_x == 'а' or user_x == 'А': x = 0
                    elif user_x == 'б' or user_x == 'Б': x = 1
                    elif user_x == 'в' or user_x == 'В': x = 2
                    elif user_x == 'г' or user_x == 'Г': x = 3
                    elif user_x == 'д' or user_x == 'Д': x = 4
                    elif user_x == 'е' or user_x == 'Е': x = 5
                    elif user_x == 'ж' or user_x == 'Ж': x = 6
                    elif user_x == 'з' or user_x == 'З': x = 7
                    elif user_x == 'и' or user_x == 'И': x = 8
                    elif user_x == 'к' or user_x == 'К': x = 9
                    else:
                        print('Неверное значение первой координаты')

                user_y = ''
                print('%s, укажи вторую координату для стрельбы (от 1 до 10):' % prepare_game.gamer.name)
                while user_y not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
                    user_y = input()
                    if user_y == '1': y = 0
                    elif user_y == '2': y = 1
                    elif user_y == '3': y = 2
                    elif user_y == '4': y = 3
                    elif user_y == '5': y = 4
                    elif user_y == '6': y = 5
                    elif user_y == '7': y = 6
                    elif user_y == '8': y = 7
                    elif user_y == '9': y = 8
                    elif user_y == '10': y = 9
                    else:
                        print('Неверное значение второй координаты')

                if (who_is_shooting.opponent_field.cell_with_wounded_or_killed_ship(x, y) or
                    who_is_shooting.opponent_field.cell_no_ship_after_shoot(x, y) or
                    who_is_shooting.opponent_field.cell_near_ship(x, y)):
                    gamer_cant_shoot_with_coordinates = True
                    input('%s, в эту клетку уже не имеет смысла стрелять, давай выберем новые координаты (жми Enter для продолжения...)' % who_is_shooting.name)
                    user_x = ''
                    user_y = ''
                else:
                    gamer_cant_shoot_with_coordinates = False

    if who_is_waiting.wounded_ship_coordinates and (prepare_game.game_mode == 2 or who_is_shooting == prepare_game.bot):
        if shoot_try_to_destroy(who_is_shooting, who_is_waiting, x, y, prepare_game.game_mode):
            round += 1
            continue
        else:
            round += 1
            who_is_shooting, who_is_waiting = whose_turn(who_is_shooting)
    else:
        if shoot(who_is_shooting, who_is_waiting, x, y, prepare_game.game_mode):
            round += 1
            continue
        else:
            round += 1
            who_is_shooting, who_is_waiting = whose_turn(who_is_shooting)
else:
    round -= 1
    if who_is_shooting.my_ships:
        print('\033[3;30;42m***Игра окончена, победителем является', who_is_shooting.name, '***\033[0m')
        print('****************************************************************************************************')
    else:
        print('\033[3;30;42m***Игра окончена, победителем является', who_is_waiting.name, '***\033[0m')
        print('****************************************************************************************************')
print('\033[3;30;42mВсего раундов:', round, '\033[0m')  # чисто для отладки, можно смело удалять
print('\033[3;30;42mКорабли были уничтожены в таких раундах:', round_with_kills, '\033[0m')  # чисто для отладки
