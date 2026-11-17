# Task 1: Fractional knapsack - greedy value/weight

def fractional_knapsack(items, capacity):
    if capacity < 0 or any(w <= 0 for _,w,_ in items):
        raise ValueError("Capacity must be nonnegative and weights positive")
    ordered = sorted(items, key=lambda x:x[2]/x[1], reverse=True)
    selected=[]; total=0.0
    for name, weight, value in ordered:
        if capacity == 0: break
        fraction=min(1.0,capacity/weight)
        selected.append((name,round(fraction,3)))
        total+=fraction*value; capacity-=fraction*weight
    return selected,total
if __name__=='__main__':
    print('Task 1 fractional knapsack')
    print(fractional_knapsack([('P',10,60),('Q',20,100),('R',30,120)],50))
