Homework 1: ToDo List Application
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status=False):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = status  # False = incomplete, True = complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "Completed" if self.status else "Incomplete"
        return f"Title: {self.title}, Due: {self.due_date.date()}, Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.status]

def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            task = Task(title, desc, due)
            todo.add_task(task)
            print("Task added.")
        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            if todo.mark_task_complete(title):
                print("Task marked as complete.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("\nAll Tasks:")
            for task in todo.list_all_tasks():
                print(task)
        elif choice == "4":
            print("\nIncomplete Tasks:")
            for task in todo.list_incomplete_tasks():
                print(task)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
Homework 2: Simple Blog System
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_title=None, new_content=None):
        if new_title:
            self.title = new_title
        if new_content:
            self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return self.posts

    def posts_by_author(self, author):
        return [post for post in self.posts if post.author == author]

    def delete_post(self, title):
        for i, post in enumerate(self.posts):
            if post.title == title:
                del self.posts[i]
                return True
        return False

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                post.edit(new_title, new_content)
                return True
        return False

    def latest_posts(self, n=5):
        return self.posts[-n:]

def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Post Title: ")
            author = input("Author: ")
            content = input("Content: ")
            blog.add_post(Post(title, content, author))
            print("Post added.")
        elif choice == "2":
            for post in blog.list_posts():
                print(post)
        elif choice == "3":
            author = input("Enter author name: ")
            posts = blog.posts_by_author(author)
            if posts:
                for post in posts:
                    print(post)
            else:
                print("No posts by this author.")
        elif choice == "4":
            title = input("Enter title of post to delete: ")
            if blog.delete_post(title):
                print("Post deleted.")
            else:
                print("Post not found.")
        elif choice == "5":
            title = input("Enter title of post to edit: ")
            new_title = input("New title (press enter to skip): ")
            new_content = input("New content (press enter to skip): ")
            if blog.edit_post(title, new_title if new_title else None, new_content if new_content else None):
                print("Post updated.")
            else:
                print("Post not found.")
        elif choice == "6":
            n = input("How many latest posts to show? (default 5): ")
            n = int(n) if n.isdigit() else 5
            for post in blog.latest_posts(n):
                print(post)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
Homework 3: Simple Banking System
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account No: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.get_account(from_acc)
        to_account = self.get_account(to_acc)
        if from_account and to_account and from_account.balance >= amount > 0:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            return True
        return False

    def display_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            acc_num = input("Account Number: ")
            name = input("Account Holder Name: ")
            bank.add_account(Account(acc_num, name))
            print("Account created.")
        elif choice == "2":
            acc_num = input("Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                print(f"Balance: {account.balance}")
            else:
                print("Account not found.")
        elif choice == "3":
            acc_num = input("Account Number: ")
            amount = float(input("Amount to deposit: "))
            if bank.deposit(acc_num, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed.")
        elif choice == "4":
            acc_num = input("Account Number: ")
            amount = float(input("Amount to withdraw: "))
            if bank.withdraw(acc_num, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed or insufficient funds.")
        elif choice == "5":
            from_acc = input("From Account Number: ")
            to_acc = input("To Account Number: ")
            amount = float(input("Amount to transfer: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed.")
        elif choice == "6":
            acc_num = input("Account Number: ")
            bank.display_account(acc_num)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
