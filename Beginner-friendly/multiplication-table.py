#function print_multiplication_table(n) takes an integer n as input and prints the multiplication table for the given number up to 10. 
#this program contains 2 nested 'for' loops:
#1. the outer loop iterates over the numbers from 1 to 10, inclusive, to print the rows of the multiplication table.
#2. the inner loop iterates from 1 to n+1 to calculae and print the products of the current number (i) in the outer loop with numbers from 1 to n.
#the program then prompts the user to enter a number and calls the function to print the multiplication table for that input number.
                                                                                                                                                                                                                                                        
def print_multiplication_table(n):
        for i in range(1,11):
            for j in range(1, n+1):
                print(i * j, end='\t' )
                print() #print func with no arguments to insert a new line after each row
mul = int(input("Enter the number you want the table for: "))
print_multiplication_table(mul)
