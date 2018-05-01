import random
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Example usage:   test_answer
# To see the graph become more linear as we increase k:
#     increase_dimensions(k=2)
#     increase_dimensions(k=10)
#     increase_dimensions(k=100)
# =============================================================================

def big_quotient(num_dimensions = 3, k=1):
    rand_nums = []
    for i in range(num_dimensions):
        rand_nums.append(random.random())
    div = max(rand_nums) / min(rand_nums)
    return [div, div >= k]

def test_answer(trials=10000, num_dim=3, k=1):
    data_num = []
    greater_than_k = []
    for i in range(trials):
        return_value = (big_quotient(num_dim, k))
        data_num.append(return_value[0])
        greater_than_k.append(return_value[1])
    x = greater_than_k.count(True) / trials
    print('Greater than k chance: {}'.format(str(x)))
    bins = np.linspace(0, 75, 75)
    plt.hist(data_num, bins)
    
def increase_dimensions(trials=10000, ini_dims=2, final_dim=10,k=1):
    greater_than_k_percentage = []
    for i in range(ini_dims, final_dim+1):
        data_num = []
        greater_than_k = []
        for j in range(trials):
            return_value = (big_quotient(i, k))
            data_num.append(return_value[0])
            greater_than_k.append(return_value[1])
        greater_than_k_percentage.append(greater_than_k.count(True) / trials)
    plt.plot(list(range(ini_dims, final_dim+1)), greater_than_k_percentage)