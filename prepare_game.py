import player
import sys  # для выхода из программы пока я не доделал ручную расстановку кораблей.

print('Привет, давай поиграем в морской бой. Если хочешь поиграть сам, \033[3;30;42mвведи 1\033[0m.'
      ' Если хочешь посмотреть на ботов, \033[3;30;42mвведи 2\033[0m.')
print('Выбери режим (и нажми Enter):')

game_mode = 0
while game_mode not in (1, 2):
    wish = input()
    if wish == '1':
        game_mode = 1
    elif wish == '2':
        game_mode = 2
    else:
        print('Неверное значение, введи 1 или 2')

if game_mode == 1:
    gamer = player.Player()
    bot = player.Player()
    bot.name_generator()
    print('Хорошо, давай поиграем в морской бой. Но сначала познакомимся, как тебя зовут?')
    gamer.name_creation()

    if bot.name == gamer.name:
        bot.name = bot.name + ' (клон)'

    print('Приятно познакомиться, %s, твоим соперником будет %s.' % (gamer.name, bot.name))
    gamer.player_ships()
    bot.player_ships()
    print()
    print('%s, как тебе хочется расставить корабли: \033[3;30;42mвручную (1)\033[0m или \033[3;30;42mавтоматически (2)\033[0m?' % gamer.name)
    print('Выбери расстановку кораблей (и нажми Enter):')

    ship_mode = 0
    while ship_mode not in (1, 2):
        wish = input()
        if wish == '1':
            ship_mode = 1
        elif wish == '2':
            ship_mode = 2
        else:
            print('Неверное значение, введи 1 или 2')

    if ship_mode == 1:
        print('Пока не сделано...')
        sys.exit()
        '''
        ДОДЕЛАТЬ ручную расстановку кораблей.
        print('Вот твои корабли:')
        gamer.player_available_ships()
        print()
        print('Давай расставим корабли. Сначала укажи тип корабля (1, 2, 3 или 4), а затем координаты начала и конца'
              ' корабля. Например, для однопалубного надо указать 1 и потом г5г5. А для трёхпалубного надо указать 3'
              ' и потом г5г7')
        while gamer.player_available_ship_count:
            gamer.player_save_ship()
            gamer.player_updated_ships()
        print('%s, Вы расставили все корабли, отлично!' % gamer.name)
        '''
    else:
        print('%s, вот твоё поле:' % gamer.name)
        gamer.player_random_ship_location()
        gamer.show_player_random_ships_on_field()

    input('жми Enter для продолжения...')
    print()
    bot.player_random_ship_location()
    gamer.player_has_opponent_field()
    bot.player_has_opponent_field()

else:
    print('Хорошо, давай посмотрим как боты играют между собой в морской бой.')
    bot = player.Player()
    bot.name_generator()
    bot2 = player.Player()
    bot2.name_generator()
    if bot2.name == bot.name:
        bot2.name = bot2.name + ' (клон)'
    print()
    print('Сегодня играют %s и %s.' % (bot.name, bot2.name))
    # input('жми Enter для продолжения...')
    bot.player_ships()
    bot2.player_ships()
    print()
    print('Вот поле бота:', bot.name)
    bot.player_random_ship_location()
    bot.show_player_random_ships_on_field()
    # input('жми Enter для продолжения...')
    print()
    print('Вот поле бота:', bot2.name)
    bot2.player_random_ship_location()
    bot2.show_player_random_ships_on_field()
    # input('жми Enter для продолжения...')
    print()
    bot.player_has_opponent_field()
    bot2.player_has_opponent_field()
