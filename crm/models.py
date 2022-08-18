from django.db import models


# Create your models here.
class Order(models.Model):
    order_dt = models.DateField(auto_now=True, verbose_name='Дата')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.order_name
