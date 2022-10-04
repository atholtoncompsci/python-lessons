#IGNORE THIS FILE

'''
TOPICS:
Print
Comments
Variables (Int, string, booleans, naming conventions)
Operators (arithmetic, assignment
Inputs
If, elif, else
While

TUTORIALS:
Hello World
Calculate age given birth year
Input name and birth year
'''

# Instruction will be in comments denoted by # or '''. Actual code
# will not be in comments.

#======== Hello World (Printing)========#
'''
There are multiple types of interfaces for a program, such as a 
console/terminal or a graphical user interface.
Console programs are easier to make, so we will start with those.

Functions can have parameters. You can pass arguments into these
parameters to make the function do something with your data.

The print() command can be used for writing on the console.
It takes one parameter, the text that you want to be printed
on the console.
print(text)

Text can be enclosed in single (') or double (") quotes, but
do not mix the two. If you want your text to contain a single
quote, then use double quotes to enclose your text, or vice versa.
'''

print("Hello world")

#======== Comments ========#

# Comments are used to put notes in your code. Use # at the start
# of a line for single line quotes, or enclose a block of text in
# ''' for a multi-line comment. Examples:

# This is a single line comment!

'''
This comment has multiple lines
You can comment a line of code to stop it from running
'''

#======== Calculate age given birth year (Variables, operators)========#
'''
Variables can be used to store data. They can contain numbers,
text (referred to as "strings"), booleans (a value that can be
True or False), and more.

Boolean values must have the first letter capitalized: True, False

Variables have particular naming rules that must be followed:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
You can't put spaces in variable names.

Declare variables as shown below.
'''

start_year = 1996
duration = 10
first_name = "Lily"
completed = True

'''
You can add values and variables together.
Variables can also be printed.

You can use operators to manipulate data. Some operators:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
**  Exponentation (Do not use ^ for exponents! ^ will do something very different.)
'''

start_year = 1996
duration = 10
end_year = start_year + duration    #end_year will be equal to 2006

print(end_year)

'''
Assignment operators also

'''

