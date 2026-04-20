from random import randint

def generate_unique_id(data: list[dict]) -> int:
    lst_id = []
    for user in data:
        lst_id.append(user.get("id"))
    new_id = randint(1, 1000000)
    while new_id in lst_id:
        new_id = randint(1, 1000000)
    return new_id

def add_new_user(data: list[dict])-> dict:
    return {
        "id": generate_unique_id(data),
        "name": input("Enter name: ").strip().lower() or None,
        "surname":input("Enter surname: ").strip().lower() or None,
        "date of birth":input("date of birth: ").strip().lower() or None,
        "grades mathematics": [],
        "grades polish": [], 
        "grades english":[]        
    }

# --- Zadanie 1: Znajdź po ID ---
def find_user_by_id(data: list[dict], user_id: int) -> dict | None:
    for user in data:
        if user["id"] == user_id:
            return user
    return None

# --- Zadanie 2: Znajdź po imieniu ---
def find_users_by_name(data: list[dict], name: str) -> list[dict]:
    wyniki = []
    for user in data:
        if user["name"] != None and user["name"] == name.lower().strip():
            wyniki.append(user)
    return wyniki

# --- Zadanie 3: Usuń po ID ---
def delete_user_by_id(data: list[dict], user_id: int) -> bool:
    for i in range(len(data)):
        if data[i]["id"] == user_id:
            data.pop(i)
            return True
    return False

# --- Zadania 4, 5, 6: Aktualizacje pól ---
def update_user_name(data: list[dict], user_id: int, new_name: str) -> bool:
    user = find_user_by_id(data, user_id)
    if user != None:
        user["name"] = new_name.lower().strip()
        return True
    return False

def update_user_surname(data: list[dict], user_id: int, new_surname: str) -> bool:
    user = find_user_by_id(data, user_id)
    if user != None:
        user["surname"] = new_surname.lower().strip()
        return True
    return False

def update_user_birth_date(data: list[dict], user_id: int, new_birth_date: str) -> bool:
    user = find_user_by_id(data, user_id)
    if user != None:
        user["date of birth"] = new_birth_date
        return True
    return False

# --- Zadanie 7: Czy zajęte ---
def is_name_taken(data: list[dict], name: str, surname: str) -> bool:
    for user in data:
        if user["name"] == name.lower() and user["surname"] == surname.lower():
            return True
    return False

# --- Zadanie 8: Pokaz jednego ---
def show_one_user(user: dict) -> None:
    if user != None:
        print("--- STUDENT DATA ---")
        for k, v in user.items():
            print(f"{k}: {v}")
    else:
        print("User not found!")

# --- Zadanie 9: Licz wszystkich ---
def count_all_users(data: list[dict]) -> int:
    return len(data)

# --- Zadanie 10: Licz brakujące imiona ---
def count_users_with_missing_name(data: list[dict]) -> int:
    licznik = 0
    for user in data:
        if user["name"] == None or user["name"] == "":
            licznik = licznik + 1
    return licznik

# --- Zadania 11, 12, 13, 14: Średnie ---
def average_math_for_user(user: dict) -> float | None:
    oceny = user["grades mathematics"]
    if len(oceny) == 0: return None
    suma = 0
    for o in oceny: suma += o
    return suma / len(oceny)

def average_polish_for_user(user: dict) -> float | None:
    oceny = user["grades polish"]
    if len(oceny) == 0: return None
    suma = 0
    for o in oceny: suma += o
    return suma / len(oceny)

def average_english_for_user(user: dict) -> float | None:
    oceny = user["grades english"]
    if len(oceny) == 0: return None
    suma = 0
    for o in oceny: suma += o
    return suma / len(oceny)

def overall_average_for_user(user: dict) -> float | None:
    wszystkie = user["grades mathematics"] + user["grades polish"] + user["grades english"]
    if len(wszystkie) == 0: return None
    suma = 0
    for o in wszystkie: suma += o
    return suma / len(wszystkie)

# --- Zadanie 16: Średnia przedmiotu dla wszystkich ---
def subject_average_for_all_users(data: list[dict], subject: str) -> float | None:
    wszystkie_oceny = []
    for user in data:
        wszystkie_oceny += user[subject]
    if len(wszystkie_oceny) == 0: return None
    suma = 0
    for o in wszystkie_oceny: suma += o
    return suma / len(wszystkie_oceny)
    



