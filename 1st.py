'''Check if a Number is Positive and Negative in Python'''
def integer_check(number) -> None :
    if number < 0:
        print("number is negetive")
    else:
        print("nnumber is positive")

    
number = input("enter the number")
integer_check(number)