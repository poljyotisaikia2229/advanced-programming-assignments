from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


def main():
    """
    Main function for user onboarding input.
    """

    print("=== User Registration System ===")

    service = RegistrationService()

    try:
        # User enters email
        email = input("Enter your email: ")

        # User enters age
        age = int(input("Enter your age: "))

        # Validate registration
        result = service.register_user(email, age)

        if result:
            print("\nRegistration successful!")
            print(f"Welcome, {email}")

    except InvalidEmailError as error:
        print(f"\nEmail Validation Error: {error}")

    except UnderageError as error:
        print(f"\nAge Validation Error: {error}")

    except ValueError:
        print("\nInvalid input. Age must be a number.")

    except AssertionError as error:
        print(f"\nSystem Assertion Error: {error}")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()