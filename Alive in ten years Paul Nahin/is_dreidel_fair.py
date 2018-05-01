import random

def dreidal_game(players=5):
    pot = players
    game_winnings = []
    for x in range(players):
        game_winnings.append(0)
    rolls = ['n', 'g', 'h', 's']
    curr_roll = 'n'
    curr_player = 0
    while curr_roll !='g':
        curr_roll = random.sample(rolls, k=1)[0]
        if curr_roll == 'h':
            game_winnings[curr_player] += pot * 0.5
            pot *= 0.5
            curr_player = (curr_player + 1) % players
        elif curr_roll == 's':
            game_winnings[curr_player] -= 1
            pot += 1
            curr_player = (curr_player+1) % players
        elif curr_roll == 'n':
            curr_player = (curr_player+1) % players
        else:
            curr_roll = 'g'
            game_winnings[curr_player] += pot
    return curr_player, game_winnings

def check_answer(trials=10000, players=5):
    game_champions = []
    earnings = []
    for x in range(players):
        earnings.append([])
    for i in range(trials):
        winner, earning = dreidal_game(players)
        game_champions.append(winner)
        for player in range(players):
            earnings[player].append(earning[player])
            
    for play in range(players):
        prob_won = game_champions.count(play)/trials
        average_winnings = sum([x for x in earnings[play]]) / trials
        print('Player: {} Prob to win: {} Avg Winnings: {}'.format(play, prob_won, average_winnings))
        
        
    
    