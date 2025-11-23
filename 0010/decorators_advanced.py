"""
Decorador que controla el acceso a una función basada en el rol del usuario.
"""
def check_access(role_required):
    def decorator(func):
        def wrapper(user):
            if user['role'] != role_required:
                print(f"Access denied for user {user['name']}. Required role: {role_required}.")
                return
            return func(user)
        return wrapper
    return decorator

def log_action(func):
    def wrapper(user):
        print(f"Action logged for user {user['name']}.")
        return func(user)
    return wrapper

@check_access('admin')
@log_action
def delete_user(user):
    print(f"User {user['name']} has been deleted.")

# Example usage
admin_user = {'name': 'Alice', 'role': 'admin'}
delete_user(admin_user)

# Example with non-admin user
regular_user = {'name': 'Bob', 'role': 'user'}
delete_user(regular_user)