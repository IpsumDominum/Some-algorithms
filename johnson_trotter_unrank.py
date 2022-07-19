import math

def unrank(num,n):
    s = [0 for _ in range(n)]
    for idx,j in enumerate(reversed(range(1,n+1))):
        r = num % j
        num_original = num
        num = math.floor(num/j)
        if(num %2 ==0):
            k = n+1
            d = -1
        else:
            k = 0
            d = 1
        c = 0
        while True:
            if(c==r+1):
                break
            else:
                k = k + d
                if(s[k-1]==0):
                    c +=1
        print(f"{idx+1}. {num_original} $\%$ {j}={r};$\\lfloor${num_original}/{j}$\\rfloor$={num} $\implies$"+"$\pi^{-1}"+f"({j})$={k}\\\\")
        s[k-1] = j
    return s

a = unrank(4424244,14)
print(a)
