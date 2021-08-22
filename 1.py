#calculate the sum of the digits of an integer

num = int(input("Please, enter a three-digit number: "))
x1 = (num % 100)% 10
x2 = ((num-x1)/10)% 10
x3 = (((num-x1)/10)-x2)/10

print(x1+x2+x3)


