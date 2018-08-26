## Find the smallest of 3 numbers

n1 = 0
n2 = 0
n3 = 0

n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))

if ((n1 < n2) & (n1 < n3)):
    print("n1 is the smallest")
if ((n2 < n1) & (n2 < n3)):
    print("n2 is the smallest")
if ((n3 < n1) & (n3 < n2)):
    print("n3 is the smallest")


## Post the add2.py program, given on the course website, by adding proper comments

# Set up variables
n1 = 0
n2 = 0
sum = 0

# Ask the user to input the first number
n1 = input()

# Get the second number by the user
n2 = input()

# Compute the sum of those 2 numbers
sum = float(n1) + float(n2)

# Display the sum
print(sum)


##if-elif-else code
'''
1.Input a number from the user.

2.Use the if, elif, and else statements to check if the number is:

  i.positive, or

  ii.Negative, or

  iii.zero.

3.Display an appropriate message for each result.
'''
# Ask the user for a number
number = float(input("Enter a number: "))

# if the number is positive, then it will print "Positive"
if number > 0:
  print("Positive")

# if the number is negative, then it will print "Negative"
elif number < 0:
  print("Negative")

# if the number is zero, then it will print "Zero"
else:
  print("zero")


## Calculator loop
# state the boolean variable
keepGoing = True

# this loop allows the user to reuse the program
while keepGoing:
    # Display
    print("\t\t\t -----------------\n\t\t\t Python Calculator\n\t\t\t -----------------\n")

    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n0. Exit\n")

    #Ask the user whether they want to add, subtract, multiply, or divide
    operation = int(input("Select the operation: "))

    # if the user inputs 0, then it'll immediately exit the loop
    if operation == 0:
         keepGoing = False
         print("\nExiting the program\n")
         break

    # if the user inputs other numbers , it will tell them to try again
    elif operation > 4:
          print("\nPlease type again\n")

    # if user input 1, 2,3, or 4, it'll later ask for their 2 numbers
    else:
          # Ask the user to input their 2 numbers
          num_1 = float(input("Enter your first number: "))

          num_2 = float(input("Enter your second number: "))

          # it'll do the operations as the user asked
          if operation == 1:
                print("\nAnswer: {} + {} = {}\n".format(num_1, num_2, num_1+num_2))

          elif operation == 2:
                print("\nAnswer: {} - {} = {}\n".format(num_1, num_2, num_1-num_2))

          elif operation == 3:
                print("\nAnswer: {} * {} = {}\n".format(num_1, num_2, num_1*num_2))

          elif operation == 4:
                print("\nAnswer: {} / {} = {}\n".format(num_1, num_2, num_1/num_2))


## for loop Multiplication table
# ask the user for a number
number = int(input("Enter a number: "))
# this will repeat this function
for num in range(1,11):
   # this will multiply the user's number and the list of numbers
   total = number * num
      # Display the statement
      print("{} x {} = {}".format(number, num, total))


## while loop Multiplication table
# ask the user for a number
number = int(input("Enter a number: "))

#state the element
num = 1

# it'll print out all the multiplication
while (num < 11):
   total = number * num
   print("{} x {} = {}".format(number, num, total))
   num = num + 1

## Read text file
'''
Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace)
'''

# Open the file
fileR = open('word.txt', 'r')

# Read the first line of the sentence
line = fileR.readline()

# convert the sentence into list
sentence = line.split()

for word in sentence:
   if len(word) > 20 and " " not in word:
      print(word)

# close the file
fileR.close()


## List of lists
'''
Stores the following table data as a list of lists and post it on the Canvas by tonight. The list name is contacts.

(Points: 0.25 - for a correct list.)

Alfreds Futterkiste               Maria Anders          Germany

Centro comercial Moctezuma        Francisco Chang       Mexico

Ernst Handel                      Roland Mendel         Austria

Island Trading                    Helen Bennett         UK

Laughing Bacchus Winecellars      Yoshi Tannamuri       Canada

Magazzini Alimentari Riuniti      Giovanni Rovelli      Italy
'''
# states the tuples
names_1 = ("Alfreds Futterkiste","Centro Comercial Moctezuma","Ernst Handel","Island Trading","Laughing Bacchus Winecellars","Magazzini Alimentari Riuniti")

names_2 = ("Maria Anders","Francisco Chang","Roland Mendel","Helen Bennett","Yoshi Tannamuri","Giovanni Rovelli")

country = ("Germany","Mexico","Austria","UK","Canada","Italy")

# create a list
contacts =[]

# adding those elements in order
for contact in range(len(names_1)):
contacts.insert(contact,[])

contacts[contact].append(names_1[contact])
contacts[contact].append(names_2[contact])
contacts[contact].append(country[contact])

# display the table
print(contacts)


## Selection Sort Program
'''
Use the following list to test your program:
     [1, 6, 0, 7, 10]
'''

# set up the list
unsorted_list= [1, 6, 0, 7, 10]
# bubble sort
for i in range(len(unsorted_list)):
   for j in range(len(unsorted_list)):
      if unsorted_list[j] > unsorted_list[i]:
         # swap those number in order
         temperary = unsorted_list[i]
         unsorted_list[i]= unsorted_list[j]
         unsorted_list[j] = temperary
# display the sorted list
print(unsorted_list)

