from django.db import models

class Client(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class Phone(models.Model):
    TYPES = (
        ('home', 'Residencial'),
        ('work', 'Trabalho'),
        ('cellphone', 'Celular'),
    )

    client      = models.ForeignKey(Client)
    type        = models.CharField(max_length=12, choices=TYPES)
    number      = models.CharField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)