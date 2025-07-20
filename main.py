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

                    choice = input(">")

                    if choice == '1':
                        manager.add_task()
                    elif choice == '2':
                        pass
                    elif choice == '3':
                        pass
                    elif choice == '4':
                        pass
                    elif choice == '5':
                        manager.user = None
                    else:
                        print("xato menu")
        elif op == '2':
            manager.register()
        
        elif op == '3':  # Quit
            print_status("Dastur tugadi. Xayr!", 'success')
            sys.exit(0)
        
        else:
            print_status("Noto'g'ri tanlov!", 'error')

if __name__ == "__main__":
    main()