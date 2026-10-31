Basic Authentication and Role-Based Access Control App

This project is a simple Python application that demonstrates the basic concepts of authentication, user roles, and access control. The application uses hardcoded usernames and assigned roles to determine which parts of the program a user is allowed to access. It includes two roles: Admin and User.

The application uses a Python dictionary to store usernames and their assigned roles. For example:
- admin1 is assigned the admin role.
- user1 is assigned the user role.
When the application runs, it checks whether the hardcoded username exists in the dictionary. If the username exists, authentication is successful, and the application retrieves the user's assigned role. If the username does not exist, authentication fails, and the application terminates.

The application contains two different user roles:

Admin
- Can access the Admin Dashboard.
- Can simulate managing users and system settings.
- Cannot access the User Dashboard

User
- Can access the User Dashboard.
- Can simulate viewing personal information.
- Cannot access the Admin Dashboard

The application uses conditional statements (if and else) to check the user's role before granting access to each dashboard.

The application contains two main functions:

admin_dashboard(role)
-This function checks whether the user's role is admin. If the condition is true, access is granted to the Admin Dashboard. Otherwise, access is denied.

user_dashboard(role)
- This function checks whether the user's role is user. If the condition is true, access is granted to the User Dashboard. Otherwise, access is denied.

Both functions demonstrate how access can be restricted based on a user's assigned role.

This application demonstrates the concept of Confidentiality, one of the three principles of the CIA Triad. Confidentiality means ensuring that information is only accessible to authorized individuals. The application demonstrates this by restricting access to certain dashboards based on the user's assigned role. For example, a regular user cannot access the Admin Dashboard. This helps demonstrate how role-based access control can protect sensitive information from unauthorized access.