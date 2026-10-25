from zelanser.models import *
from django.db import transaction
from rest_framework.exceptions import ValidationError
from zelanser.tasks import create_transfer, room_notes
# - شرط class chat 
# انه لازم أذا أنت عميل تضع خيار ربط تبعك اما اذا مستقل ربط تبعك

class ChatRoomServices:
    def link_client_or_freelancer(room_id):
        
        room_notes.delay(room_id)

        if 'client' !=  'client_chat':
            raise ValidationError("يجب عليك كعميل بأن تختار ربط بعميل لغرفة المراسلة")

        if 'client' == 'project':
            raise ValidationError("اذا عندك مشروع كعميل فقم بربطه")

        elif 'freelancer' != 'freelancer_chat':
            raise ValidationError("يجب عليك كمستقل بأن تربط بي خيار مستقل لمراسلة")

        else:
            raise ValidationError("لايمكنك ربط والدخول لغرفة المراسلة ")

    
class WalletTransferServices:

    @transaction.atomic
    @staticmethod

    def client_payment(wallet_id, txid, currency, amount):

        wallet = Wallet.objects.select_for_update().get(id=wallet_id)
        

        if currency != 'USDT':
            raise ValidationError("'USDT' يجب عليك تحويل بعملة واحدة والأكثر أنتشارا هي")

       
        if not txid:
            raise ValidationError("لازم تضع رقم العملية من بينانس كعميل لي المستقل")
    
        transfer = Transfer.objects.get_or_create(
            wallet=wallet,
            TxID=txid,
            transfer_type='deposit_escrow',
            status='pending',
        )

        create_transfer.delay(transfer.id, transfer.transfer_type, transfer.status)

        wallet.pending_balance += amount
        wallet.save()

        return transfer




