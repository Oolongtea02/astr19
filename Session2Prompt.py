#session 2 prompt
#This program will print the sum of two floating point numbers, the difference between two integers, and the product of a floating point number and an integer.

def Sum_Numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1 + num2
    print("Sum of two numbers: ", sum)
    print(type(sum))

def Difference_Numbers():
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    diff = abs(num1 - num2)
    print("Difference between two integers: ", diff)
    print(type(diff))

def Product_Numbers():
    num1 = float(input("Enter the first number: "))
    num2 = int(input("Enter an integer: "))
    product = num1 * num2
    print("Product of a floating-point and an integer: ", product)
    print(type(product))

def main():
    Sum_Numbers()
    Difference_Numbers()
    Product_Numbers()

if __name__=="__main__":
    main()

