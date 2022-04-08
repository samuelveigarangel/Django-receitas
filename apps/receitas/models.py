from django.db import models
from datetime import datetime
from django.db.models import Transform
from django.contrib.auth.models import User

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)


    class Meta:
        ordering = ("id",)
        verbose_name = "nomes de receita"

    def __str__(self):
        return self.nome_receita


class Unaccent(Transform):
    bilateral = True
    lookup_name = 'unaccent'

    def as_postgresql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return "UNACCENT(%s)" % lhs, params

models.CharField.register_lookup(Unaccent)

