from django.db import models

# Create your models here.

class Telegram(models.Model):
    tele_token = models.CharField(max_length=200, verbose_name='Токен')
    tele_chat_id = models.CharField(max_length=200, verbose_name='Чат ID')
    tele_text = models.TextField(verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Извещения'
        verbose_name_plural = 'Извещении'

    def __str__(self):
        return self.tele_text
