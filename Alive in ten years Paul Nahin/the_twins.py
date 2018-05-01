import random

###Example Usage
# check_answer(trials = 10000)    
#RESULTS = 0.156 and 0.1571


def the_twins():
    #Check if twins is a subset of one of the group subsets
    twins = set(random.sample(range(1,21), 2))
    groups = [set(range(1,5)), set(range(5,9)), set(range(9, 13)),
              set(range(13,17)), set(range(17,21))]
    for _set in groups:
        if twins < _set:
            return True
    return False

def check_answer(trials):
    results = []
    for x in range(trials):
        results.append(the_twins())
    return results.count(True) / trials
    
        