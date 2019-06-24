all=int(input())
m=int(input())

protmy=str(int(input()))
for i in range(m):
    

b=int(input())

protsale=str(int(input()))
sale=protsale.split()

re=list(set(sale) - set(my))
print(re)
