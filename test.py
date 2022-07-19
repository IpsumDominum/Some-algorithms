v = []

n = 5
k = 3
for i in range(k):
    v.append(i+1)
v.append(n+1)

done = False
while not done:    
    print(v)
    print(v[0])
    print(n-k+1)
    print("="*10)
    if(v[0]<n-k+1):        
        j = 0
        while True:
            if(v[j+1]> v[j]+1):
                break
            else:
                j +=1
        v[j] = v[j]+1            
        for i in range(j):
            v[i] = i+1
    else:
        done = True
