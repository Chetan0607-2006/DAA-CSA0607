# Task 2: Job sequencing with deadlines and unit-duration jobs

def schedule(jobs):
    if any(d<1 for _,d,_ in jobs): raise ValueError('Deadlines must be positive')
    slots=[None]*min(len(jobs),max((d for _,d,_ in jobs),default=0))
    profit=0
    for name,deadline,value in sorted(jobs,key=lambda x:x[2],reverse=True):
        if value<=0: continue
        for slot in range(min(deadline,len(slots))-1,-1,-1):
            if slots[slot] is None:
                slots[slot]=name;profit+=value
                print('Placed',name,'in slot',slot+1)
                break
    return slots,profit
if __name__=='__main__':
    print('Task 2 job sequencing')
    print('Result:',schedule([('A',2,80),('B',1,35),('C',2,60),('D',3,40),('E',1,25)]))
