from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

r = DefaultRouter()


r.register(r'freelancers', FreelancerViewset, basename='freelancer')
r.register(r'clients', ClientViewset, basename='client')
r.register(r'projects', SpecialProjectViewset, basename='project')
r.register(r'chatrooms', ChatRoomViewset, basename='chatroom')
r.register(r'wallets', WalletViewset, basename='wallet')

urlpatterns = [
    path('', include(r.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile')
]





