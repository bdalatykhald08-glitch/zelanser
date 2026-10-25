from .models import *
from celery import shared_task
from rest_framework.exceptions import ValidationError
# مهمتين لكل من حقلين كلاس تحويلات

@shared_task
def room_notes(room_id):

    try:
        room = ChatRoom.objects.get(id=room_id)

        if room.freelancer_unread > 0:
            print(f"أشعارات المستقل في غرفة المراسلة : {room.freelancer_unread}")

        elif room.client_unread > 0:
            print(f"أشعارات العميل في غرفة المراسلة: {room.client_unread}")

    except ChatRoom.DoesNotExist:
        print("غرفة مراسلة غير موجودة")

    except Exception as e:
        print(f"حدث خطأ ما : {str(e)}")


@shared_task
def create_transfer(transfer_id, transfer_type, status):

    try:
        transfer = Transfer.objects.get(id=transfer_id)

        if transfer_type in ['deposit_escrow', 'release_to_freelancer'] and status == 'pending':
            print(f"دفع العميل  وحجز المبلغ في المنصة  وتسليم المستقل : {transfer_type}")

        elif transfer_type == 'withdraw' and status == 'completed':
            print(f"سحب الأموال لمستقل : {transfer_type}")

        elif status == 'failed':
            print(f"قد فشلت العملية : {status}")

    except Transfer.DoesNotExist:
        print("عملية تحويل غير موجودة")

    except ValidationError:
        print("لايمكنك أتمام مهام تحويلات بشكل مختلف")


        


