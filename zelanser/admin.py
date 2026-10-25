from django.contrib import admin
from .models import *
# Register your models here.



class MessageInline(admin.TabularInline):

    model = Message
    extra = 1

class AgreementInline(admin.StackedInline):

    model = Agreement
    extra = 0

class TransferInline(admin.TabularInline):

    model = Transfer
    extra = 0

class ChatRoomAdmin(admin.ModelAdmin):
    inlines = [MessageInline, AgreementInline]
    list_display = ['id', 'created_at']

class WalletAdmin(admin.ModelAdmin):
    inlines = [TransferInline]
    list_display = ['id', 'updated_at']

    
admin.site.register(Profile)
admin.site.register(Freelancer)
admin.site.register(Client)
admin.site.register(SpecialProject)
admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Wallet, WalletAdmin)






