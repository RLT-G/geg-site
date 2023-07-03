from django.db import models


class ModelNews(models.Model):

    title = models.CharField('Название новости', max_length=50, null=False, blank=False)
    full_text = models.TextField('Содержание новости', max_length=2000, null=False, blank=False)
    author = models.CharField('Автор новости', max_length=50, null=False, blank=True, default='unknown')
    image = models.ImageField('Иконка новости (4х4)', null=True, blank=True)
    info = models.TextField('Дополнительная информация', max_length=2000, null=True, blank=True, default=None)

    time = models.DateTimeField('Дата добавление новости', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости сайта'
        verbose_name_plural = 'Новости сайта'
