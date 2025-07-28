from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")  
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅ Completed" if self.completed else "❌ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date.date()}\nStatus: {status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.\n")
                return
        print(f"No task found with title '{title}'.\n")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.completed]
        if not incomplete:
            print("All tasks are complete!\n")
        for task in incomplete:
            print(task)



def main():
    todo_list = ToDoList()

    while True:
        print("ToDo List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Show Incomplete Tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task = Task(title, description, due_date)
                todo_list.add_task(task)
                print("Task added successfully!\n")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.\n")

        elif choice == "2":
            title = input("Enter the title of the task to mark complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            print("\nAll Tasks:")
            todo_list.list_all_tasks()

        elif choice == "4":
            print("\nIncomplete Tasks:")
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()






from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content
        self.timestamp = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content: {self.content}\n")
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully!\n")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.\n")
            return
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author.lower() == author.lower()]
        if not filtered:
            print(f"No posts found by author '{author}'.\n")
            return
        for post in filtered:
            print(post)

    def delete_post(self, title):
        for i, post in enumerate(self.posts):
            if post.title == title:
                del self.posts[i]
                print(f"Post '{title}' deleted.\n")
                return
        print(f"No post found with title '{title}'.\n")

    def edit_post(self, title, new_title, new_content):
        for post in self.posts:
            if post.title == title:
                post.edit(new_title, new_content)
                print(f"Post '{title}' updated successfully.\n")
                return
        print(f"No post found with title '{title}'.\n")

    def latest_posts(self, count=3):
        if not self.posts:
            print("No posts to display.\n")
            return
        sorted_posts = sorted(self.posts, key=lambda p: p.timestamp, reverse=True)
        for post in sorted_posts[:count]:
            print(post)


def main():
    blog = Blog()

    while True:
        print("\nSimple Blog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.posts_by_author(author)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_title, new_content)

        elif choice == "6":
            try:
                count = int(input("How many latest posts to display? (default 3): ") or "3")
                blog.latest_posts(count)
            except ValueError:
                print("Invalid number. Please enter a valid integer.\n")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()





class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to account {self.account_number}.\n")
        else:
            print("Deposit amount must be positive.\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}.\n")
        else:
            print("Insufficient balance for withdrawal.\n")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name  : {self.holder_name}")
        print(f"Balance      : ${self.balance:.2f}\n")



class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def add_account(self, account):
        if self.find_account(account.account_number):
            print("Account with this number already exists.\n")
        else:
            self.accounts.append(account)
            print("Account created successfully.\n")

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"Balance for account {account_number}: ${acc.balance:.2f}\n")
        else:
            print("Account not found.\n")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.\n")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.\n")

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)

        if not from_acc or not to_acc:
            print("One or both accounts not found.\n")
            return

        if from_acc.balance >= amount:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f"Transferred ${amount:.2f} from {from_acc_num} to {to_acc_num}.\n")
        else:
            print("Transfer failed: insufficient funds.\n")

    def display_account(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            acc.display()
        else:
            print("Account not found.\n")





def main():
    bank = Bank()

    while True:
        print("Simple Banking System")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            try:
                balance = float(input("Enter initial deposit: "))
                bank.add_account(Account(acc_num, name, balance))
            except ValueError:
                print("Invalid input for balance.\n")

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(acc_num, amount)
            except ValueError:
                print("Invalid input for amount.\n")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print("Invalid input for amount.\n")

        elif choice == "5":
            from_acc = input("Enter sender account number: ")
            to_acc = input("Enter receiver account number: ")
            try:
                amount = float(input("Enter amount to transfer: "))
                bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print("Invalid input for amount.\n")

        elif choice == "6":
            acc_num = input("Enter account number: ")
            bank.display_account(acc_num)

        elif choice == "7":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()
