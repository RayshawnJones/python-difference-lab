# Get Name
# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

def get_name():
    name = input("What is your name? ")
    return name

# Reverse It
# Write a method that reverses a string. Here’s the javascript:


# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

# Notes: Explanation: String Slicing: uses slicing to access a portion of a string. Syntax: string[start:end:step] allows you to specify a start point, a stop point, and an end point. Using -1 as the step, Python will start from the end of the string and work backwards.

def reverse_it():
    string = "a man, a plan, a canal, frenemies!"
    reverse = string[::-1]
    print(reverse)

reverse_it() # function prints the reversed string


# Notes: Explanation: swap the values of two variables using a function called swap_em(). Inside the function, variables "a" and "b" are initialized with values 10 and 30. It then uses a temporary variable to swap the values and prints the new values of "a" and "b". After the function swap_em() is called, it effectively swaps the values of "a" and "b".

# Swap Em
# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swap_em():
    a = 10
    b = 30

    temp = b
    b = a
    a = temp

    print(f"a is now {a}, and b is now {b}")

swap_em()

# Multiply Array/List
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# notes: explanation: initializes a total variable to 1 and iterates through the list, multiplying each element by the running total. Finally, it returns the total

def multiply_array(ary):
    if len(ary) == 0:
        return 1
    total = 1
    for number in ary:
        total *= number
    return total

# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }


# notes: explanation: checks if x is divisible by both 3 and 5. This is done by using the modulus operator %, which returns the remainder of the division. If x is divisible by 15 (which is the product of 3 and 5), the remainder will be 0. In this case, the function returns the string 'fizzbuzz'.

# If x is not divisible by 15, the function then checks if x is divisible by 3. If it is, the function returns the string 'fizz'.

# If x is not divisible by either 15 or 3, the function checks if x is divisible by 5. If it is, the function returns the string 'buzz'.

# If x is not divisible by 15, 3, or 5, the function returns the string 'archer'.
def fizzbuzzer(x):
    if x % (3 * 5) == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 0:
        return 'buzz'
    else:
        return 'archer'

# Nth Fibonacci
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nth_fibonacci_number():
    fibs = [1, 1]
    num = int(input("Which Fibonacci number do you want?"))

    while len(fibs) < num:
        next_fib = fibs[-2] + fibs[-1]
        fibs.append(next_fib)

    print(f"{fibs[-1]} is the Fibonacci number at position {num}")

# call the function to test it
nth_fibonacci_number()

# Search Array/List
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def search_array(array, value):
    for item in array:
        if item == value:
            return True
    return False

# Palindrome
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# function checks whether a given string is a palindrome (reads the same forward and backward).
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

# hasDupes
# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:



def has_dupes(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False
