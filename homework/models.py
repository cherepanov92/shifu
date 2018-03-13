from django.db import models

class Page(models.Model):
    id = models.AutoField('id', primary_key=True)
    title = models.CharField('Значение', max_length=20)

    def __str__(self):
        return (self.title)

class Cities(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('Название', max_length=40)

    def __str__(self):
        return (self.name)