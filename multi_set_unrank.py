from multi_set import find_sub_set,pred
from multi_set_rank import rank
def unrank_naive(index,n,k):
    res = [0 for i in range(k)]
    idx = 0
    while True:
        r = rank(res,n,k)
        if(r>index):
            res[idx] -= 1
            idx = idx+1
        elif r<index:
            for j in range(idx,k):
                res[j] += 1
        else:
            return res
def unrank(index,n,k):
    res = [0 for i in range(k)]
    idx = 0
    num = 0
    for idx in range(k):
        for i in range(n-num):
            enum = pred(n-i-num,k-idx-1)
            if(index-enum<0):
                res[idx] = i+num                
                break
            if(index-enum==0):
                for j in range(idx,k):
                    res[j] = i+num+1
                return res
            if(index-enum>0):
                index -= enum
                res[idx] = i+num+1
        num = res[idx]
    return res

if __name__=="__main__":
    n = 10
    k = 10
    subsets = find_sub_set(n,k,0)
    import time
    def a(s):
        b = []
        for item in s:
            b.append(int(item))
        return b
    start = time.time()
    for r,item in enumerate(subsets):
        u = unrank(
            r,n,k
        )    
        print(r,"UNRANK",u,"ACTUAL",a(item),"CORRECT",u==a(item))
    end = time.time()
    print("better",end-start)

    start = time.time()
    for r,item in enumerate(subsets):
        u = unrank_naive(
            r,n,k
        )    
        #print(r,"UNRANK",u,"ACTUAL",a(item),"CORRECT",u==a(item))
    end = time.time()
    print("naive",end-start)
