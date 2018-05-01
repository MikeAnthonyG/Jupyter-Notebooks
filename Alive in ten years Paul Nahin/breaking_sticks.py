import random 
import scipy.stats as stats

#Example usage  
# check_answer(3, 10000)  #Break into 3 equal parts  and use 10,000 trials
####RETURNS: 0.3322   which is close to the theoretical 1/n or 1/3

def breaking_sticks(n):
    mark_1 = random.random()
    mark_2 = random.random()
    stick_len = 1 / n
    start_pt = 0
    end_pt = start_pt + stick_len
    while(start_pt <= 1):
        if(mark_1 > start_pt and mark_2 > start_pt and mark_1 < end_pt and mark_2 < end_pt):
            return True
        start_pt += stick_len
        end_pt += stick_len
    return False

def check_answer(num_breaks, trials):
    list_check = []
    for x in range(0, trials):
        list_check.append(breaking_sticks(num_breaks))
    return list_check.count(True)/len(list_check)