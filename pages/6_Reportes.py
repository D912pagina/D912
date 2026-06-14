import streamlit as st
import pandas as pd

from utils.data_manager import (
    cargar_ventas,
    cargar_clientes,
    cargar_inventario
)

st.title("📈 Reportes")

ventas = cargar_ventas()
clientes = cargar_clientes()
inventario = cargar_inventario()

ventas["Subtotal_Productos"] = pd.to_numeric(
    ventas["Subtotal_Productos"],
    errors="coerce"
).fillna(0)

ventas["Subtotal_IVA"] = pd.to_numeric(
    ventas["Subtotal_IVA"],
    errors="coerce"
).fillna(0)

ventas["Total_Envio"] = pd.to_numeric(
    ventas["Total_Envio"],
    errors="coerce"
).fillna(0)

ventas["IVA_Envio"] = pd.to_numeric(
    ventas["IVA_Envio"],
    errors="coerce"
).fillna(0)

ventas["Total_Facturado"] = pd.to_numeric(
    ventas["Total_Facturado"],
    errors="coerce"
).fillna(0)

# ======================
# RESUMEN FINANCIERO
# ======================

ventas_productos = ventas[
    "Subtotal_Productos"
].sum()

iva_productos = ventas[
    "Subtotal_IVA"
].sum()

ingresos_envio = ventas[
    "Total_Envio"
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

cantidad_pedidos = len(
    ventas
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💵 Facturación Total",
        f"${facturacion_total:,.0f}"
    )

with col2:
    st.metric(
        "💰 Ventas Productos",
        f"${ventas_productos:,.0f}"
    )

with col3:
    st.metric(
        "🚚 Ingresos Envíos",
        f"${ingresos_envio:,.0f}"
    )

with col4:
    st.metric(
        "🛒 Pedidos",
        cantidad_pedidos
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🧾 IVA Productos",
        f"${iva_productos:,.0f}"
    )

with col2:
    st.metric(
        "📦 IVA Envíos",
        f"${iva_envios:,.0f}"
    )

with col3:
    st.metric(
        "🧾 IVA Total",
        f"${iva_total:,.0f}"
    )

st.divider()

# ======================
# TOP CLIENTES
# ======================

st.subheader(
    "👥 Top Clientes"
)

clientes["Total_Compras"] = pd.to_numeric(
    clientes["Total_Compras"],
    errors="coerce"
).fillna(0)

top_clientes = clientes.sort_values(
    by="Total_Compras",
    ascending=False
)

st.dataframe(
    top_clientes[
        [
            "Nombre",
            "Apellido",
            "Ciudad",
            "Total_Compras"
        ]
    ],
    use_container_width=True
)

st.divider()

# ======================
# TOP PERFUMES
# ======================

st.subheader(
    "🏆 Top Perfumes"
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

    ventas_perfume = (
        ventas_perfume
        .sort_values(
            by="Cantidad",
            ascending=False
        )
    )

    st.dataframe(
        ventas_perfume[
            [
                "Marca",
                "Perfume",
                "Cantidad"
            ]
        ],
        use_container_width=True
    )

else:

    st.info(
        "No existen ventas registradas."
    )

st.divider()

# ======================
# MÉTODOS DE PAGO
# ======================

st.subheader(
    "💳 Métodos de Pago"
)

metodos_pago = ventas[
    "Metodo_Pago"
].value_counts().reset_index()

metodos_pago.columns = [
    "Método",
    "Cantidad"
]

st.dataframe(
    metodos_pago,
    use_container_width=True
)

st.divider()

# ======================
# TIPOS DE ENTREGA
# ======================

st.subheader(
    "🚚 Tipos de Entrega"
)

tipos_entrega = ventas[
    "Tipo_Entrega"
].value_counts().reset_index()

tipos_entrega.columns = [
    "Tipo Entrega",
    "Cantidad"
]

st.dataframe(
    tipos_entrega,
    use_container_width=True
)

st.divider()

# ======================
# ESTADO DE PEDIDOS
# ======================

st.subheader(
    "📦 Estado de Pedidos"
)

estados = ventas[
    "Estado_Pedido"
].value_counts().reset_index()

estados.columns = [
    "Estado",
    "Cantidad"
]

st.dataframe(
    estados,
    use_container_width=True
)

st.divider()

# ======================
# RESUMEN ENVÍOS
# ======================

st.subheader(
    "🚚 Resumen Envíos"
)

resumen_envios = pd.DataFrame(
    {
        "Concepto": [
            "Costo Envíos",
            "IVA Envíos",
            "Total Envíos"
        ],
        "Monto": [
            ventas[
                "Costo_Envio"
            ].sum(),

            ventas[
                "IVA_Envio"
            ].sum(),

            ventas[
                "Total_Envio"
            ].sum()
        ]
    }
)

st.dataframe(
    resumen_envios,
    use_container_width=True
)