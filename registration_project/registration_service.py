import re


class InvalidEmailError(ValueError):
    """Raised when an email address is invalid."""

    def __init__(self, message: str):
        super().__init__(message)


class UnderageError(ValueError):
    """Raised when user is under 18."""

    def __init__(self, message: str):
        super().__init__(message)


class RegistrationService:
    """
    Handles user registration validation.
    """

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(self, active: bool = True):
        self.active = active

    def register_user(self, email: str, age: int) -> bool:
        """
        Validates registration details.

        Args:
            email (str): User email.
            age (int): User age.

        Returns:
            bool: True if validation succeeds.
        """

        # Internal invariant check
        assert self.active, (
            "RegistrationService is inactive."
        )

        # Email cannot be null or empty
        if email is None or not email.strip():
            raise InvalidEmailError(
                "Email cannot be null or empty."
            )

        # Regex email validation
        if not self.EMAIL_PATTERN.match(email):
            raise InvalidEmailError(
                f"Invalid email format: {email}"
            )

        # Age validation
        if age < 18:
            raise UnderageError(
                f"User age {age} is below minimum age requirement of 18."
            )

        return True