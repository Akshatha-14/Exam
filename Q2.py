#Q2.
#Print the pattern
#11112
#32222
#33334
#54444
#55556
for i in range(5):
    for j in range(5):
        print((i//2*2+1) if (i+j)%4!=1 else i+2, end="")
    print()

