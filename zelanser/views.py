from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .BusinessLogic.services import ChatRoomServices, WalletTransferServices
from .permission import IsFreelancer, IsClient, IsAdminOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    
class ProfileView(generics.RetrieveUpdateAPIView):

    queryset = Profile.objects.select_related('user')
    serializer_class = ProfileSerializer

    def get_object(self):

        profile = Profile.objects.get_or_create(user=self.request.user)
        return profile

class FreelancerViewset(viewsets.ModelViewSet):

    queryset = Freelancer.objects.prefetch_related('freelancer_chats', 'wallet_freelancers')
    serializer_class = FreelancerSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['field', 'specialist', 'level']

    permission_classes = [IsFreelancer | IsAdminOnly]
    
    def perform_create(self, serializer):
        user_profile, created = Profile.objects.update_or_create(user=self.request.user)
        serializer.save(freelancer=user_profile)

    @method_decorator(cache_page(60 * 30))
    def dispatch(self,  *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ClientViewset(viewsets.ModelViewSet):

    queryset = Client.objects.prefetch_related('client_chats', 'wallet_clients')
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['company_name']

    
    permission_classes = [IsClient | IsAdminOnly]

    def perform_create(self, serializer):
        user_profile, created = Profile.objects.update_or_create(user=self.request.user)
        serializer.save(client=user_profile)

    
    @method_decorator(cache_page(60 * 30))
    def dispatch(self,  *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SpecialProjectViewset(viewsets.ModelViewSet):

    queryset = SpecialProject.objects.select_related('project_client')
    serializer_class = SpecialProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'work', 'time_work']

    
    
    @method_decorator(cache_page(60 * 20))
    def dispatch(self,  *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    
class ChatRoomViewset(viewsets.ModelViewSet):

    queryset = ChatRoom.objects.prefetch_related('chat_agrees')
    serializer_class = ChatRoomSerializer

    def perform_create(self, serializer):
    
        ChatRoomServices(serializer.validated_data)

    
    @method_decorator(cache_page(60 * 20))
    def dispatch(self,  *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class MessageViewset(viewsets.ModelViewSet):

    queryset = Message.objects.select_related('room')
    serializer_class = MessageSerializer


class AgreementViewset(viewsets.ModelViewSet):

    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class WalletViewset(viewsets.ModelViewSet):

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def perform_create(self, serializer):
        
        WalletTransferServices(validated_data=serializer.validated_data, 
                               user=self.request.user)

    
    @method_decorator(cache_page(60 * 20))
    def dispatch(self,  *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TransferViewset(viewsets.ModelViewSet):

    queryset = Transfer.objects.select_related('wallet')
    serializer_class = TransferSerializer

    def perform_create(self, serializer):
        transfer = serializer.save()
    
      








