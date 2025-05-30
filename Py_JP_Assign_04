'''Q1.
An e-commerce store stores information about its products in a nested dictionary. The outer dictionary uses product IDs as keys, and the inner dictionary stores product details like name, category, price, and stock quantity. products = { 101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50}, 102: {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200}, 103: {"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30} }
• Increase the stock of the "Shirt" product (add 50 more units)
• Add a new product (e.g., "Smartphone")'''



products = {
    101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50},
    102: {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200},
    103: {"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30}
    }

# Increase the stock of the "Shirt" product (add 50 more units)
products[102]["stock"] += 50
# Add a new product (e.g., "Smartphone")
products[104] = {"name": "Smartphone", "category": "Electronics", "price": 800, "stock": 100}
print(products)




'''
Q2.
You are given a list that contains some duplicate items. Remove the duplicates
shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]'''



shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
# Remove duplicates by converting the list to a set and then back to a list
shopping_list = list(set(shopping_list))
print(shopping_list)




'''
Q3.

You are managing a list of students enrolled in two different courses. You need to perform various set operations to understand the student enrollment. 
Task: Create two sets: one for students in "Course A" and one for students in "Course B". Find the students who are in "Course A" but not in "Course B" (difference). 
Find students who are only in one of the two courses (symmetric difference). 
course_a = {"John", "Alice", "Bob", "David"} 
course_b = {"Alice", "Eve", "Charlie", "David"}
• Find students who are in Course A but not in Course B (difference)
• Find students who are only in one of the two courses (symmetric difference)'''

course_a = {"John", "Alice", "Bob", "David"}
course_b = {"Alice", "Eve", "Charlie", "David"}
# Find students who are in Course A but not in Course B (difference)
students_in_a_not_b = course_a - course_b
# Find students who are only in one of the two courses (symmetric difference)
students_only_in_one = course_a ^ course_b
print("Students in Course A but not in Course B:", students_in_a_not_b)
print("Students only in one of the two courses:", students_only_in_one)




'''
Q4.
Write a Python program that calculates the sum of all even numbers between 1 and 50 (inclusive) using a for loop.

Hint
- Initialize a variable to hold the sum (e.g., sum_of_evens).
- Use a for loop to iterate through all numbers from 1 to 50.
- Inside the loop, check if the number is even.
- If the number is even, add it to sum_of_evens.
- After the loop finishes, print the total sum of all even numbers between 1 and 50.'''

sum_of_evens = 0
for number in range(1, 51):
    if number % 2 == 0:
        sum_of_evens += number 
print("Sum of all even numbers between 1 and 50:", sum_of_evens)



'''
Q5.Q5. Power of a Number Write a Python program that takes a number and prints the powers of the number (starting from 1 to 10) using a while loop. For example, if the user inputs 3, the output should be:

3^1 = 3
3^2 = 9
3^3 = 27

... up to 3^10.'''


number = int(input("Enter a number: "))
power = 1
count = 1
while count <= 10:
    result = number ** power
    print(f"{number}^{power} = {result}")
    power += 1
    count += 1



'''
Q6. 
Problem Statement: Write a Python program that takes an integer input from the user and counts down from that number to 0. 
The program should display the current number at each step until it reaches 0, 
at which point it should print a message indicating the countdown is finished
Output Hint:
Enter a number to start the countdown: 3
3
2
1
0

Countdown finished!'''


number = int(input("Enter a number to start the countdown: "))
while number >= 0:
    print(number)
    number -= 1
print("Countdown finished!")



'''
Q7.
Write a Python program that takes a number as input from the user and calculates its factorial using a for loop. The program should display the result to the user.

Example Input/Output:
Input:
5
Output:
The factorial of 5 is 120'''


number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")




'''
Q8.
Create an empty dictionary called person_info.
Assign the following key-value pairs to the dictionary:

"name": "Alice"
"age": 25
"occupation": "Engineer"
After assigning the values, print the dictionary.'''


person_info = {}
person_info["name"] = "Alice"  
person_info["age"] = 25
person_info["occupation"] = "Engineer"
print(person_info)



'''
Q9.print 
* 
* * 
* * * 
* * * * 
* * * * * '''
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

'''
Q10.

Write a Python program that does the following:

Range: Loop through numbers from 1 to 20 (inclusive).

Continue: If the number is divisible by 4, skip that iteration and move to the next number.

Break: If the number is divisible by 7, stop the loop entirely.

For all other numbers, print the number.'''

for number in range(1, 21):
    if number % 4 == 0:
        continue
    if number % 7 == 0:
        break
    print(number)
