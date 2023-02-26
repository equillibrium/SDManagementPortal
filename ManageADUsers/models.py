from django.db import models


class ADUser(models.Model):
    fullname = models.CharField('ФИО', max_length=50)
    mail = models.CharField('Email', max_length=50)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = "Пользователь AD"
        verbose_name_plural = "Пользователи AD"
