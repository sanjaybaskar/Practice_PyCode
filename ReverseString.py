# Python program for Reverse String

def ReverseString(string):
    return string[:: -1]


print("Enter any string: ")
a = input()
print(ReverseString(a))
