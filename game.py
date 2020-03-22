from random import randint

game_running = True
game_result = []

def calculate_monster_attack():
    return randint(monster['attack_min'], monster["attack_max"])

def game_ends(winner_name):
    print(f'Player {winner_name} won the game')


while game_running == True:
    counter = 0
    new_round = True
    player = {'name':'pleayer_name','attack':10,'heal':16,'health': 100}
    monster = {'name':'Beast','attack_min':12, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player name')
    player['name'] = input()
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health.')

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')
        print('4) Show result')
        player_choice = input('Select action is:')

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_monster_attack()
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True
            print('Attack')
        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True
        elif player_choice == '3':
            game_running = False
            new_round = False
        elif player_choice =='4':
            for player_stats in game_result:
                print(player_choice)

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left ')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left ')
        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'],'health':player['health'],'rounds': counter}
            game_result.append(round_result)
            new_round = False
        elif monster_won:
            print('The monster won')
            game_ends(monster['name'])
            round_result = {'name': player['name'],'health':player['health'],'rounds': counter}
            game_result.append(round_result)

            new_round = False

