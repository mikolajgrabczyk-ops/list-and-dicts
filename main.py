from functions import data
from functions import users
import os
import time 

def program_menu()->None:
        print(
    """
    ================================================
    \n
    e - exsit
    w - add user
    r - data inf
    t - find user by id (Zad 1 & 8)
    y - delete user (Zad 3)
    u - update name (Zad 4)
    i - update surname (Zad 5)
    s - search by name (Zad 2)
    p - show statistics (Zad 9-16)
    \n
    ================================================
    """)


def main(): 
    loaded_data:list[dict] = data.read_data()
    while True:
        program_menu()
        inp = input("- ").lower().strip()
        if inp == "e":
            print("The program has finished running")
            data.save_data(loaded_data)
            break
        elif inp == "w":
            new_user = users.add_new_user(loaded_data)
            loaded_data.append(new_user)
            data.save_data(loaded_data)
        elif inp == "r":
            data.print_all_data(loaded_data)
        elif inp == "t":
            idx = int(input("Enter ID: "))
            u = users.find_user_by_id(loaded_data, idx)
            users.show_one_user(u)
            
        elif inp == "y":
            idx = int(input("Enter ID to delete: "))
            res = users.delete_user_by_id(loaded_data, idx)
            print("Success:", res)
            
        elif inp == "u":
            idx = int(input("Enter ID: "))
            n = input("New name: ")
            res = users.update_user_name(loaded_data, idx, n)
            print("Success:", res)
            
        elif inp == "i":
            idx = int(input("Enter ID: "))
            s = input("New surname: ")
            res = users.update_user_surname(loaded_data, idx, s)
            print("Success:", res)
        
        elif inp == "s":
            s = input("Enter name: ")
            res = users.find_users_by_name(loaded_data, s)
            data.print_all_data(res)
            
        elif inp == "p":
            # Przykład statystyk (Zadania 9-16)
            print(f"Total users: {users.count_all_users(loaded_data)}")
            print(f"Missing names: {users.count_users_with_missing_name(loaded_data)}")
            # Średnia matematyki dla całej szkoły
            avg_m = users.subject_average_for_all_users(loaded_data, "grades mathematics")
            print(f"School Math Average: {avg_m}")
            avg_p = users.subject_average_for_all_users(loaded_data, "grades polish")
            print(f"School Polish Average: {avg_p}")
            avg_e = users.subject_average_for_all_users(loaded_data, "grades english")
            print(f"School English Average: {avg_e}")

        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("There is no such command")
            time.sleep(2)


if __name__ == '__main__':
    main()