def inv(num,s):
    for idx,item in enumerate(s):
        if(item==num):
            return idx
    return -1

def rank(s):
    r = 0
    for i in range(1,len(s)+1):
        moves = 0
        for j in range(inv(i,s)):
            if(s[j]<i):
                moves +=1
        if r %2 ==1:
            remainder = moves
        else:
            remainder = i - 1 - moves
        print("{} * {} + {} = {}".format(i,r,remainder,i*r + remainder))
        r = i*r + remainder
    return r

a = rank(
    [5,1,7,3,2,6,4]
)
print(a)