# Python program to print all prime numbers between 1 to 20
lower=0;
upper=20;
print("Prime numbers between ",lower," and ",upper,"are: ")
for num in range(lower,upper + 1):
  # all prime nos are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)