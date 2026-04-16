def call_counter(func):

    count = 0

    def counter(*args, **kwargs):

        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} has been called {count} times.')
        return result

    return counter

@call_counter
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
greet("Bob")
greet("Charlie")
greet("Alice")
greet("Bob")
greet("Bob")