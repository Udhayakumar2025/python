try:
    number = int(input("Enter a number: "))
    print(100 / number)
except:
    print("Something went wrong.")

#ZeroDivisionError
try:
    num = int(input("Enter number: "))
    print(100 / num)

except ZeroDivisionError:
    print("You cannot divide by zero.")

#ValueError
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Please enter numbers only.")

#Handling Multiple Exceptions
try:
    num = int(input("Enter number: "))
    print(100 / num)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

#else
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

#finally
try:
    print("Opening file")

except:
    print("Error")

finally:
    print("Closing file")

#Example 
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print(f"Welcome {name}")

except ValueError as e:
    print("Error:", e)

finally:
    print("Program ended.")                       