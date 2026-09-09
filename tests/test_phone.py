from services.phone_service import (
    PhoneService
)


def test_get_all_phones():

    phones = (
        PhoneService.get_all_phones()
    )

    assert isinstance(
        phones,
        list
    )