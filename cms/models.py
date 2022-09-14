from django.db import models

# Create your models here.
class CmsSlaider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Описание')
    cms_css = models.CharField(max_length=200, null=True, default='', verbose_name='CSS класс')

    def __str__(self):
        return self.cms_text

    class Meta():
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'