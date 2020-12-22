from django.db import IntegrityError
import pytest


@pytest.mark.django_db
class TestUser:
    def test_get_full_name(self, user):
        assert user.get_full_name() == user.full_name

    def test_get_short_name(self, user):
        assert user.get_short_name() == user.username

    def test_unique_username(self, user, user_factory):
        with pytest.raises(IntegrityError, match="UNIQUE"):
            user_factory(username=user.username)

    def test_str(self, user):
        assert str(user) == user.full_name
        user.full_name = ""
        assert str(user) == user.username
