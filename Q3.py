#Write program to find first n Disarium numbers and Disarium numbers between two given numbers.

#A number is said to be Disarium if it is equal to sum of its digits raised to the power of their respective position in the number. 
#For example, 135 is a Disarium number. Because, it is equal to sum of its digits raised to the power of their respective position.

#135 = 1^1 + 3^2 + 5^3
#135 = 1 + 9 + 125
def Disarium(input):
    result=[]
    for index in range (len(input)):
        a=(input[index])^index
        result.append(a)
    return result
count=0
for i in range(len(result)):
    count=result[i]+(result[i+1])
print(count)

if count==sum(input):
    print("Disarium number")
else:
    print("Not a disarium number")

input="135"
a=input.replace(""," ")
a=a.split()
print(a)
Disarium(a)