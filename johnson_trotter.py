import numpy as np
def move_largest(s,m,s_inv,n):    
    if(n==0):
        return s,m,s_inv
    max_inv = s_inv[n]
    next_swap = max_inv+m[max_inv]
    if(s[next_swap]>n):
        m[max_inv] = -m[max_inv]
        return move_largest(s,m,s_inv,n-1)
    else:
        temp = s[next_swap]
        temp_m = m[next_swap]
        s[next_swap] = n
        s[max_inv] = temp
        m[next_swap] = m[max_inv]
        m[max_inv] = temp_m
        s_inv[temp] = max_inv
        s_inv[n] = next_swap
        return s,m,s_inv
def factorial(n):
    res = 1
    for i in range(n-1):
        res *= n-i
    return res
def johnson_trotter(n):
    s = [n+1] + [i for i in range(n)] + [n+1]#Contents
    s_inv = [i+1 for i in range(n)] #Contents
    m = [-1 for _ in range(len(s))] #Directions
    for i in range(factorial(n)):
        if(i % n==0):
            print("="*10)
        print(np.array(s[1:-1])+1, " = ",i)
        s,m,s_inv = move_largest(s,m,s_inv,n-1)

johnson_trotter(5)

