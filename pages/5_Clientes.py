import streamlit as st
import pandas as pd

from utils.data_manager import (
    cargar_clientes
)

st.title("👥 Clientes")

clientes = cargar_clientes()
if len(clientes) == 0:

    st.warning(
        "No existen clientes registrados."
    )

    st.stop()

# ======================
# MÉTRICAS
# ======================
col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "👥 Total Clientes",
        len(clientes)
    )

with col2:

    if len(
        clientes
    ) > 0:

        mejor_cliente = clientes.loc[
            clientes[
                "Total_Compras"
            ].idxmax()
        ]

        st.metric(
            "🏆 Mejor Cliente",
            f"{mejor_cliente['Nombre']} "
            f"{mejor_cliente['Apellido']}"
        )

    else:

        st.metric(
            "🏆 Mejor Cliente",
            "-"
        )

with col3:

    if len(
        clientes
    ) > 0:

        mayor_compra = pd.to_numeric(
            clientes[
                "Total_Compras"
            ],
            errors="coerce"
        ).fillna(
            0
        ).max()


    else:

        mayor_compra = 0

    st.metric(
        "💰 Mayor Compra Acumulada",
        f"${mayor_compra:,.0f}"
    )

st.divider()

# ======================
# BUSCADOR
# ======================

busqueda = st.text_input(
    "🔎 Buscar Cliente"
)

clientes_filtrados = clientes[
    (
        clientes["Nombre"]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    )
    |
    (
        clientes["Apellido"]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    )
    |
    (
        clientes["Telefono"]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    )
    |
    (
        clientes["ID_Cliente"]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    )
]

# ======================
# TABLA
# ======================

st.subheader("📋 Base de Clientes")

st.dataframe(
    clientes_filtrados,
    use_container_width=True
)

st.divider()

# ======================
# FICHA CLIENTE
# ======================

clientes["Cliente_Mostrar"] = (
    "ID "
    + clientes["ID_Cliente"].astype(str)
    + " | "
    + clientes["Telefono"].astype(str)
    + " | "
    + clientes["Nombre"].fillna("")
    + " "
    + clientes["Apellido"].fillna("")
)

cliente_seleccionado = st.selectbox(
    "🔎 Buscar Cliente",
    clientes["Cliente_Mostrar"].tolist(),
    index=None,
    placeholder="Escribe ID, teléfono o nombre..."
)

if cliente_seleccionado:

    ficha = clientes[
        clientes["Cliente_Mostrar"]
        == cliente_seleccionado
    ].iloc[0]

    st.subheader("📇 Ficha Cliente")

    st.write(
        f"🆔 ID Cliente: {ficha['ID_Cliente']}"
    )

    st.write(
        f"👤 Cliente: {ficha['Nombre']} {ficha['Apellido']}"
    )

    st.write(
        f"📞 Teléfono: {ficha['Telefono']}"
    )

    st.write(
        f"📧 Email: {ficha['Email']}"
    )

    st.write(
        f"📸 Instagram: {ficha['Instagram']}"
    )

    st.write(
        f"📍 Ciudad: {ficha['Ciudad']}"
    )

    st.write(
        f"📅 Última Compra: {ficha['Ultima_Compra']}"
    )

    st.write(
        f"📦 Total Pedidos: {ficha['Total_Pedidos']}"
    )

    st.write(
        f"💰 Total Compras: ${ficha['Total_Compras']:,.0f}"
    )

    st.write(
        f"📝 Observaciones: {ficha['Observaciones']}"
    )