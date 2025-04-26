tax=[1,2,3,4,5,6]
Ftop,Stop=0,0
for i in range(len(tax)):
    if (Ftop<tax[i]):
        Stop=Ftop
        Ftop=tax[i]
    elif Stop<tax[i] and tax[i]!=Ftop:
        Stop=tax[i]
print(Ftop,Stop)