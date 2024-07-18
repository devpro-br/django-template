import pytest
from django.contrib.auth import get_user_model
from django_min_custom_user.manager import MinUserManager


def test_user_has_customized_manager_instance():
    User = get_user_model()
    assert isinstance(User.objects, MinUserManager)


@pytest.mark.django_db
def test_user_creation_with_lower_case_email():
    User = get_user_model()
    user = User.objects.create_user(email='RenZo@dev,pro.br')
    assert user.email == 'renzo@dev,pro.br'
