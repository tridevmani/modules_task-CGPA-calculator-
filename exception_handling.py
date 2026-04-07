
class WeakPasswordError(Exception):
    pass

class DataFormatError(Exception):
    pass


def validate_password(password):
    if len(password) < 6:
        raise WeakPasswordError("Password too short!")
    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain a number!")


def read_and_process_file():
    try:
        filename = input("Enter file name: ")

        with open(filename, "r") as f:
            data = f.readlines()

        numbers = []

        for line in data:
            line = line.strip()
            if not line.isdigit():
                raise DataFormatError(f"Invalid data found: {line}")
            numbers.append(int(line))

        print("\nProcessed Data:")
        print("Numbers:", numbers)
        print("Total:", sum(numbers))

    except FileNotFoundError:
        print("Error: File does not exist!")

    except DataFormatError as e:
        print("Data Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    else:
        print("File processed successfully!")

    finally:
        print("File operation finished.\n")


def user_login():
    try:
        password = input("Create password: ")
        validate_password(password)

    except WeakPasswordError as e:
        print("Password Error:", e)

    else:
        print("Password set successfully!")

    finally:
        print("Login module executed.\n")


def main():
    print("=== Secure System ===")
    user_login()
    read_and_process_file()


if __name__ == "__main__":
    main()