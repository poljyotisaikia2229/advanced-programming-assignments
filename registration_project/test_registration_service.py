import pytest

from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


@pytest.fixture
def registration_service():
    """
    Creates RegistrationService instance before each test.
    """
    return RegistrationService()


def test_successful_registration(registration_service):
    result = registration_service.register_user(
        "john.doe@example.com",
        25
    )

    assert result is True


def test_invalid_email(registration_service):
    with pytest.raises(InvalidEmailError):
        registration_service.register_user(
            "invalid-email",
            25
        )


def test_empty_email(registration_service):
    with pytest.raises(InvalidEmailError):
        registration_service.register_user(
            "",
            25
        )


def test_none_email(registration_service):
    with pytest.raises(InvalidEmailError):
        registration_service.register_user(
            None,
            25
        )


def test_underage_user(registration_service):
    with pytest.raises(UnderageError):
        registration_service.register_user(
            "young@example.com",
            16
        )


def test_boundary_age_18(registration_service):
    result = registration_service.register_user(
        "adult@example.com",
        18
    )

    assert result is True


def test_inactive_service_assertion():
    service = RegistrationService(active=False)

    with pytest.raises(AssertionError):
        service.register_user(
            "valid@example.com",
            30
        )