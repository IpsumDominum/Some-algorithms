import math
def rank(s,m):
    r = 0
    for i in range(len(s)):
        if(r % 2 ==1):
            c = m[i] - s[i] - 1
        else:
            c = s[i]
        r = m[i]*r +c
    return r
def unrank(num,m):
    s = [0 for _ in range(len(m))]
    for i in reversed(range(len(m))):   
        v = num % m[i]
        num = math.floor(num/m[i])
        if(num%2==1):
            s[i] = m[i]-v-1
        else:
            s[i] = v
    return s
    
print(rank(
    [2,1,8],
    [3,5,10],
))

print(unrank(
    66,
    [3,5,10]
))