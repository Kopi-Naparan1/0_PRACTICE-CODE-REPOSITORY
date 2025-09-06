import json
from typing import Dict, Any, Callable, Tuple


"""
MAIN LESSON: A well-structured program separates:
1. Data handling (loading/saving)
2. Business logic (contact operations)
3. User interface (input/output)
4. Validation logic
This makes the code easier to maintain, test, and extend.
"""


def get_valid_input(prompt: str, validator: Callable[[str], bool] = None) -> str:
    """
    Generic input validator that ensures non-empty input and optionally validates format
    TEACHING: This demonstrates the power of higher-order functions - we can pass different
    validation functions for different types of input (email, phone, etc.)
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: This field cannot be empty")
            continue
        if validator and not validator(value):
            print("Error: Invalid format")
            continue
        return value


def validate_email(email: str) -> bool:
    """Basic email validation"""
    return '@' in email and '.' in email.split('@')[-1]


def validate_phone(phone: str) -> bool:
    """Basic phone number validation (digits only)"""
    return phone.isdigit()


def display_contact(name: str, info: dict) -> None:
    """
    Unified contact display function
    TEACHING: Centralizing display logic ensures consistent formatting throughout the app_api
    and makes it easy to change how contacts are displayed everywhere at once.
    """
    print(f"\n{'=' * 30}")
    print(f"Contact: {name.title()}")
    print('-' * 30)
    for field, value in info.items():
        print(f"{field}: {value}")
    print('=' * 30)


def display_all_contacts(data: Dict[str, Dict[str, str]]) -> None:
    """Display all contacts with numbering"""
    if not data:
        print("\nNo contacts available")
        return

    print("\nALL CONTACTS:")
    for i, (name, info) in enumerate(data.items(), 1):
        print(f"\nContact #{i}")
        display_contact(name, info)


def add_contacts(data: Dict[str, Dict[str, str]]) -> None:
    """
    Add new contacts until user chooses to stop
    TEACHING: Notice how we've broken down the contact creation into smaller,
    more manageable steps with clear validation for each field.
    """
    print('\n--- ADD NEW CONTACT ---')

    while True:
        name = get_valid_input('Name: ').lower()
        email = get_valid_input('Email: ', validate_email).lower()
        phone = get_valid_input('Phone #: ', validate_phone)
        city = get_valid_input('City: ').title()

        data[name] = {
            "Email": email,
            "Phone": phone,
            "City": city
        }
        print(f"\nContact '{name.title()}' added successfully!")

        if input("\nAdd another? (y/n): ").lower() != 'y':
            break


def update_contact(data: Dict[str, Dict[str, str]]) -> None:
    """
    Update existing contact information
    TEACHING: This shows how to safely modify nested dictionary structures
    with proper validation at each step.
    """
    if not data:
        print("\nNo contacts available to update")
        return

    display_all_contacts(data)

    name = get_valid_input("\nEnter name of contact to update: ").lower()
    if name not in data:
        print(f"\nContact '{name.title()}' not found")
        return

    contact = data[name]
    display_contact(name, contact)

    # Define update options
    update_options = {
        1: ("Email", validate_email),
        2: ("Phone", validate_phone),
        3: ("City", None)  # No special validation for city
    }

    print("\nUpdate Options:")
    for num, (field, _) in update_options.items():
        print(f"[{num}] {field}")

    choice = get_valid_input("Choose field to update (1-3): ",
                             lambda x: x.isdigit() and int(x) in update_options)
    field, validator = update_options[int(choice)]

    new_value = get_valid_input(f"New {field}: ", validator)
    contact[field] = new_value.lower() if field != "Phone" else new_value
    print(f"\n{field} updated successfully!")
    display_contact(name, contact)


def search_contacts(data: Dict[str, Dict[str, str]]) -> None:
    """
    Search contacts by any field with partial matching
    TEACHING: This demonstrates flexible searching across all contact fields
    with case-insensitive matching and proper result display.
    """
    if not data:
        print("\nNo contacts available to search")
        return

    term = get_valid_input("\nSearch term (name/email/phone/city): ").lower()
    results = []

    for name, info in data.items():
        if (term in name.lower() or
                any(term in str(value).lower() for value in info.values())):
            results.append((name, info))

    if not results:
        print("\nNo matching contacts found")
        return

    print(f"\nFound {len(results)} matching contacts:")
    for name, info in results:
        display_contact(name, info)


def save_contacts(data: Dict[str, Dict[str, str]]) -> bool:
    """
    Save contacts to JSON file with error handling
    TEACHING: Proper file operations should always include error handling
    and provide feedback about success/failure.
    """
    try:
        with open('contacts.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("\nContacts saved successfully!")
        return True
    except Exception as e:
        print(f"\nError saving contacts: {str(e)}")
        return False


def load_contacts() -> Dict[str, Dict[str, str]]:
    """
    Load contacts from JSON file with comprehensive error handling
    TEACHING: This shows how to properly handle different types of file-related errors
    and provide appropriate fallback behavior.
    """
    try:
        with open('contacts.json', 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("\nWarning: Contacts file is corrupted - starting with empty contacts")
                return {}
    except FileNotFoundError:
        print("\nNo existing contacts file found - starting fresh")
        return {}
    except Exception as e:
        print(f"\nError loading contacts: {str(e)} - starting with empty contacts")
        return {}


def show_menu(options: Dict[str, Tuple[str, Callable]]) -> None:
    """
    Display the main menu dynamically based on available options
    TEACHING: Dynamic menu generation makes it easy to add/remove options
    without changing the display logic.
    """
    print("\n" + "=" * 30)
    print(" CONTACT MANAGER ".center(30, '='))
    print("=" * 30)
    for key, (text, _) in sorted(options.items()):
        print(f"[{key}] {text}")


def main():
    """
    Main program loop
    TEACHING: The main() function should be clean and easy to read,
    acting as the "table of contents" for your program's functionality.
    """
    contacts = load_contacts()

    menu_options = {
        "1": ("Add Contacts", add_contacts),
        "2": ("Update Contact", update_contact),
        "3": ("Search Contacts", search_contacts),
        "4": ("Save and Exit", save_contacts)
    }

    while True:
        show_menu(menu_options)
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "4":
            if menu_options[choice][1](contacts):
                break
        elif choice in menu_options:
            menu_options[choice][1](contacts)
        else:
            print("\nInvalid choice. Please enter 1-4")

    print("\nThank you for using Contact Manager!")


if __name__ == "__main__":
    """
    TEACHING: This standard Python idiom ensures your code only runs
    when executed directly (not when imported as a module)
    """
    main()