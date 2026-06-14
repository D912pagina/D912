from datetime import datetime
import os
import pandas as pd

from utils.data_manager import (
    cargar_ventas,
    cargar_clientes,
    cargar_inventario
)


def generar_excel_mensual(
    mes,
    anio
):

    ventas = cargar_ventas()
    clientes = cargar_clientes()
    inventario = cargar_inventario()

    # ======================
    # FILTRO FECHA
    # ======================

    ventas["Fecha"] = pd.to_datetime(
        ventas["Fecha"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    meses_numero = {
        "Enero": 1,
        "Febrero": 2,
        "Marzo": 3,
        "Abril": 4,
        "Mayo": 5,
        "Junio": 6,
        "Julio": 7,
        "Agosto": 8,
        "Septiembre": 9,
        "Octubre": 10,
        "Noviembre": 11,
        "Diciembre": 12
    }

    mes_numero = meses_numero[
        mes
    ]

    ventas = ventas[
        (
            ventas["Fecha"]
            .dt.month
            == mes_numero
        )
        &
        (
            ventas["Fecha"]
            .dt.year
            == anio
        )
    ]

    # ======================
    # CARPETA
    # ======================

    carpeta = "Informes"

    os.makedirs(
        carpeta,
        exist_ok=True
    )

    ruta_excel = os.path.join(
        carpeta,
        f"D912_Informe_{mes}_{anio}.xlsx"
    )

    # ======================
    # RESUMEN EJECUTIVO
    # ======================

    facturacion_total = ventas[
        "Total_Facturado"
    ].sum()

    ventas_productos = ventas[
        "Subtotal_Productos"
    ].sum()

    ingresos_envio = ventas[
        "Total_Envio"
    ].sum()

    iva_productos = ventas[
        "Subtotal_IVA"
    ].sum()

    iva_envios = ventas[
        "IVA_Envio"
    ].sum()

    iva_total = (
        iva_productos
        + iva_envios
    )

    resumen = pd.DataFrame(
        {
            "Concepto": [
                "Facturación Total",
                "Ventas Productos",
                "Ingresos Envíos",
                "IVA Productos",
                "IVA Envíos",
                "IVA Total",
                "Clientes Registrados",
                "Pedidos Registrados"
            ],
            "Valor": [
                facturacion_total,
                ventas_productos,
                ingresos_envio,
                iva_productos,
                iva_envios,
                iva_total,
                len(clientes),
                len(ventas)
            ]
        }
    )

    # ======================
    # TOP CLIENTES
    # ======================

    top_clientes = clientes.copy()

    top_clientes = top_clientes[
        top_clientes["Nombre"]
        .notna()
    ]

    top_clientes = top_clientes[
        top_clientes["Total_Compras"]
        > 0
    ]

    top_clientes = top_clientes.sort_values(
        by="Total_Compras",
        ascending=False
    )

    # ======================
    # TOP PERFUMES
    # ======================

    ventas_perfume = []

    for _, venta in ventas.iterrows():

        ids = str(
            venta["ID_Producto"]
        ).split("|")

        cantidades = str(
            venta["Cantidad"]
        ).split("|")

        for id_producto, cantidad in zip(
            ids,
            cantidades
        ):

            ventas_perfume.append(
                {
                    "ID_Producto": int(
                        id_producto
                    ),
                    "Cantidad": int(
                        cantidad
                    )
                }
            )

    if len(
        ventas_perfume
    ) > 0:

        ventas_perfume = pd.DataFrame(
            ventas_perfume
        )

        ventas_perfume = (
            ventas_perfume
            .groupby(
                "ID_Producto"
            )["Cantidad"]
            .sum()
            .reset_index()
        )

        ventas_perfume = ventas_perfume.merge(
            inventario[
                [
                    "ID_Producto",
                    "Marca",
                    "Perfume"
                ]
            ],
            on="ID_Producto",
            how="left"
        )

        ventas_perfume = ventas_perfume.sort_values(
            by="Cantidad",
            ascending=False
        )

    else:

        ventas_perfume = pd.DataFrame()

    # ======================
    # ESTADO INVENTARIO
    # ======================

    def estado_stock(
        fila
    ):

        if (
            fila[
                "Stock_Actual_ml"
            ]
            <=
            fila[
                "Stock_Minimo_ml"
            ]
        ):

            return "🔴 Crítico"

        elif (
            fila[
                "Stock_Actual_ml"
            ]
            <=
            fila[
                "Stock_Minimo_ml"
            ]
            * 2
        ):

            return "🟡 Bajo"

        else:

            return "🟢 Normal"

    stock_estado = inventario.copy()

    stock_estado[
        "Estado"
    ] = stock_estado.apply(
        estado_stock,
        axis=1
    )

    # ======================
    # DETALLE VENTAS
    # ======================

    detalle_ventas = []

    for _, venta in ventas.iterrows():

        cliente_info = clientes[
            clientes["ID_Cliente"]
            == venta["ID_Cliente"]
        ]

        if len(
            cliente_info
        ) > 0:

            cliente_nombre = (
                str(
                    cliente_info.iloc[0][
                        "Nombre"
                    ]
                )
                + " "
                + str(
                    cliente_info.iloc[0][
                        "Apellido"
                    ]
                )
            )

        else:

            cliente_nombre = (
                "No encontrado"
            )

        productos = []

        ids = str(
            venta["ID_Producto"]
        ).split("|")

        tamanos = str(
            venta["Tamano_Decant_ml"]
        ).split("|")

        cantidades = str(
            venta["Cantidad"]
        ).split("|")

        for (
            id_producto,
            tamano,
            cantidad
        ) in zip(
            ids,
            tamanos,
            cantidades
        ):

            perfume = inventario[
                inventario[
                    "ID_Producto"
                ]
                == int(
                    id_producto
                )
            ]

            if len(
                perfume
            ) > 0:

                nombre_perfume = (
                    perfume.iloc[0][
                        "Perfume"
                    ]
                )

            else:

                nombre_perfume = (
                    "Desconocido"
                )

            productos.append(
                f"{nombre_perfume} {tamano}ml x{cantidad}"
            )

        detalle_ventas.append(
            {
                "ID_Venta":
                venta["ID_Venta"],

                "Fecha":
                venta["Fecha"],

                "Cliente":
                cliente_nombre,

                "Productos":
                " | ".join(
                    productos
                ),

                "Método Pago":
                venta["Metodo_Pago"],

                "Estado":
                venta["Estado_Pedido"],

                "Subtotal Productos":
                venta["Subtotal_Productos"],

                "Total Envío":
                venta["Total_Envio"],

                "Total Facturado":
                venta["Total_Facturado"]
            }
        )

    detalle_ventas = pd.DataFrame(
        detalle_ventas
    )

    # ======================
    # EXPORTAR
    # ======================

    with pd.ExcelWriter(
        ruta_excel,
        engine="openpyxl"
    ) as writer:

        resumen.to_excel(
            writer,
            sheet_name="Resumen Ejecutivo",
            index=False
        )

        top_clientes.to_excel(
            writer,
            sheet_name="Top Clientes",
            index=False
        )

        ventas_perfume.to_excel(
            writer,
            sheet_name="Top Perfumes",
            index=False
        )

        detalle_ventas.to_excel(
            writer,
            sheet_name="Ventas",
            index=False
        )

        stock_estado[
            [
                "Marca",
                "Perfume",
                "Stock_Actual_ml",
                "Stock_Minimo_ml",
                "Estado"
            ]
        ].to_excel(
            writer,
            sheet_name="Stock",
            index=False
        )

    return ruta_excel