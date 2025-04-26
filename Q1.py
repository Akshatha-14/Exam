#There are n houses build in a line, each of which contains some value in it.

#A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will
#tell his two neighbors left and right side.

#What is the maximum stolen value?

def main(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])
    return dp[-1]
Sample_Input = [6, 7, 1, 3, 8, 2, 5]
print(main(Sample_Input))  



