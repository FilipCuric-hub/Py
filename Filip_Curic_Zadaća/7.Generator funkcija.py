def parni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
def neparni(n):
    for i  in range(n):
        if i % 2 != 0:
            yield i
            
gen1=parni(5)
gen2=neparni(5)

for par in gen1:
    print("Parni: ",par)
for nepar in gen2:
    print("Neparni: ",nepar)
