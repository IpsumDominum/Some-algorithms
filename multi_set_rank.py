from multi_set import find_sub_set,pred
def rank(s,n,k):
    r = 0
    num = 0
    for idx in range(len(s)):
        item = s[idx]
        for i in range(item-num):
            r += pred(n-i-num,k-idx-1)
        num = item
    return r

if __name__=="__main__":
    p = pred(2,2)
    print(p)
    #exit()
    n = 4
    k = 4
    subsets = find_sub_set(n,k,0)
    print(subsets)

    def a(s):
        b = []
        for item in s:
            b.append(int(item))
        return b

    for actual_r,item in enumerate(subsets):
        r = rank(
            a(item),n,k
        )
        print(a(item),"RANK",r,"ACTUAL",actual_r)
