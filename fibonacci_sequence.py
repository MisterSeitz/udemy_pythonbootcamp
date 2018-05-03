def fibo(x):
    if x <= 1:
        return x
    else:
        return(fibo(x-1) + fibo(x-2))

fibo_nth = input("Please enter a number to generate fibonacci sequence: ")
fibo_nth = int(fibo_nth)

while fibo_nth <= 0:
    print("Please enter positive integer")
else:
    print("Fibonacci Sequence to {} Numbers: ".format(fibo_nth))
    for i in range(fibo_nth):
          print(fibo(i))
