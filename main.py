def fact(n) -> object:
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


n = int(input("Enter the number: "))

if n == 1:
    print("Number is equal to 1")
elif n <= 0:
    n = print("Number is less than or equal to 0")
else:
    print("Factorial of ", n, "is", fact(n))


def even(num):
    print("Enter the number: ")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


even(num)
