a=list(range(1,14))
box=[]
for b in a:
    c=(b+10)%13
    box.append(c)

print(a)
print(box)

#  a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#       ||
#box=[11,12,0,1,2,3,4,5,6,7,8,9,10]
#2が最強3が最弱
