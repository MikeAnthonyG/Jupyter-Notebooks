import random
import math

def adj(trials=10000):
    total = 0
    for i in range(trials):
        r = math.sqrt(random.random()**2 + random.random()**2)
        total += r
    print(total/trials)
    
def sts(trials = 10000):
    total=0
    for i in range(trials):
        r = math.sqrt((1+(random.random()-random.random())**2))
        total += r
    print(total/trials)
    
def _any(trials=10000):
    total = 0
    for i in range(trials):
        r = math.sqrt((random.random()-random.random())**2+(random.random()-random.random())**2)
        total += r
    print(total/trials)