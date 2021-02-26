def nthfib(n):

    if n < 0:
        return None

    elif n == 0:
        return 0

    elif n == 1:
        return 1
    
    else:
        return nthfib(n - 1) + nthfib(n - 2)


def nthfact(n):
    
    if n < 0:
        return 0
    
    elif n == 0 or n == 1:
        return 1
    
    else:
        return n * nthfact(n-1)
