users = {
    "admin1": "admin",
    "user1": "user"
}

username = "admin1"

if username in users:
    role = users[username]
    print("Authentication successful")
    print("Welcome,", username)
    print("Your role is:", role)
else:
    print("Authentication Failed")
    exit()

def admin_dashboard(role):
    if role == "admin":
        print("\nAccess Granted: Welcome to the Admin Dashboard")
        print("You can manage users and systems settings.")
    else:
        print("\nAccess Denied: Admin privileges required.")

def user_dashboard(role):
    if role == "user":
        print("\nAccess Granted: Welcome to the User Dashboard")
        print("You can manage users and system settings.")
    else:
        print("\nAccess Denied: User role required.")

admin_dashboard(role)
user_dashboard(role)
