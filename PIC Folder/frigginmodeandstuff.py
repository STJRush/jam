connor put the thing here
ok love you x
I DO NOT

y= [784400000,156880000,5490800000,392200000,392200000,235320000,78440000]
y.sort()
L1=[]
i = 0
while i < len(y) :
    L1.append(y.count(y[i]))
    i += 1
    d1 = dict(zip(y, L1))
    d2={k for (k,v) in d1.items() if v == max(L1) }
 
print("Mode(s) is :" + str(d2))
