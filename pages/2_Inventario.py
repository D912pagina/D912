import streamlit as st

from utils.data_manager import (
    cargar_inventario,
    guardar_inventario
)

st.title(
    "📦 Inventario"
)

inventario = cargar_inventario()

# ======================
# MÉTRICAS
# ======================

stock_total = inventario[
    "Stock_Actual_ml"
].sum()

stock_bajo = len(
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

col1, col2, col3, col4 = st.columns(
    4
)

with col1:

    st.metric(
        "📦 Stock Total",
        f"{stock_total:,.0f} ml"
    )

with col2:

    st.metric(
        "🧴 Perfumes",
        len(
            inventario
        )
    )

with col3:

    st.metric(
        "🔴 Críticos",
        stock_bajo
    )

with col4:

    st.metric(
        "🏷️ Marcas",
        inventario[
            "Marca"
        ].nunique()
    )

st.divider()

# ======================
# FILTROS
# ======================

col1, col2 = st.columns(
    2
)

with col1:

    marca = st.selectbox(
        "🏷️ Filtrar por marca",
        [
            "Todas"
        ]
        +
        sorted(
            inventario[
                "Marca"
            ]
            .dropna()
            .unique()
            .tolist()
        )
    )

with col2:

    busqueda = st.text_input(
        "🔎 Buscar perfume"
    )

# ======================
# FILTRAR
# ======================

if marca != "Todas":

    inventario = inventario[
        inventario[
            "Marca"
        ]
        ==
        marca
    ]

if busqueda:

    inventario = inventario[
        inventario[
            "Perfume"
        ]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    ]

# ======================
# ESTADO
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


inventario[
    "Estado"
] = inventario.apply(
    estado_stock,
    axis=1
)

# ======================
# ALERTAS
# ======================

stock_bajo_df = inventario[
    inventario[
        "Stock_Actual_ml"
    ]
    <=
    inventario[
        "Stock_Minimo_ml"
    ]
]

if len(
    stock_bajo_df
) > 0:

    st.warning(
        (
            f"🔴 Hay "
            f"{len(stock_bajo_df)} "
            f"producto(s) en estado critico."
        )
    )

# ======================
# TABLA PRINCIPAL
# ======================

st.subheader(
    "📋 Inventario Actual"
)

st.dataframe(
    inventario[
        [
            "Marca",
            "Perfume",
            "Stock_Actual_ml",
            "Stock_Minimo_ml",
            "Estado"
        ]
    ],
    use_container_width=True
)

st.divider()

# ======================
# TOP STOCK
# ======================

st.subheader(
    "🏆 Mayor Stock Disponible"
)

top_stock = inventario.sort_values(
    by="Stock_Actual_ml",
    ascending=False
)

st.dataframe(
    top_stock[
        [
            "Marca",
            "Perfume",
            "Stock_Actual_ml"
        ]
    ]
    .head(10),
    use_container_width=True
)

# ======================
# AJUSTE DE STOCK
# ======================

st.divider()

st.subheader(
    "⚙️ Ajuste de Stock"
)

inventario_completo = cargar_inventario()

inventario_completo[
    "Perfume_Mostrar"
] = (
    inventario_completo["Marca"]
    .fillna("")
    + " | "
    + inventario_completo["Perfume"]
    .fillna("")
)

perfume_stock = st.selectbox(
    "🧴 Seleccionar perfume",
    inventario_completo[
        "Perfume_Mostrar"
    ].tolist()
)

fila_perfume = inventario_completo[
    inventario_completo[
        "Perfume_Mostrar"
    ]
    ==
    perfume_stock
].iloc[0]

st.info(
    f"""
Marca: {fila_perfume['Marca']}

Perfume: {fila_perfume['Perfume']}

Stock actual: {fila_perfume['Stock_Actual_ml']} ml

Stock mínimo: {fila_perfume['Stock_Minimo_ml']} ml
"""
)

col1, col2 = st.columns(
    2
)

with col1:

    tipo_movimiento = st.radio(
        "Movimiento",
        [
            "➕ Agregar",
            "➖ Descontar"
        ]
    )

with col2:

    cantidad_ml = st.number_input(
        "Cantidad (ml)",
        min_value=1,
        value=10,
        step=1
    )

if st.button(
    "💾 Aplicar Ajuste",
    use_container_width=True
):

    indice = inventario_completo[
        inventario_completo[
            "ID_Producto"
        ]
        ==
        fila_perfume[
            "ID_Producto"
        ]
    ].index[0]

    stock_anterior = int(
        inventario_completo.loc[
            indice,
            "Stock_Actual_ml"
        ]
    )

    if tipo_movimiento == "➕ Agregar":

        nuevo_stock = (
            stock_anterior
            + cantidad_ml
        )

    else:

        nuevo_stock = max(
            0,
            stock_anterior
            - cantidad_ml
        )

    inventario_completo.loc[
        indice,
        "Stock_Actual_ml"
    ] = nuevo_stock

    guardar_inventario(
        inventario_completo
    )

    st.success(
        (
            f"✅ Stock actualizado\n\n"
            f"Antes: {stock_anterior} ml\n\n"
            f"Ahora: {nuevo_stock} ml"
        )
    )

    st.rerun()