def hello_world():
    """Return a greeting message."""
    return "Hello, World from Jenkins CI/CD!"

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    print(hello_world())
    print(f"5 + 3 = {add_numbers(5, 3)}")