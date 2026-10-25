from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
      
        return user


class FreelancerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Freelancer
        fields = '__all__'
        read_only_fields = ['freelancer', 'created_at', 'updated_at']


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['client', 'created_at', 'updated_at']


class ProfileSerializer(serializers.ModelSerializer):

    freelancer = FreelancerSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class SpecialProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialProject
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['created_at']


class AgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agreement
        fields = '__all__'
        read_only_fields = ['accept_freelancer', ' accept_client', 'admin_check', 'created_at', 'updated_at']


class ChatRoomSerializer(serializers.ModelSerializer):

    message = MessageSerializer(many=True, read_only=True)
    agreement = AgreementSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = '__all__'
        read_only_fields = ['created_at']


class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = '__all__'
        read_only_fields = ['is_approved', 'created_at']


class WalletSerializer(serializers.ModelSerializer):

    transfer = TransferSerializer(many=True, read_only=True)
    
    class Meta:
        model = Wallet
        fields = '__all__'
        read_only_fields = ['updated_at']




