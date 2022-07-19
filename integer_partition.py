# A utility function to print an
# array p[] of size 'n'
def printArray(p, n,idx):
    out = ""
    for i in range(0, n):
        out += str(p[i]) + " "
    #if(out.strip(" ")=="2 1 1 1 1 1 1 1 1 1 1"):
    #if(idx==101):
    #if(out.strip(" ")=="5 4 2"):
    print(out.strip(" ")," | ",idx)
def printAllUniqueParts(n):
    p = [0] * n	 # An array to store a partition
    k = 0		 # Index of last element in a partition
    p[k] = n	 # Initialize first partition
    idx = 0
    while True:
        printArray(p, k + 1,idx)
        rem_val = 0
        while k >= 0 and p[k] == 1:
            rem_val += p[k]
            k -= 1
        if k < 0:
            print()
            return
        p[k] -= 1
        rem_val += 1
        while rem_val > p[k]:
            p[k + 1] = p[k]
            rem_val = rem_val - p[k]
            k += 1
        p[k + 1] = rem_val
        k += 1
        idx +=1

def p(n,k):
    if(k<=1 or n<1): return 0
    elif k==2: return 1
    elif k>n: return p(n,n) + 1
    else: return p(n,k-1) + p(n-(k-1),k)
def lambdas(vals,m,n):
    t = p(n,n)
    print("TOTAL",t)
    l = 0
    outs = []
    for i,k in enumerate(vals):
        for z in range(m[i]):
            print("+ p({},{})".format(n,k),end=" ")
            a = p(n,k)
            l += a
            outs.append(a)
            n -= k
    for item in outs:
        print("+"+str(item),end="")
    print()
    return t - l

#print(lambdas([10,10],[1,1],20))
#print(lambdas([5,4,2],[1,1,1],11))
#print(lambdas([2,1],[1,10],12))
#print(lambdas([7,3,1],[1,1,2],12))

#print(p(11,11))
printAllUniqueParts(20)
# This code is contributed
# by JoshuaWorthington


