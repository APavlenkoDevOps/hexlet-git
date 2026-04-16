def make_check(role):

        def check(user_role):
            return user_role == role
        return check

    



def required_role(role):
    def decorator(func):
        def wrapper(user_role):
            if role == user_role:
                return func(user_role)
            else:
                print(f"Access denied for role: {user_role}. Required role: {role}.")
        return wrapper
    return decorator