enuzunzincir=0
zincirsayısı=[]
a=0
for i in range(2,1000000):
    b=i
    while b>1:
        if b %2==0:
          b=b>>1
        else:
           b=(b<<1)+b+1
        zincirsayısı.append(b)
    if len(zincirsayısı)>enuzunzincir:
          enuzunzincir=len(zincirsayısı)
          a=i
    zincirsayısı.clear()       
print(a)
print(enuzunzincir)              