from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = "nome"

    def __str__(self):
        return self.nome
