
x = 0

while True:
    # if x == 5:
    #     break
    print(x)
    x += 1


#break in Loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num==3:
        print("found")
        break
    print(num)

#continue in Loop
for num in nums:
    if num==3:
        print("found")
        continue
    print(num)

#Nested Loop
for num in nums:
    for letter in 'abc':
        print(num,letter)

#Range Loop
for i in range(1,10,2):
    print(i)
    
#While Loop
i=0
while i < 10:
    if i ==5:
        break
    print(i)
    i=i+1

while True:
    if i == 5:
        break
    print(i)
    i = i + 1
