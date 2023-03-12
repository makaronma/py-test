word = 'word'

sentence = "This is a sentence."

paragraph = """This is a paragraph. It is
\\\n made up of multiple lines and sentences."""
print(paragraph)
if True:
    print("True")
else:
    print("False")

someInt = 6
if someInt > 6:
    print("large")
elif someInt == 6:
    print("equal")
else:
    print("small")
'''
asd
'''


def add(a: int, b):
    """Function to add the value of a and b"""
    return a + b


print(add.__doc__)


def sum(x, y):
    sum = x + y
    return sum


print(sum(5, 10))

# integer variable.
a = 100
print("The type of variable having value", a, " is ", type(a))

# float variable.
b = 20.345
print("The type of variable having value", b, " is ", type(b))

# complex variable.
c = 10 + 3j
print("The type of variable having value", c, " is ", type(c))

str = 'Hello World!'

print(str)  # Prints complete string
print(str[0])  # Prints first character of the string
print(str[2:5])  # Prints characters starting from 3rd to 5th
print(str[2:])  # Prints string starting from 3rd character
print(str * 2)  # Prints string two times
print(str + "TEST")  # Prints concatenated string

list = ['abcd' * 2, 786, 2.23, 'john', 70.2]
print(list)

tuple = ('abcd', 786, 2.23, 'john', 70.2)
list = ['abcd', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000  # Valid syntax with list

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # Prints value for 'one' key
print(dict[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

# Returns false as a is not equal to b
a = 2
b = 4
print("1" == 1)
import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)

def func(arr):
    arr = arr+arr
    print(arr)
    return arr
aaa = [1]
aaa = func(arr=a)
print(aaa)

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

from util import sum
print(sum(1,2))


car = {"a": 1,"b":2}
print(car)
