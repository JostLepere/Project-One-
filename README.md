### Project-One- This is my first project EVER ###

**This is a short summary for me personally on what I want to remeber after the first week of learning python with @codeacademyberlin**<br />

The list of most important commands, functions and general things to keep in mind is far from complete, just for me to remember. <br />

We will get started with first **basic functions**. Ususally in python you would destinguish between inbuild functions and functions build by the user. <br />

The most common used functions are the following:

   **#'s** are used to mark comments <br />
   The colon **(:)** at the end of the line indicates that a new code block is starting <br />
   **Strings** in Python mark functions that include only text <br />
<br />
<br />
##Operators##

Operator	  Name	                Description <br />
a + b	      Addition	            Sum of a and b <br />
a - b	      Subtraction	          Difference of a and b <br />
a * b	      Multiplication	      Product of a and b <br />
a / b	      True division	        Quotient of a and b <br />
a // b	    Floor division	      Quotient of a and b, removing fractional parts <br />
a % b	      Modulus	              Integer remainder after division of a by b <br />
a ** b	    Exponentiation	      a raised to the power of b <br />
-a	        Negation	            The negative of a <br />

Operators are main commands to use in functions, like using a calculator
<br />
<br />
##bools##

Bools are binary, yes or no, true or false statements e.g. like in the example here:

bools examples
team1_pts = 110 <br />
team2_pts = 120 <br />
<br />
<br />
##if statements##

If statements give conditions to functions

e.g.
if team1_won:
  message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"

message
<br />
<br />
<br />
<br />
**##Container:##**
<br />
Containers will hold different type of lists or dicts, which can hold a string of information and 

**#-> Lists or dicts#**
Always in [ ]    first slot is 0, second is 1 and so on… <br />
                          Negativ Intgr calls end of list 
Sections are called slices<br />
<br />
**lists**
my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']

my_roster_list[0]
my_roster_list[0:2]
my_roster_list[-2:]
<br />
<br />
**dicts** 
Python dicts have key and values <br />
<br />
Hold data and give each piece a name. Written in { } <br />
<br />
my_roster_dict = {'qb': 'tom brady',
                  'rb1': 'adrian peterson',
                  'wr1': 'antonio brown'}
<br />
<br />
<br />
**Indexing**
You can access individual list elements with square brackets. <br />
Which planet is closest to the sun? Python uses zero-based indexing, so the first element has index 0 <br />
List functions <br />
len  #length of list <br /> 
sorted #sort in specific order <br />
sum #sum <br />
<br />
<br />
.append   #adds an appendix which e.g. doesn’t really belong to the list <br />
<br />
<br />
**Tuples**
Tuples are almost exactly the same as lists. They differ in just two ways. <br />
1: The syntax for creating them uses parentheses instead of square brackets <br />
2: They cannot be modified (they are immutable). <br />
t = (1, 2, 3)    # e.g. <br />

