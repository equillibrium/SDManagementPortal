from django.db import models


class NewADUser(models.Model):
    f = models.CharField('Фамилия', max_length=50)
    i = models.CharField('Имя', max_length=50)
    o = models.CharField('Отчество', max_length=50)

    def __str__(self):
        return f'{self.f} {self.i} {self.o}'

    class Meta:
        verbose_name = "Новый пользователь AD"
        verbose_name_plural = "Новые пользователи AD"
