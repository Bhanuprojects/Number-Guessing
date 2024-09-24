class ToDoApp:
    def __init__(self):
        self.accounts = {}  # Dictionary to store user accounts
        self.tasks = {}  # Dictionary to store tasks for each user
        self.logged_in_user = None

    # Sign In: Create a new user account
    def sign_in(self, username, password):
        if username in self.accounts:
            print("Username already exists. Please choose a different one.")
        else:
            self.accounts[username] = password
            self.tasks[username] = []
            print(f"Account created for {username}.")

    # Login: Log in with existing account
    def login(self, username, password):
        if username in self.accounts and self.accounts[username] == password:
            self.logged_in_user = username
            print(f"Welcome {username}! You are logged in.")
        else:
            print("Invalid username or password.")

    # Logout: Log out of the current session
    def logout(self):
        if self.logged_in_user:
            print(f"Goodbye, {self.logged_in_user}!")
            self.logged_in_user = None
        else:
            print("No user is currently logged in.")

    # Add task for the logged-in user
    def add_task(self, task):
        if self.logged_in_user:
            self.tasks[self.logged_in_user].append(task)
            print(f"Task '{task}' added.")
        else:
            print("You need to log in to add tasks.")

    # View tasks for the logged-in user
    def view_tasks(self):
        if self.logged_in_user:
            user_tasks = self.tasks.get(self.logged_in_user, [])
            if not user_tasks:
                print("No tasks in your to-do list.")
            else:
                print(f"{self.logged_in_user}'s To-Do List:")
                for idx, task in enumerate(user_tasks, start=1):
                    print(f"{idx}. {task}")
        else:
            print("You need to log in to view tasks.")

    # Delete task for the logged-in user
    def delete_task(self, task_number):
        if self.logged_in_user:
            user_tasks = self.tasks.get(self.logged_in_user, [])
            if 0 < task_number <= len(user_tasks):
                removed_task = user_tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        else:
            print("You need to log in to delete tasks.")

    # Start the To-Do List App with login and sign-in functionality
    def start(self):
        while True:
            print("\nChoose an option:")
            print("1. Sign In")
            print("2. Login")
            print("3. Add Task")
            print("4. View Tasks")
            print("5. Delete Task")
            print("6. Logout")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.sign_in(username, password)
                
            elif choice == '2':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.login(username, password)
                
            elif choice == '3':
                if self.logged_in_user:
                    task = input("Enter the task: ")
                    self.add_task(task)
                else:
                    print("Please log in to add tasks.")
                    
            elif choice == '4':
                self.view_tasks()
                
            elif choice == '5':
                if self.logged_in_user:
                    task_number = int(input("Enter task number to delete: "))
                    self.delete_task(task_number)
                else:
                    print("Please log in to delete tasks.")
                    
            elif choice == '6':
                self.logout()
                
            elif choice == '7':
                print("Exiting the application. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please try again.")

# Running the app
app = ToDoApp()
app.start()
