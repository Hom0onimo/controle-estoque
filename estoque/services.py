from decimal import Decimal


MARGEM_SEGURANCA = Decimal("1.20")


def calcular_quantidade_compra(ingrediente):

    if ingrediente.vencido:
        return ingrediente.meta

    if ingrediente.acabou_antes_fim_mes:
        return ingrediente.consumo_mes * MARGEM_SEGURANCA

    return ingrediente.meta - ingrediente.estoque_atual