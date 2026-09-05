from django.shortcuts import render

from .models import Ingrediente
from .services import calcular_quantidade_compra


def lista_compras(request):
    ingredientes = Ingrediente.objects.all()

    compras = []

    for ingrediente in ingredientes:
        quantidade = calcular_quantidade_compra(ingrediente)

        if quantidade > 0:
            compras.append({
                "quantidade": quantidade,
                "unidade": ingrediente.unidade,
                "ingrediente": ingrediente.nome,
            })

    return render(
        request,
        "estoque/lista_compras.html",
        {"compras": compras}
    )