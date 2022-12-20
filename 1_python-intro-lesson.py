#2022.12.20_python-into-lesson.py
#This lesson assumes the reader has some experience in another language (usually Java) already. 

#this is a comment

"""
Long comment
You can use single and double quotes interchangeably for strings and comments
"""

#Python prints strings with a newline at the end by default. You can print without a newline by passing an empty string to the end parameter. The second print below will have a newline added.
print("hello world", end="")
print("test")

#You dont need to declare variable types. True and False are capitalized
var1 = 1
var2 = "ABCD"
var3 = True;

#You can even overwrite variables with new values of different types
var3 = "asdfasdfasdf"
print(var3)

#Combining strings
print(var2 + var3)

#Simple arithmetic is the same as other languages. Python does not do integer division by default, so the decimal will not be truncated. If you want to truncate the decimal, use two slashes
var4_dec = 5/3 #Will give you 1.6666667
var4_int = 5 // 3 #Will give you 1

print(var4_int)

#Code blocks do not use brackets. Instead, use a colon.
#The parentheses around the conditional (var5==true) are optional.
#You must indent properly, and have the same indentation throught the code block.
#Python knows the code block is over when you stop indenting.
#You must consistently use only tabs or only spaces to indent a code block.

var5 = True;
if (var5 == True):
  print("true!")
elif (var5 == False):
  print("false! elif means else if.")
else:
  print("var5 can actually be neither True or False, since variables can change types in Python.")

print("This line is not indented, so it is outside the if-elif-else statement and will run no matter what.")


#Format strings exist in Python too. You can put .format() at the end of any string.
#There is a lot more to them, so read about them online.
print("test {}: {}".format("label", 5))

#While loops are basically the same as Java. The same rules surrounding if block structure apply to loops.
#i++ doesnt exist in Python. Use i += 1.
i = 0;
while (i < 5):
  print(i)
  i += 1

#For loops in Python are equivalent to for-each loops (enhanced for loops) in Java.
#range() returns an array consisting of each number in the range, not including the upper bound: [10, 11, 12, 13, 14]
for j in range(10, 15):
  print(j)


#You can combine different types in lists, and have nested lists.
myList = ["a", "b", "c", 2.13, [2, False, "adf"]]

for thingy in myList:
  print(thingy)

#len() returns the length of a list or string.
print(len(myList))

#Loop through each index value of the array (closer to regular Java for loops)
#If only one parameter is passed to range(), the starting value defaults to 0 and the ending value is the parameter.
for x in range(len(myList)):
  print(x)

#Referencing an index in the list works the same as in Java
print(myList[1])

#You can print the whole list
print(myList)


#Lists differ from Java arrays not just because they can store multiple data types, but also because they can change in length. They are comparable to an ArrayList in Java.

#Add values to the end of the list
myList.append("d")
myList.append("c")
print(myList)

#Remove the item at index 1 (The second element of the array. Remember, the index of the first element is 0!)
#pop will remove the last item by default if no parameter is passed
myList.pop(1)
print(myList)

#Remove will remove the first element in the list that matches the parameter.
#If multiple instances of the parameter exist, only the first will be removed.
myList.remove('c')
print(myList)

#insert() adds a variable into an array at an index other than the end. The existing elements are pushed forward by one index, and nothing is overwritten. This example adds "qwerty" to the third space in the array.
myList.insert(2, "qwerty")


#Get user input. The parameter will be printed as a prompt.

myString = input("Enter text: ")
print("You entered:" + myString)


#All input will be treated as a string. You must cast it to another data type if needed.
#In Java, casting is done like this: (int)myNum
#In Python: int(myNum)

myNum = int(input("Enter a number: "))
print(myString + 1) #If you did not cast to int, myNum would still be a string, and the character "1" would be appended to whatever you inputted.
