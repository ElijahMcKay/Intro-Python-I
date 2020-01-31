# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n % 2 == 0:
        print("true")
        return True
    else:
        print("false")
        return False

is_even(10)


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_odd():
    global num
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

even_odd()


