def check_access(func):
    def wrapper(user):
        if user['role'] == 'admin':
            return func(user)
        else:
            print("Access denied. Admins only.")
    return wrapper

@check_access
def delete_user(user):
    print(f"User {user['name']} has been deleted.")

# Example usage
admin_user = {'name': 'Alice', 'role': 'admin'}
delete_user(admin_user)

# Example with non-admin user
regular_user = {'name': 'Bob', 'role': 'user'}
delete_user(regular_user)