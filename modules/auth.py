from utils.file_handler import load_users, save_users
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def ensure_admin_exists():
    users = load_users()
    if users:
        return  # Admin already exists

    print("\n🔐 First-time setup: Create Admin Account")
    username = input("Admin username: ")
    password = input("Admin password: ")

    users.append({
        "username": username,
        "password": hash_password(password)
    })
    save_users(users)
    print("✅ Admin account created successfully.\n")


def register():
    print("\n🆕 Register New User (admin only)")
    username = input("Username: ")
    password = input("Password: ")
    confirm = input("Confirm Password: ")

    if password != confirm:
        print("❌ Passwords don't match!")
        return

    users = load_users()
    if any(u["username"] == username for u in users):
        print("⚠️ User already exists!")
        return

    users.append({
        "username": username,
        "password": hash_password(password)
    })
    save_users(users)
    print("✅ User registered!")

def login():
    print("\n🔐 Login")
    username = input("Username: ")
    password = input("Password: ")

    users = load_users()
    hashed = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed:
            print(f"✅ Welcome back, {username.capitalize()}!")
            return True

    print("❌ Invalid credentials.")
    return False
