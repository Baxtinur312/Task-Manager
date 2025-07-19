import sys
from utils import print_main, print_status, print_menu
from manager import Manager

def main() -> None:
    manager = Manager()

    while True:
        print("\n" + "="*30)
        print_main()
        op = input("> ")

        if op == '1':  # Sign In
            if manager.login():
                while manager.user:
                    print_status(f"{manager.user.name} sizni accounting.")
                    print_menu()

                    choice = input("> ")
                    
                    if choice == '1':  # Task Yaratish
                        manager.create_task()
                    elif choice == '2':  # Tasklarni Ko'rish
                        manager.show_tasks()
                    elif choice == '3':  # Quit (Logout)
                        manager.logout()
                        break
                    else:
                        print_status("Noto'g'ri tanlov!", 'error')
        
        elif op == '2':  # Sign Up
            manager.register()
        
        elif op == '3':  # Quit
            print_status("Dastur tugadi. Xayr!", 'success')
            sys.exit(0)
        
        else:
            print_status("Noto'g'ri tanlov!", 'error')

if __name__ == "__main__":
    main()