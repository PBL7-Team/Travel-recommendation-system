from django.db import models

from api_user.models.user import User

# Create your models here.
class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chathistories')
    chat_message = models.TextField()
    system_answer = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)  
    is_from_system = models.BooleanField(default=False) # True if the message is from the system
    descriptions = models.TextField(null=True)
    
    class Meta:
        db_table = 'chat_history'
    def __str__(self):
        return f'{self.user.username}: {self.chat_message[:50]}...'