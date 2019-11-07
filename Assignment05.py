# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# GSears,11.6.2019,commented out sample dictionary content (line 17)
# Gsears,11.6.2019, renamed objFile to strFile and declared empty objFile
# Gsears,11.6.2019, added code to read-in ToDoList.txt file
# GSears,11.6.2019, added code to display current data (option 1)
# GSears,11.6.2019, added code to add new items to list (option 2)
# GSears,11.6.2019, added code to delete items from list (option 3)
# GSears,11.6.2019, fixed error in delete item (option 3)
# GSears, 11.6.2019 added loop to write current data to txt file, replacing old data (option 4)
# Gsears, 11.6.2019 added exit option to the menu (option 5)
# GSears, 11.6.2019 moved import of data from ToDoList.txt to option 1
# Gsears, 11.6.2019 used try...except error recovery to allow deletion
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
strFile = 'ToDoList.txt' # an object that represents a file
objFile = None # an object that will be handle for connection to file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary
# {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here
objFile = open(strFile,"r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user

while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Task"," | ","Priority")
        for row in lstTable:
            print(row["Task"]," | ",row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        taskEntry = input("Enter the name of the task: ")
        taskPri = input("Enter the priority of the task (1-Low to 5-Highest): ")
        dicRow = {"Task": taskEntry, "Priority": taskPri}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        taskDelete = input("Enter the name of the task to delete: ")
#        objFile = open(strFile)
        for row in range(len(lstTable)):
            try:
                while lstTable[row]['Task'] == taskDelete:
                    del lstTable[row]
            except:
                continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"]+','+row["Priority"]+'\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Thank you for using the ToDo Manager.')
        input('Please hit Enter to exit the program.')
        # TODO: Add Code Here
        break  # and Exit the program

