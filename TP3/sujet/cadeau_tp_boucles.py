
def est_premier(n):
    """test de primalité"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    for d in range(2, int(n**(1/2))+1):
        if n%d == 0:
            return False
    return True