from django.db import models
from .BaseModels.models import TimeStamp, AuditModel
from django.contrib.auth.models import User

# Create your models here.

class Profile(TimeStamp):

    USER_TYPE = [('Client', 'عميل'), ('Freelance', 'مستقل')]


    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='users')
    user_type = models.CharField(max_length=30, choices=USER_TYPE)
    image = models.ImageField(upload_to='image/')


    def __str__(self):
        return str(self.user.username) if self.user else "No User"

    class Meta:
        ordering = ['-created_at']


class Freelancer(TimeStamp, AuditModel):
      
    FIELDS = [
            ('Web Dev', 'تطوير الموقع'), ('Mobile App', 'تطوير التطبيق'), ('UI/UX Design', 'تصميم واجهات وتجربة المستخدم'), ('Automation', 'أتمتة المهام'),
            ('ERP Systems', 'أدارة الأنظمة المحاسبية'), ('Cloud', 'السيرفرات السحابية'), ('Editing & Motion', 'مونتاج وتحرير الفيديو'), ('Graphic Design', 'تصميم الجرافيك'),
            ('Copywriting', 'كتابة التسويقية'), ('Seo', 'تحسين محركات البحث'), ('Paid Ads', 'أدارة الحملات الأعلانية'), ('Social Media Mangement', 'أدارة حسابات سوشيال ميديا'),
            ('Store Mangement', 'أدارة المتاجر'), ('Translation', 'الترجمة المتخصصة'), ('Customer Support', 'الدعم الفني'), ('Research', 'البحث'),
            ('Accounting', 'محاسبة'), ('Business Plans', 'خطط العمل'), ('Data Analysis', 'تحليل البيانات'), ('Cybersecurity', 'الأمن السيبراني')
        ]
    
    LEVEL = [('junior', 'مبتدئ'), ('senior', 'محترف'), ('expert', 'خبير')]

    freelancer = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='freelancers')
    field = models.CharField(max_length=50, choices=FIELDS, help_text='المجال')
    specialist = models.CharField(max_length=50, help_text='تخصص')
    link_portfolio = models.URLField(help_text='رابط معرض أعمال')
    level = models.CharField(max_length=30, choices=LEVEL)
    binance_address = models.CharField(max_length=250, help_text='عنوان محفظة بينانس الخاصة بك بي عملة USDT')

    
    def __str__(self):
        return str(self.freelancer.user.username) if self.freelancer and self.freelancer.user else "Freelancer"

    class Meta:
        ordering = ['-created_at']


class Client(TimeStamp, AuditModel):

    client = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='clients')
    company_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.client.user.username) if self.client and self.client.user else "Client"

    class Meta:
        ordering = ['-created_at']


class SpecialProject(TimeStamp):

    WORK = [
            ('Service', 'خدمة'), ('Training', 'تدريب والاستشارات'), ('Contract', 'عقد عمل'),
            ('PartTime', 'عمل جزئي'), ('FullTime', 'عمل كامل')
            ]


    TIME_WORK = [
        ('week', 'أسبوع'), ('two weeks', 'أسبوعين'), ('month', 'شهر'),
        ('two months', 'شهرين'), ('sex months', 'ستة اشهر'), ('specify by deal', 'تحديد المدة بالأتفاق')
    ]

    
    project_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='project_clients')
    title = models.CharField(max_length=100, help_text='عنوان المشروع')
    bio_project = models.TextField(max_length=350, help_text='وصف المشروع')
    work = models.CharField(max_length=30, choices=WORK, help_text='شكل العمل')
    time_work = models.CharField(max_length=50, choices=TIME_WORK, help_text='تحديد عدد الايام أو الأسابيع أو الشهور لي أكمال المشروع')
    budget = models.DecimalField(max_digits=15, decimal_places=5)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ChatRoom(TimeStamp):

    project = models.ForeignKey(SpecialProject, on_delete=models.CASCADE, null=True, blank=True, related_name='projects')
    freelancer_chat = models.ForeignKey(Freelancer, on_delete=models.CASCADE,  null=True, blank=True, related_name='freelancer_chats')
    client_chat = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, related_name='client_chats')
    freelancer_unread = models.PositiveIntegerField(default=0)
    client_unread = models.PositiveIntegerField(default=0)
    

    class Meta:
        ordering = ['-created_at']


class Message(TimeStamp):
    
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='rooms')
    text = models.TextField(max_length=500)


    def __str__(self):
        return f"{self.room}"
    
    class Meta:
        ordering = ['-created_at']
    

class Agreement(TimeStamp, AuditModel):

    chat_agree  = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='chat_agrees')
    clauses_client = models.TextField(max_length=300, help_text='بنود العميل')
    accept_freelancer = models.BooleanField(default=False)
    clauses_freelancer = models.TextField(max_length=300, help_text='بنود المستقل')
    accept_client = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.chat_agree}"

    class Meta:
        ordering = ['-created_at']
    
    
class Wallet(models.Model):

    wallet_freelancer = models.OneToOneField(Freelancer, on_delete=models.CASCADE,  null=True, blank=True, related_name='wallet_freelancers')
    wallet_client = models.OneToOneField(Client, on_delete=models.CASCADE,  null=True, blank=True, related_name='wallet_clients')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    pending_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=50, default='USDT')
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.wallet_freelancer}" + f"{self.wallet_client}"

    class Meta:
        ordering = ['-id']
    
    
class Transfer(models.Model):
    

    TRANSFER_TYPE = [
                    ('deposit_escrow', 'دفع العميل وتم حجز المبلغ'), 
                    ('release_to_freelancer', 'أستلام المستقل المال'),
                    ('withdraw', 'سحب الأرباح')
                    ]

                
    STATUS = [
            ('pending', 'قيد الأنتظار'), 
            ('completed', 'مكتملة'), 
            ('failed', 'فشل')
            ]
    
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallets')
    status = models.CharField(max_length=30, choices=STATUS)
    transfer_type = models.CharField(max_length=30, choices=TRANSFER_TYPE)
    TxID = models.CharField(max_length=100, null=True, blank=True, unique=True, help_text='أدخال رقم عملية من بينانس')
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.transfer_type}"

    class Meta:
        ordering = ['-created_at']


