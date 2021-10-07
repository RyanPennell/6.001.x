import factorial
from factorial import fact

def combo(n,r):
    return fact(n)/(fact(n-r)*fact(r))
