from datetime import datetime
import os
import pandas as pd

from utils.data_manager import (
    cargar_ventas,
    cargar_clientes,
    cargar_inventario
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors


def generar_pdf_mensual(
    mes,
    anio
):

    # ======================
    # CARPETA INFORMES
    # ======================

    carpeta = "Informes"

    os.makedirs(
        carpeta,
        exist_ok=True
    )

    nombre_archivo = (
        f"D912_Informe_{mes}_{anio}.pdf"
    )

    ruta_pdf = os.path.join(
        carpeta,
        nombre_archivo
    )

    # ======================
    # CARGAR DATOS
    # ======================

    ventas = cargar_ventas()

    clientes = cargar_clientes()

    inventario = cargar_inventario()

    ventas["Total_Facturado"] = pd.to_numeric(
        ventas["Total_Facturado"],
        errors="coerce"
    ).fillna(0)

    ventas["Subtotal_Productos"] = pd.to_numeric(
        ventas["Subtotal_Productos"],
        errors="coerce"
    ).fillna(0)

    ventas["Subtotal_IVA"] = pd.to_numeric(
        ventas["Subtotal_IVA"],
        errors="coerce"
    ).fillna(0)

    ventas["IVA_Envio"] = pd.to_numeric(
        ventas["IVA_Envio"],
        errors="coerce"
    ).fillna(0)

    ventas["Total_Envio"] = pd.to_numeric(
        ventas["Total_Envio"],
        errors="coerce"
    ).fillna(0)

    ventas["Subtotal_Neto"] = pd.to_numeric(
        ventas["Subtotal_Neto"],
        errors="coerce"
    ).fillna(0)

    clientes["Total_Compras"] = pd.to_numeric(
        clientes["Total_Compras"],
        errors="coerce"
    ).fillna(0)

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
    # PDF
    # ======================

    doc = SimpleDocTemplate(
        ruta_pdf
    )

    estilos = getSampleStyleSheet()

    contenido = []

    # ======================
    # PORTADA
    # ======================

    logo_path = "logo_d912.png"

    if os.path.exists(
        logo_path
    ):

        contenido.append(
            Image(
                logo_path,
                width=350,
                height=90
            )
        )

    contenido.append(
        Spacer(
            1,
            30
        )
    )

    contenido.append(
        Paragraph(
            "D912 Perfumes",
            estilos["Title"]
        )
    )

    contenido.append(
        Spacer(
            1,
            10
        )
    )

    contenido.append(
        Paragraph(
            "Informe Comercial Mensual",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            15
        )
    )

    contenido.append(
        Paragraph(
            f"{mes} {anio}",
            estilos["Heading2"]
        )
    )

    contenido.append(
        Spacer(
            1,
            15
        )
    )

    contenido.append(
        Paragraph(
            (
                "Generado el "
                + datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )
            ),
            estilos["Normal"]
        )
    )

    contenido.append(
        PageBreak()
    )

    # ======================
    # RESUMEN EJECUTIVO
    # ======================

    contenido.append(
        Paragraph(
            "Resumen Ejecutivo",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            15
        )
    )

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

    resumen = [
        [
            "Indicador",
            "Valor"
        ],
        [
            "Facturación Total",
            f"${facturacion_total:,.0f}"
        ],
        [
            "Ventas Productos",
            f"${ventas_productos:,.0f}"
        ],
        [
            "Ingresos Envíos",
            f"${ingresos_envio:,.0f}"
        ],
        [
            "IVA Productos",
            f"${iva_productos:,.0f}"
        ],
        [
            "IVA Envíos",
            f"${iva_envios:,.0f}"
        ],
        [
            "IVA Total",
            f"${iva_total:,.0f}"
        ],
        [
            "Clientes Registrados",
            len(clientes)
        ],
        [
            "Pedidos Registrados",
            len(ventas)
        ]
    ]

    tabla_resumen = Table(
        resumen,
        colWidths=[
            250,
            180
        ]
    )

    tabla_resumen.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                )
            ]
        )
    )

    contenido.append(
        tabla_resumen
    )

    contenido.append(
        PageBreak()
    )

    # ======================
    # TOP CLIENTES
    # ======================

    contenido.append(
        Paragraph(
            "Top Clientes",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            10
        )
    )

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
    ).head(10)

    tabla_clientes = [
        [
            "Cliente",
            "Total Compras"
        ]
    ]

    for _, fila in top_clientes.iterrows():

        tabla_clientes.append(
            [
                (
                    f"{fila['Nombre']} "
                    f"{fila['Apellido']}"
                ),
                f"${fila['Total_Compras']:,.0f}"
            ]
        )

    tabla_clientes = Table(
        tabla_clientes,
        colWidths=[
            280,
            150
        ]
    )

    tabla_clientes.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                )
            ]
        )
    )

    contenido.append(
        tabla_clientes
    )

    contenido.append(
        PageBreak()
    )

    # ======================
    # TOP PERFUMES
    # ======================

    contenido.append(
        Paragraph(
            "Top Perfumes",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            10
        )
    )

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

        tabla_perfumes = [
            [
                "Marca",
                "Perfume",
                "Cantidad"
            ]
        ]

        for _, fila in (
            ventas_perfume
            .head(10)
            .iterrows()
        ):

            tabla_perfumes.append(
                [
                    fila["Marca"],
                    fila["Perfume"],
                    fila["Cantidad"]
                ]
            )

        tabla_perfumes = Table(
            tabla_perfumes,
            colWidths=[
                120,
                220,
                80
            ]
        )

        tabla_perfumes.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.black
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    )
                ]
            )
        )

        contenido.append(
            tabla_perfumes
        )

    else:

        contenido.append(
            Paragraph(
                "No existen ventas registradas.",
                estilos["Normal"]
            )
        )

    contenido.append(
        PageBreak()
    )

    # ======================
    # ESTADO INVENTARIO
    # ======================

    contenido.append(
        Paragraph(
            "Estado del Inventario",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            10
        )
    )

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

    tabla_stock = [
        [
            "Marca",
            "Perfume",
            "Stock Actual",
            "Stock Minimo",
            "Estado"
        ]
    ]

    for _, fila in (
        stock_estado
        .sort_values(
            by="Stock_Actual_ml"
        )
        .iterrows()
    ):

        tabla_stock.append(
            [
                fila["Marca"],
                fila["Perfume"],
                fila["Stock_Actual_ml"],
                fila["Stock_Minimo_ml"],
                fila["Estado"]
            ]
        )

    tabla_stock = Table(
        tabla_stock,
        colWidths=[
            100,
            200,
            80,
            80,
            90
        ]
    )

    tabla_stock.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                )
            ]
        )
    )

    contenido.append(
        tabla_stock
    )

    # ======================
    # DETALLE DE VENTAS
    # ======================

    contenido.append(
        PageBreak()
    )

    contenido.append(
        Paragraph(
            "Detalle de Ventas",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            10
        )
    )

    for _, venta in ventas.iterrows():

        cliente_id = venta[
            "ID_Cliente"
        ]

        cliente_info = clientes[
            clientes["ID_Cliente"]
            == cliente_id
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
                "Cliente no encontrado"
            )

        ids = str(
            venta["ID_Producto"]
        ).split("|")

        tamanos = str(
            venta["Tamano_Decant_ml"]
        ).split("|")

        cantidades = str(
            venta["Cantidad"]
        ).split("|")

        precios = str(
            venta["Precio_Total"]
        ).split("|")

        productos_texto = []

        for (
            id_producto,
            tamano,
            cantidad,
            precio
        ) in zip(
            ids,
            tamanos,
            cantidades,
            precios
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
                    "Perfume desconocido"
                )

            productos_texto.append(
                (
                    f"• {nombre_perfume}"
                    f"<br/>"
                    f"{tamano} ml x{cantidad}"
                    f"<br/>"
                    f"${int(float(precio)):,.0f}"
                )
            )

        cliente_columna = Paragraph(
            (
                f"{cliente_nombre}<br/>"
                f"{venta['Fecha']}<br/>"
                f"{venta['Metodo_Pago']}<br/>"
                f"{venta['Estado_Pedido']}"
            ),
            estilos["Normal"]
        )

        productos_columna = Paragraph(
            "<br/><br/>".join(
                productos_texto
            ),
            estilos["Normal"]
        )

        totales_columna = Paragraph(
            (
                f"<b>Productos</b><br/>"
                f"${venta['Subtotal_Productos']:,.0f}"
                f"<br/><br/>"
                f"<b>Envío</b><br/>"
                f"${venta['Total_Envio']:,.0f}"
                f"<br/><br/>"
                f"<b>Facturado</b><br/>"
                f"${venta['Total_Facturado']:,.0f}"
            ),
            estilos["Normal"]
        )

        tabla_venta = [
            [
                "Cliente",
                "Productos",
                "Totales"
            ],
            [
                cliente_columna,
                productos_columna,
                totales_columna
            ]
        ]

        tabla_venta = Table(
            tabla_venta,
            colWidths=[
                140,
                250,
                120
            ]
        )

        tabla_venta.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        1,
                        colors.black
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),
                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "TOP"
                    )
                ]
            )
        )

        contenido.append(
            Paragraph(
                (
                    f"Venta "
                    f"#{venta['ID_Venta']}"
                ),
                estilos["Heading3"]
            )
        )

        contenido.append(
            tabla_venta
        )

        contenido.append(
            Spacer(
                1,
                15
            )
        )

    # ======================
    # RESUMEN TRIBUTARIO
    # ======================

    contenido.append(
        PageBreak()
    )

    contenido.append(
        Paragraph(
            "Resumen Tributario",
            estilos["Heading1"]
        )
    )

    contenido.append(
        Spacer(
            1,
            15
        )
    )

    subtotal_neto = ventas[
        "Subtotal_Neto"
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

    facturacion_total = ventas[
        "Total_Facturado"
    ].sum()

    tabla_tributaria = [
        [
            "Concepto",
            "Monto"
        ],
        [
            "Subtotal Neto",
            f"${subtotal_neto:,.0f}"
        ],
        [
            "IVA Productos",
            f"${iva_productos:,.0f}"
        ],
        [
            "IVA Envíos",
            f"${iva_envios:,.0f}"
        ],
        [
            "IVA Total",
            f"${iva_total:,.0f}"
        ],
        [
            "Facturación Total",
            f"${facturacion_total:,.0f}"
        ]
    ]

    tabla_tributaria = Table(
        tabla_tributaria,
        colWidths=[
            250,
            180
        ]
    )

    tabla_tributaria.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                )
            ]
        )
    )

    contenido.append(
        tabla_tributaria
    )

    # ======================
    # CONSTRUIR PDF
    # ======================

    doc.build(
        contenido
    )

    return ruta_pdf