import random

def exact_cover(n, m, C=None):
    if C == None:    
        C = []
    for i in range(m):
        size_set = random.randrange(n)
        add_set = set(random.sample(range(0, n), size_set))
        if add_set not in C:
            C.append(add_set)
    if len(C) != m:
        return exact_cover(n, m, C)
    return C


def exact_cover_same_probability(n, m, C = None):
    if 2^n < m:
        return "no se puede"
    
    if C == None:    
        C = []
    X = [i for i in range(n)]
    for i in range(m):
        select = tuple(random.randrange(2) for i in range(m))
        add_set = set()
        
        for j in range(n):
            if select[j] == 1:
                add_set.add(j)

        if add_set not in C:
            C.append(add_set)
    if len(C) != m:
        return exact_cover(n, m, C)
    return C




def zero_or_one(l):
    select = tuple(random.randrange(2) for i in range(l))
    return select

def exact_cover_same_probability(n, m, C = None):
    if 2^n < m:
        return "no se puede"
    
    if C == None:    
        C = []
    X = [i for i in range(n)]
    for i in range(m):
        zero_or_one(m)
        add_set = set()
        
        for j in range(n):
            if select[j] == 1:
                add_set.add(j)

        if add_set not in C:
            C.append(add_set)
    if len(C) != m:
        return exact_cover(n, m, C)
    return C