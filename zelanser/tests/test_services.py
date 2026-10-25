from zelanser.models import *
import pytest


@pytest.mark.django_db
def test_chatroom():

    chatroom = ChatRoom.objects.create()
    
    assert chatroom is not None
  
    assert chatroom.id is not None


@pytest.mark.django_db
def test_wallet():
  
    wallet = Wallet.objects.create(currency='USDT')

    assert wallet.currency == 'USDT' 
   
    assert wallet is not None

  





