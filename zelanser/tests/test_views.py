import pytest
from rest_framework import status
from django.urls import reverse

pytestmark = pytest.mark.django_db

endpoints = [
    'freelancer-list',
    'client-list',
    'project-list',
    'chatroom-list',
    'wallet-list'
] 

        
@pytest.mark.parametrize("endpoint_name", endpoints)
def test_get_allowed(api_client, endpoint_name):

    url = reverse(endpoint_name)
    response = api_client.get(url)
    
    assert response.status_code in [
        status.HTTP_200_OK,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_403_FORBIDDEN
    ]
     


@pytest.mark.parametrize("endpoint_name", endpoints)
def test_post_auth_for_guest(api_client, endpoint_name):

    url = reverse(endpoint_name)
    data = {}
    response = api_client.post(url, data=data)
    
    assert response.status_code in [
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_403_FORBIDDEN
    ]
     






