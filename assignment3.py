#Ques:1 sum of all numbers in list
x = list(map(int,input().split()))
sum = 0
for i in x:
    sum += i
print("Sum of given list:", sum)

#Ques:2 Reverse a string
x = input("Enter the string:")
reverse = x[::-1]
print("Reverse of given string is:", reverse)

#Ques:3 Calculate the upper and lower case letter
text = input("Give a sentence = ")
upper = 0
lower = 0
for i in text:
    if i.isupper():
        upper += 1
    else:
        lower += 1
print("No of upper character is:", upper)
print("No of lower character is:", lower)

