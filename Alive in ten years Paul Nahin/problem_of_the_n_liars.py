import random
import matplotlib.pyplot as plt

# =============================================================================
# Example usage: check_answer()
#  or to really see the limit is 0.5  check_answer(10000, 2, 200, 0.99)
# =============================================================================
#p=1 if never lies, p=0 if always lies
def liars(prob_truth=0.99, participants=41):
    truth_value = True
    for i in range(participants):
        if random.random() > prob_truth:
            truth_value = not truth_value
    return truth_value

def check_answer(trials=10000, lower_limit=41, upper_limit_participants = 100, truth_prob=0.99):
    results = []
    for i in range(lower_limit, upper_limit_participants+1):
        result_trial = []
        for j in range(trials):
            result_trial.append(liars(truth_prob, i))
        results.append(result_trial.count(True)/trials)
    
    plt.plot(list(range(lower_limit, upper_limit_participants+1)), results)
    plt.show()