from decimal import Decimal

from django.test import TestCase

from .models import Ingrediente
from .services import calcular_quantidade_compra


class CalculoCompraTest(TestCase):

    def test_compra_diferenca_meta_e_estoque(self):
        ingrediente = Ingrediente(
            nome="Farinha",
            unidade="kg",
            meta=Decimal("10.00"),
            estoque_atual=Decimal("4.00"),
            consumo_mes=Decimal("6.00"),
        )

        resultado = calcular_quantidade_compra(ingrediente)

        self.assertEqual(resultado, Decimal("6.00"))

    def test_compra_meta_completa_se_ingrediente_vencido(self):
        ingrediente = Ingrediente(
            nome="Leite",
            unidade="litros",
            meta=Decimal("20.00"),
            estoque_atual=Decimal("5.00"),
            consumo_mes=Decimal("15.00"),
            vencido=True,
        )

        resultado = calcular_quantidade_compra(ingrediente)

        self.assertEqual(resultado, Decimal("20.00"))

    def test_compra_consumo_com_20_porcento_se_ingrediente_acabou(self):
        ingrediente = Ingrediente(
            nome="Ovos",
            unidade="unidades",
            meta=Decimal("100.00"),
            estoque_atual=Decimal("0.00"),
            consumo_mes=Decimal("100.00"),
            acabou_antes_fim_mes=True,
        )

        resultado = calcular_quantidade_compra(ingrediente)

        self.assertEqual(resultado, Decimal("120.00"))

    def test_nao_compra_quando_estoque_e_igual_a_meta(self):
        ingrediente = Ingrediente(
            nome="Arroz",
            unidade="kg",
            meta=Decimal("10.00"),
            estoque_atual=Decimal("10.00"),
            consumo_mes=Decimal("5.00"),
        )

        resultado = calcular_quantidade_compra(ingrediente)

        self.assertEqual(resultado, Decimal("0.00"))

    def test_nao_compra_quando_estoque_e_maior_que_meta(self):
        ingrediente = Ingrediente(
            nome="Feijão",
            unidade="kg",
            meta=Decimal("10.00"),
            estoque_atual=Decimal("12.00"),
            consumo_mes=Decimal("5.00"),
        )

        resultado = calcular_quantidade_compra(ingrediente)

        self.assertLessEqual(resultado, Decimal("0.00"))