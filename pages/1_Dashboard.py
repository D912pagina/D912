import streamlit as st
import pandas as pd

from utils.data_manager import (
    cargar_inventario,
    cargar_clientes,
    cargar_ventas
)

st.title("📊 Dashboard")

inventario = cargar_inventario()

inventario[
    "Stock_Actual_ml"
] = pd.to_numeric(
    inventario[
        "Stock_Actual_ml"
    ],
    errors="coerce"
)

inventario[
    "Stock_Minimo_ml"
] = pd.to_numeric(
    inventario[
        "Stock_Minimo_ml"
    ],
    errors="coerce"
)

clientes = cargar_clientes()
ventas = cargar_ventas()

# ======================
# MÉTRICAS PRINCIPALES
# ======================

ventas["Total_Facturado"] = pd.to_numeric(
    ventas["Total_Facturado"],
    errors="coerce"
).fillna(0)

ventas["Subtotal_Productos"] = pd.to_numeric(
    ventas["Subtotal_Productos"],
    errors="coerce"
).fillna(0)

ventas["Total_Envio"] = pd.to_numeric(
    ventas["Total_Envio"],
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

stock_critico = len(
    inventario[
        inventario[
            "Stock_Actual_ml"
        ]
        <=
        inventario[
            "Stock_Minimo_ml"
        ]
    ]
)

stock_bajo = len(
    inventario[
        (
            inventario[
                "Stock_Actual_ml"
            ]
            >
            inventario[
                "Stock_Minimo_ml"
            ]
        )
        &
        (
            inventario[
                "Stock_Actual_ml"
            ]
            <=
            inventario[
                "Stock_Minimo_ml"
            ]
            * 2
        )
    ]
)

# ======================
# FILA 1
# ======================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💵 Facturación Total",
        f"${facturacion_total:,.0f}"
    )

with col2:
    st.metric(
        "👥 Clientes",
        len(clientes)
    )

with col3:
    st.metric(
        "🧴 Perfumes",
        len(inventario)
    )

with col4:
    st.metric(
        "🔴 Stock Crítico",
        stock_critico
    )

# ======================
# FILA 2
# ======================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "💰 Ventas Productos",
        f"${ventas_productos:,.0f}"
    )

with col2:
    st.metric(
        "🚚 Ingresos Envíos",
        f"${ingresos_envio:,.0f}"
    )

with col3:
    st.metric(
        "🧾 IVA Productos",
        f"${iva_productos:,.0f}"
    )

with col4:
    st.metric(
        "📦 IVA Envíos",
        f"${iva_envios:,.0f}"
    )

with col5:
    st.metric(
        "🧾 IVA Total",
        f"${iva_total:,.0f}"
    )

st.divider()

# ======================
# ALERTAS INVENTARIO
# ======================

st.subheader(
    "📦 Alertas de Inventario"
)

criticos = inventario[
    inventario[
        "Stock_Actual_ml"
    ]
    <=
    inventario[
        "Stock_Minimo_ml"
    ]
]

bajos = inventario[
    (
        inventario[
            "Stock_Actual_ml"
        ]
        >
        inventario[
            "Stock_Minimo_ml"
        ]
    )
    &
    (
        inventario[
            "Stock_Actual_ml"
        ]
        <=
        inventario[
            "Stock_Minimo_ml"
        ]
        * 2
    )
]

col1, col2 = st.columns(
    2
)

with col1:

    st.metric(
        "🔴 Críticos",
        len(
            criticos
        )
    )

with col2:

    st.metric(
        "🟡 Bajos",
        len(
            bajos
        )
    )

if len(
    criticos
) > 0:

    st.error(
        (
            f"⚠️ Existen "
            f"{len(criticos)} "
            f"producto(s) en estado crítico."
        )
    )

    st.dataframe(
        criticos[
            [
                "Marca",
                "Perfume",
                "Stock_Actual_ml",
                "Stock_Minimo_ml"
            ]
        ],
        use_container_width=True
    )

if len(
    bajos
) > 0:

    st.warning(
        (
            f"⚠️ Existen "
            f"{len(bajos)} "
            f"producto(s) con stock bajo."
        )
    )

    st.dataframe(
        bajos[
            [
                "Marca",
                "Perfume",
                "Stock_Actual_ml",
                "Stock_Minimo_ml"
            ]
        ],
        use_container_width=True
    )

if (
    len(criticos)
    == 0
    and
    len(bajos)
    == 0
):

    st.success(
        "✅ Inventario saludable."
    )

st.divider()

# ======================
# ÚLTIMAS VENTAS
# ======================

st.subheader(
    "🛒 Últimas Ventas"
)

ultimas_ventas = ventas.sort_values(
    by="ID_Venta",
    ascending=False
).head(10)

st.dataframe(
    ultimas_ventas[
        [
            "Fecha",
            "ID_Cliente",
            "Subtotal_Productos",
            "Total_Envio",
            "Total_Facturado",
            "Estado_Pedido"
        ]
    ],
    use_container_width=True
)

st.divider()

# ======================
# TOP PERFUMES VENDIDOS
# ======================

st.subheader(
    "🏆 Top Perfumes Vendidos"
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
                "Perfume",
                "Cantidad"
            ]
        ],
        use_container_width=True
    )

else:

    st.info(
        "Aún no existen ventas registradas."
    )