import json
from getpass import getpass
from utils import is_valid_password, is_valid_name, make_password, print_satatus
from models import User
from task import Task  # Ensure there is a 'task.py' file in the same directory as this script


class Manager:
    def __init__(self):
        self.user = None
        self.users = self.load_users()

    def register(self):
        name = input("name: ").strip()
        username = input("username: ")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")
        if  not is_valid_name(name):
            print('ism xato\n')
        elif self.check_username(username):
            print(f"{username} tanlangan.\n")
        elif password != confirm_password:
            print("password bilan confirm password bir xil emas.\n")
        elif not is_valid_password(password):
            print("xato password.")
        else:
            self.users.append(User(name, username, make_password(password)))
            self.save_users()
            print("muvaffaqiyatli royxatdan otdingiz.")

    def login(self):
        username = input("username: ")
        password = getpass("password: ")

        hashed_password = make_password(password)

        for user in self.users:
            if user.username == username and user.password == hashed_password:
                print_satatus("muvaffaqiyatli kirdingiz.")
                self.user = user
                return True
        print_satatus("user topilmadi.", "error")
        return False

    @staticmethod
    def load_users():
        import os
        if not os.path.exists('data/users.json'):
            return []
        with open('data/users.json') as jsonfile:
            try:
                data = json.load(jsonfile)
                users = []
                for item in data:
                    user = User.from_dict(item)
                    users.append(user)
                return users
            except Exception:
                return []

    def save_users(self):
        with open('data/users.json', 'w') as jsonfile:
            data = [user.to_dict() for user in self.users]
            json.dump(data, jsonfile, indent=4)

    def check_username(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False
    def create_task(self):
        """Task yaratish"""
        title = input("Task nomi: ")
        description = input("Tavsif: ")
        task = Task(title, description)
        self.user.add_task(task)
        print_satatus(f"'{title}' yaratildi!", 'success')
    
    def show_tasks(self):
        """Tasklarni ko'rsatish"""
        tasks = self.user.get_tasks()
        
        if not tasks:
            print_satatus("Task yo'q!", 'error')
            return
        
        print(f"\n{self.user.name} tasklari:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task.completed else "○"
            print(f"{i}. {status} {task.title}")
        
        # Task bajarish uchun
        try:
            num = int(input("\nQaysi taskni bajarasiz? (0 - chiqish): "))
            if num > 0 and num <= len(tasks):
                tasks[num-1].mark_as_completed()
        except:
            pass
