import math


def precio_venta(valor):

    valor = str(valor).strip()

    valor = float(valor)

    return (
        math.ceil(
            (valor * 1.19) / 100
        ) * 100
    )


def iva_cobrado(valor):

    precio_final = precio_venta(
        valor
    )

    return (
        precio_final
        - float(valor)
    )