import random

#Example check_answer(100000)
# My b_then_a returns around 0.17967 which differs from the theoretical result of 0.14985
# I tried two implementations which both returned the same result, the other answers align.


def roll_two_sixes_in_a_row():
    count = 0
    attempts = 0
    last_throw = 0
    while count < 3:
        attempts += 1
        current_throw = random.randint(1,6)
        if current_throw == 6 and last_throw == 6:
            return attempts
        last_throw = current_throw        
    return attempts

#Returns true if 4 heads come before 4 tails
def heads_tails_4h_7t(prob):
    HT_list = []
    while HT_list.count('H') <= 4 and HT_list.count('T') <= 7:
        HT_list.append(random.choices('HT', cum_weights=(prob, 1.0))[0])
        if HT_list.count('H') == 4:
            return True
        if HT_list.count('T') == 7:
            return False
        
def a_b_c_toss_order():
    out_order = []
    remaining_players = ['a','b','c']
    flag = True
    while flag:
        for player in remaining_players:
            if random.randint(1,6) == 6:
                out_order.append(player)
                remaining_players.remove(player)
                new_flag = True
                while new_flag:
                    for _player in remaining_players:
                        if random.randint(1,6) == 6:
                            out_order.append(_player)
                            return out_order
                    

    
def check_answer(trials):
    mean_six = sum(roll_two_sixes_in_a_row() for i in range(trials)) / trials
    print('Average attempts to roll two sixes in a row: {}'.format(str(mean_six)))
    
    ht_even = [heads_tails_4h_7t(0.5) for i in range(trials)].count(True) / trials
    print('4 Heads beats 7 Tails (EVEN): {}'.format(str(ht_even)))

    ht_weighted = [heads_tails_4h_7t(0.45) for i in range(trials)].count(True) / trials
    print('4 Heads beats 7 Tails (WEIGHTED): {}'.format(str(ht_weighted)))
    
    abc_order = []
    for i in range(trials):
        abc_order.append(a_b_c_toss_order())
    a_then_b = abc_order.count(['a','b']) / trials
    b_then_a = abc_order.count(['b', 'a']) / trials
    print('A loses then B: {}'.format(str(a_then_b)))
    print('B loses then A: {}'.format(str(b_then_a)))