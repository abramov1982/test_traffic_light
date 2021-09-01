from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Unit(MPTTModel):
    name = models.CharField(max_length=100, blank=False, verbose_name='Подразделение')
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children',
                            verbose_name='Входит в подразделение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Employee(models.Model):
    first_name = models.CharField(max_length=50, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=False, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, blank=False, verbose_name='Отчество')
    position = models.CharField(max_length=100, blank=False, verbose_name='Должность')
    unit = models.ForeignKey(Unit, null=True, on_delete=models.DO_NOTHING, verbose_name='Подразделение')
    salary = models.IntegerField(null=False, blank=False, verbose_name='Оклад')
    employment_date = models.DateField(blank=False, verbose_name='Дата приёма на работу')
    full_name = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def save(self, *args, **kwargs):
        self.full_name = f'{self.last_name} {self.first_name} {self.middle_name}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
