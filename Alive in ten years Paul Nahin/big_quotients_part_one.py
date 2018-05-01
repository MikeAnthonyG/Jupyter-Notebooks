import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat


#test_answer()  --> change variables as you like
# Distribution is interesting 

def big_quotient_1(k = 1):
    rand_uni_1 = random.random()
    rand_uni_2 = random.random()
    div = max(rand_uni_1,rand_uni_2) / min(rand_uni_1, rand_uni_2)
    return [div, div >= k]

def test_answer(trials=10000, k=1):
    data_num = []
    greater_than_k = []
    for i in range(trials):
        return_value = (big_quotient_1(k))
        data_num.append(return_value[0])
        greater_than_k.append(return_value[1])
    x = greater_than_k.count(True) / trials
    print('Greater than k chance: {}'.format(str(x)))
    bins = np.linspace(0, 75, 75)
    plt.hist(data_num, bins)
    #Uncomment to use examine_distribution()
    #return data_num
       
    
def examine_distribution():
    _data = test_answer()
    #Normal Distribution
    m,s = stat.norm.fit(_data)
    print('Normal: Mean: {} Var: {}'.format(m,s))
    #Weibull
    wc, wl, ws = stat.weibull_min.fit(_data)
    print('Webull: c: {}, loc: {} scale: {}'.format(wc,wl,ws))
    #lognormal
    s, loc, scale = stat.lognorm.fit(_data)
    print('lognormal: {} {} {}'.format(s,loc,scale))
    #pareto
    b, ploc, pscale = stat.pareto.fit(_data)
    print('pareto {} {} {}'.format(b, ploc, pscale))
    
    
    
    
        
    