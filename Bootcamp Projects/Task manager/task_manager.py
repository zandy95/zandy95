# The following sources were used to assist in parts of the project;
# https://www.w3schools.com/python/ref_string_split.asp
# https://realpython.com/python-in-operator/#putting-pythons-in-and-not
# -in-operators-into-action
# https://realpython.com/python-pep8/
# https://builtin.com/software-engineering-perspectives/python-
# remove-character-from-string
# https://stackoverflow.com/questions/14532875/creating-for-
# loop-until-list-length
 
user_path = ("user.txt")
task_path = ("tasks.txt")

def data_checker(username, password,user_path):
    with open (user_path, "r+") as file:
    # The data needs to be given a name so it can be represented 
    # in a simple way for our code.
        for line in file:
            line = line.strip()
            line = line.replace(","," ")
            line = line.split()
        # We strip and split the lines to ensure that we can call the 
        # user and password separetly.Replacing the "," ensures the code doesn't
        # read it as part of the username.
            if len(line) == 2:
                if line[0] == username and line[1] == password:
                    return True
    return False


username = input("Enter your username:")
password = input("Enter your password:")

while not data_checker(username, password, user_path):
    # In this section, starting off with while not helps with being able
    # to sort out any issues that might arise with the incorrect inputs
    # before getting into the tasks at hand, so that while true can be
    # used for that part of the code. 
    print("You have entered the wrong username or password. \n \
          Note: username and password are case sensitive.")
    username = input("Enter your username:")
    password = input("Enter your password:")


while True:
    if username == 'admin':
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    vs - view statistics
    e - exit
    : ''').lower()
        
    else:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

    if menu == 'r':
        if menu == 'r'and username != 'admin':
            print("You are not authorised to add a user.")

        else:
            new_username = input("Please enter the new username:")
            new_password = input("Please enter a new password:")
            password_conf = input("Please confirm your password:")
            
            if password_conf != new_password:
                print("Password doesn't match")
                password_conf = input("Please confirm your password:")

            else:
                file = open(user_path, "a+")
                file.write(str("\n" + (new_username) + "," + " " + (new_password)))
                file.close()

    elif menu == 'a':
        
        user_assigned = input("Enter the name of the user the task is assigned to:")
        task_title = input("Enter the title of the task:")
        task_descr = input("Enter the description of the task:")
        due_date = input("Enter the due date of the task:")
        current_date = input("Enter the current date:")
        task_complete = input("Is the task completed? Yes or No:")

        task = open(task_path, "a+")
        # The code below ensures that the text appended text matches the 
        # format already in the file and ensures there are no errors
        # in other codes using the text.
        task.write(str("\n" + (user_assigned) + "," + " " + (task_title) 
                       + "," + " " + (task_descr) + "," + " " + (due_date) 
                       + "," + " " + (current_date) + "," + " " 
                       + (task_complete) + "\n"))

        task.close()

    elif menu == 'va':
        with open (task_path, "r") as file:
            for line in file:
                line = line.split(',')
                
                print(str("Task:" + "                   " + (line[1]) + "\n"))
                print(str("Assigned to :" + "            " + (line[0]) + "\n"))
                print(str("Date assisgned:" + "         " + (line[3]) + "\n"))
                print(str("Task Completed?" + "         " + (line[4]) + "\n"))
                print(str("Task Description:" + "       " + "\n" + (line[2])))
                print("\n")

    elif menu == 'vm':
        with open (task_path, "r") as file:
            for line in file:
                line = line.split(',')

                if username == line[0]:
                    print(str("Task:" + "                   " + (line[1]) + "\n"))
                    print(str("Assigned to :" + "            " + (line[0]) + "\n"))
                    print(str("Date assigned:" + "         " + (line[3]) + "\n"))
                    print(str("Task Completed?" + "         " + (line[4]) + "\n"))
                    print(str("Task Description:" + "       " + "\n" + (line[2])))
                    print("\n")

    elif menu == 'vs':
        # This code will only be visible to the admin to pull the statistics.
        with open (user_path, "r") as file:    
            user_count = 0
            for line in file:
                user_count += 1

            print("The number of users is:" , (user_count))

        with open (task_path, "r") as file:    
            task_count = 0
            for line in file:
                task_count += 1
            print("The number of tasks is:" , (task_count))

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")