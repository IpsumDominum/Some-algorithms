def find_sub_set(n,k,offset):
    result = []
    if(k==1):
        return [str(i) for i in range(offset,n)]
    else:
        for i in range(offset,n):
            recur = find_sub_set(n,k-1,i)
            for j in range(len(recur)):
                r = recur[j]
                result.append(str(i)+r)
        return result
        
import math
def pred(n,k_i):
    res = 1
    for i in range(k_i):
        res *= (n+k_i-1-i)/(k_i-i)
    return res

if __name__=="__main__":
    n = 3
    k_i = 3
    subsets = find_sub_set(n,k_i,0)
    print(subsets)
    exit()
    for n in range(1,10):
        for k_i in range(1,10):
            subsets = find_sub_set(n,k_i,0)        
            print(len(subsets), pred(n,k_i),int(len(subsets)-pred(n,k_i)))
        print("="*10)

