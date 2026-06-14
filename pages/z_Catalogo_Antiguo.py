import streamlit as st
import pandas as pd

from utils.data_manager import (
    cargar_catalogo,
    cargar_precios,
    cargar_inventario
)

st.title("🧴 Catálogo D912")

catalogo = cargar_catalogo()
precios = cargar_precios()
inventario = cargar_inventario()

# ======================
# FILTROS
# ======================

marca = st.selectbox(
    "Marca",
    ["Todas"]
    + sorted(
        catalogo["Marca"]
        .dropna()
        .unique()
        .tolist()
    )
)

genero = st.selectbox(
    "Género",
    ["Todos"]
    + sorted(
        catalogo["Genero"]
        .dropna()
        .unique()
        .tolist()
    )
)

familia = st.selectbox(
    "Familia Olfativa",
    ["Todas"]
    + sorted(
        catalogo["Familia_Olfativa"]
        .dropna()
        .unique()
        .tolist()
    )
)

busqueda = st.text_input(
    "🔎 Buscar Perfume"
)

# ======================
# FILTRADO
# ======================

catalogo_filtrado = catalogo.copy()

# ======================
# SOLO ACTIVOS
# ======================

catalogo_filtrado = catalogo_filtrado.merge(
    inventario[
        [
            "ID_Producto",
            "Estado"
        ]
    ],
    on="ID_Producto",
    how="left"
)

catalogo_filtrado = catalogo_filtrado[
    catalogo_filtrado["Estado"] == "Activo"
]

# ======================
# APLICAR FILTROS
# ======================

if marca != "Todas":

    catalogo_filtrado = catalogo_filtrado[
        catalogo_filtrado["Marca"] == marca
    ]

if genero != "Todos":

    catalogo_filtrado = catalogo_filtrado[
        catalogo_filtrado["Genero"] == genero
    ]

if familia != "Todas":

    catalogo_filtrado = catalogo_filtrado[
        catalogo_filtrado["Familia_Olfativa"]
        == familia
    ]

if busqueda:

    catalogo_filtrado = catalogo_filtrado[
        catalogo_filtrado["Perfume"]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    ]

st.write(
    f"Perfumes encontrados: {len(catalogo_filtrado)}"
)

# ======================
# PERFUMES
# ======================

cols = st.columns(3)

for i, (_, perfume) in enumerate(
    catalogo_filtrado.iterrows()
):

    with cols[i % 3]:

        if pd.notna(perfume["Imagen_URL"]):

            try:
                st.image(
                    perfume["Imagen_URL"],
                    width=150
                )
            except:
                pass

        st.caption(
            perfume["Marca"]
        )

        st.markdown(
            f"### {perfume['Perfume']}"
        )

        precio = precios[
            precios["ID_Producto"]
            == perfume["ID_Producto"]
        ]

        if len(precio) > 0:

            precio = precio.iloc[0]

            st.write(
                f"""
**2 ml:** ${precio['Precio_2ml']:,.0f}

**5 ml:** ${precio['Precio_5ml']:,.0f}

**10 ml:** ${precio['Precio_10ml']:,.0f}
"""
            )

        with st.expander("🔍 Ver detalles"):

            st.markdown(
                f"""
**Familia:** {perfume['Familia_Olfativa']}

**Duración:** {perfume['Duracion']}

**Proyección:** {perfume['Proyeccion']}

**Estación:** {perfume['Estacion']}

**Uso:** {perfume['Uso']}
"""
            )

            st.markdown(
                f"""
### 🎼 Pirámide Olfativa

**🍋 Salida:** {perfume['Notas_Salida']}

**🌸 Corazón:** {perfume['Notas_Corazon']}

**🌲 Fondo:** {perfume['Notas_Fondo']}
"""
            )

            st.markdown(
                "### 📝 Descripción"
            )

            st.write(
                perfume["Descripcion"]
            )