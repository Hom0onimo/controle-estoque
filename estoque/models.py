from django.db import models



class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    unidade = models.CharField(max_length=30)

    meta = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque_atual = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    consumo_mes = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    vencido = models.BooleanField(default=False)

    acabou_antes_fim_mes = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
