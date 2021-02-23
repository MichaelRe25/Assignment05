# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): Mike Re, 1/15/21, created script
# ------------------------------------------------------------------------ #

#Data
#Declare variables and constants
objFile = "ToDoList.txt" #An object that represents a file
strData = "" # A row of text data from the file
dicRow = {} # A row of data separated into elements of a dictionary
lstTable = [] #A list that acts as a 'table' of rows
Choice = ""
strMenu = '''Menu of Options
    1) Show current data
    2) Add new item
    3) Remove an existing item
    4) Save data to a file
    5) Exit program
'''

# A menu of user options

#Processing
#Step 1 - When the program starts load any of the data you have in a text file called ToDoList.txt into a python list of dictionary rows
file = open('ToDoList.txt', 'a')
file = open('ToDoList.txt', 'r')
print("These items are on your list already.")
for item in file:
    print(item)
    lstRow = item.split(",")  # Returns a list!
    dicRow = {'Task': lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
file.close()

#Step 2 = Display a menu of choices to the user
while (True):
    print(strMenu)
    choice = str(input('Which option would you like to perform? [1 - 5] \n'))
    #step 3 - Show the current items in the table
    if (choice.strip() == '1'):
        for item in lstTable:
            print(item['Task'] + ' | ' + item['Priority'])
        continue
    #Step 4 - Add a new item to the list/table
    elif (choice.strip() == '2'):
        task = input("What's new on your list?")
        prio = input("How important is it on a scale of 1-10")
        dicappend = {'Task': task, 'Priority': prio}
        lstTable.append(dicappend)
        continue
    #Step 5 = Remove an item from the list/table based on its name
    elif (choice.strip() == '3'):
        removal = input('Which task would you like to remove from the list?')
        for row in lstTable:
            if row['Task'].lower() == removal.lower():
                lstTable.remove(row)
        continue
    #Step 6 - Save Tasks to the ToDoList.txt file
    elif (choice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(row['Task'] + ' , ' + row['Priority'] + '\n')
        objFile.close()

        continue
    #Step 7 - Exit program
    elif (choice.strip() == '5'):
        input('\nPress enter to exit the program.')
        break #end the program