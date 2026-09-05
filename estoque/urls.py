from django.urls import path

from .views import lista_compras


urlpatterns = [
    path("", lista_compras, name="lista_compras"),
]