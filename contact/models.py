from ckeditor.fields import RichTextField
from django.db import models

class ContactModel(models.Model):
    """ Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class About(models.Model):
    """ Класс модели страницы о нас """
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = 'Страница О нас'
        verbose_name_plural = 'Страницы О нас'


class Social(models.Model):
    """ Класс модели соцю сетей страницы о нас """
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()

