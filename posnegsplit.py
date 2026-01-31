l = [1,-2,3,6,7,-5,5]


lpos = []
lneg = []
for i in l:
    if(i>0):
        lpos.append(i)
    if(i<0):
        lneg.append(i)


print(lneg)
print(lpos)

l = lneg + lpos
print(l)