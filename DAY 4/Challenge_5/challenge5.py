import itertools as it

def infinite_data(iter):
    return it.cycle(iter) 
  
# Dictionary
result = infinite_data({1: 'Skae', 2: 'Hub', 3: 'Developer'})

for k in result:
    print(k)