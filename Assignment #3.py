'''Question 1: Age Group Classification 

Write a Python program that takes the age of a person as input and classifies them into one of the following age groups:

"Child" if the age is between 0 and 12 (inclusive).

"Teenager" if the age is between 13 and 19 (inclusive).

"Adult" if the age is between 20 and 64 (inclusive).

"Senior" if the age is 65 or older.'''


age = int(input('Enter your Age : '))

if 0 <= age <=12:
    print('you are child')

if 13 <= age <=19:
    print('you are Teenager')

if  20<= age <=64:
    print('you are Adult')

if 64<= age:
    print('you are Seniour citizen')




'''Q2. Write a Python program that asks the user to enter an email address. 
The program should check if the email contains the characters @ and "." (ignoring case).
 If either character is present, print "Email format is valid." Otherwise, print "Invalid email format."
'''

email = input('Enter your email : ')

if '@' in email and '.' in email:
    print('Valid email format')

else:
    print('Invalid Email Format')






'''Q3. Write a Python program that takes three numbers as input and determines the largest among them. 
Also, check if any or all of the numbers are equal.'''



num1 = float(input('Enter your 1st Number : '))
num2 = float(input('Enter your 2nd Number : '))
num3 = float(input('Enter your 3rd Number : '))

if num1==num2==num3:
    print('All numbers are eqaual')

elif num1==num2 or num1 == num3 or num2 == num3:
    print('two numbers are equal')
elif num1>num2 and num1>num3:
    print('1st number is greater')
elif num2>num1 and num2>num3:
    print('2nd number is greater')
elif num3>num1 and num3>num2:
    print('3rd number is greater')






'''
Q4. Write a Python program that:

Asks the user to enter a number.

Checks whether the number is positive.

If yes, further check if it's even or odd.

Print "The number is positive and even" if divisible by 2.

Print "The number is positive and odd" if not divisible by 2.

If the number is zero or negative, print "The number is not positive".'''


number = int(input('Enter your number : '))

if number > 0:
    if number % 2 == 0:
        print('The number is positive and even')
    else:
        print('The number is positive and odd')
elif number == 0:
    print('The number is zero')
else:
    print('The number is negative or zero')


'''Q5. Ask the user for a username and password. Check if the username is correct. If it is,
 then check if the password is correct. If both are correct, print "Access granted".
username = "admin"
password = "1234"'''

username = (input('Enter your username : '))
password = (input('Enter your password : '))

if username == 'admin':
    if password == '1234':
        print('Access granted')
    else:
        print('Incorrect password')




'''Q6. Take an integer input from the user and check whether the entered value exists in the tuple 
my_tuple = (5, 10, 15, 20, 25).
Print an appropriate message based on the result.
'''

tuple_check = int(input('Enter your age : '))
my_tuple = (5, 10, 15, 20, 25)
if tuple_check in my_tuple:
    print('The entered value exists in the tuple')
else:
    print('The entered value does not exist in the tuple')





'''Q7. Create a program that takes the user's first name, last name, and age as input, 
packs them into a tuple, and prints the tuple.'''

first_name = (input('Enter your 1st Nme : '))
Last_name = (input('Enter your 2nd Name : '))
your_age = int(input('Enter your age : '))

my_tuple_1 = (first_name, Last_name, your_age)
print(my_tuple_1)



'''Q9. Given the tuple my_tuple = (1, 2, 3, 4, 5), remove the element 3 from the tuple by first converting it to a list, 
and then print the resulting tuple.'''


my_tuple = (1, 2, 3, 4, 5)
my_tuple_list = list(my_tuple)
my_tuple_list.remove(3)
my_tuple = tuple(my_tuple_list)
print(my_tuple)




'''Q10. Given the tuple numbers = (10, 20, 5, 30, 15), find and print the maximum and minimum values in the tuple.'''

Tupple_2 = (10, 20, 5, 30, 15)
max_value = max(Tupple_2)
min_value = min(Tupple_2)
print('Maximum value in the tuple is : ', max_value)
print('Minimum value in the tuple is : ', min_value)