from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField('Имя', max_length=25)
    email = models.EmailField('Почта')
    question = models.TextField('Текст')
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'