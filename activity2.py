try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1/num2
    print("The result is ", result)
    
except ZeroDivisionError:
    print("Division by 0 is error !")
    
except SyntaxError:
    print("a comma is missing, Enter numbers separated by a comma like this 1,2 ")
except:
    print("Wrong input")
else:
    print("No Exceptions")
finally:
    print("This would execute no matter what.")