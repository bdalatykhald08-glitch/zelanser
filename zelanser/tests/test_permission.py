from zelanser.permission import IsFreelancer, IsClient, IsAdminOnly
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

@pytest.mark.django_db
def test_freelancer_permission():

    user = User.objects.create_user(username='free_user', password='123')

    setattr(user, 'role','freelancer')

    factory = APIRequestFactory()
    request = factory.get('/')
    request.user = user

    permission = IsFreelancer()
    assert permission.has_permission(request, None) is True


@pytest.mark.django_db
def test_client_permission():

    user = User.objects.create_user(username='free_user2', password='123')

    setattr(user, 'role', 'freelancer')

    factory = APIRequestFactory()
    request = factory.get('/')
    request.user = user

    permission = IsClient()
    assert permission.has_permission(request, None) is False




