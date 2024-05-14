from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=250, verbose_name='ФИО')
    institution = models.CharField(max_length=250, verbose_name='Наименование учебного заведения')
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(max_length=150, verbose_name='E-mail')

    class Meta():
        verbose_name= 'Участника'
        verbose_name_plural = 'Участники'
    
    def __str__(self):
        return self.name
