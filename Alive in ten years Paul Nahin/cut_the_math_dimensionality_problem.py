import random
import matplotlib.pyplot as plt

# =============================================================================
# What is the probability that a dart, hitting a square board at random, 
# lands nearer the center than an edge. (Then I added more dimensions)
# =============================================================================

def closer_or_farther(dims=2):
    if dims < 2: 
        print('Must have more than 2 dimensions')
        return
    for i in range(dims):
        if random.random() > 0.5:
            return False
    return True

def run(dimension_range=10, trials=10000):
    prob_closer = []
    for i in range(2, dimension_range+1):
        _test = []
        for x in range(trials):
            _test.append(closer_or_farther(dims=i))
        prob_closer.append(_test.count(True)/trials)
    
    for j in range(2, dimension_range+1):
        index = j - 2
        print('Dimensions: {}   Probability: {}'.format(str(j), str(prob_closer[index])))
        
    plt.plot(list(range(2,dimension_range+1)), prob_closer)
    plt.show()