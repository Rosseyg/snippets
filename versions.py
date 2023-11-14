import sys
import pip
import django

def print_version_and_location(module_name, module):
    version = getattr(module, '__version__', 'N/A')
    location = getattr(module, '__file__', 'N/A')
    print(f"{module_name} version: {version}")
    print(f"{module_name} location: {location}\n")

def main():
    # Python
    print_version_and_location("Python", sys)

    # Pip
    print_version_and_location("Pip", pip)

    # Django
    print_version_and_location("Django", django)

if __name__ == "__main__":
    main()
