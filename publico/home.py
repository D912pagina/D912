import sys
import base64
from pathlib import Path

import pandas as pd
import streamlit as st

def get_base64_image(
    image_path
):

    with open(
        image_path,
        "rb"
    ) as img_file:

        return base64.b64encode(
            img_file.read()
        ).decode()

st.set_page_config(
    page_title="D912",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="expanded"
)

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from utils.data_manager import (
    cargar_catalogo,
    cargar_inventario,
    cargar_ventas
)

st.markdown(
    """
    <style>

    section[data-testid="stSidebar"]{
        width:220px !important;
    }

    section[data-testid="stSidebar"] > div{
        width:220px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

imagen_sidebar = get_base64_image(
    "assets/sidebar.png"
)

imagen_fondo = get_base64_image(
    "assets/fondo.png"
)
st.markdown(
    f"""
    <style>

    [data-testid="stSidebar"] {{

        background-image: url(
            "data:image/png;base64,{imagen_sidebar}"
        );

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>

    .stApp {{

        background-image: url(
            "data:image/png;base64,{imagen_fondo}"
        );

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>

    section[data-testid="stSidebar"]{
        width:220px !important;
    }

    section[data-testid="stSidebar"] > div{
        width:220px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>

    [data-testid="stSidebarNav"] * {
        text-transform: capitalize;
    }

    </style>
    """,
    unsafe_allow_html=True
)


catalogo = cargar_catalogo()


inventario = cargar_inventario()

ventas = cargar_ventas()

inventario_activo = inventario[
    inventario["Estado"]
    .astype(str)
    .str.strip()
    .str.lower()
    ==
    "activo"
]

cantidad_perfumes = len(
    inventario_activo
)

cantidad_marcas = (
    inventario_activo["Marca"]
    .astype(str)
    .str.strip()
    .str.title()
    .nunique()
)

stock_total = int(
    inventario_activo[
        "Stock_Actual_ml"
    ]
    .sum()
)


# ======================
# ESTILO
# ======================

st.markdown(
    """
    <style>

    /* ======================
       TEMA FIJO D912
       ====================== */

    html,
    body,
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }

    [data-testid="stHeader"] {
        background-color: #F3F3F3 !important;
    }

    [data-testid="stToolbar"] {
        background-color: #F3F3F3 !important;
    }

    [data-testid="stSidebar"] * {
        color: #111111 !important;
    }

    [data-testid="stSidebarNav"] * {
        color: #111111 !important;
    }

    .stMarkdown,
    .stMetric,
    .stText,
    .stCaption,
    .stSubheader,
    .stHeader {
        color: #111111 !important;
    }

    /* ======================
       HERO
       ====================== */

    .hero {
        text-align:center;
        padding-top:20px;
        padding-bottom:20px;
    }

    .hero-title {
        font-size:52px;
        font-weight:700;
        color:#111111 !important;
    }

    .hero-subtitle {
        font-size:24px;
        color:#444444 !important;
        margin-bottom:25px;
    }

    .hero-text {
        font-size:18px;
        color:#666666 !important;
        max-width:800px;
        margin:auto;
    }

    /* ======================
       EXPERIENCIA D912
       ====================== */

    .feature-box {
        background: #FFFFFF;
        color: #111111 !important;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    }

    .feature-box h5{
        font-size: 24px;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 20px;
        color: #111111 !important;
    }

    .feature-box p{
        color: #111111 !important;
        line-height: 1.6;
        margin-bottom: 0;
    }

    /* ======================
       PERFUMES DESTACADOS
       ====================== */

    .perfume-box {
        background: #FFFFFF;
        color: #111111 !important;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .perfume-box h4{
        font-size: 20px;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 15px;
        color: #111111 !important;
    }

    .perfume-box p{
        color: #111111 !important;
    }

    /* ======================
       MARCAS
       ====================== */

    .brand-box {
        background: #FFFFFF;
        color: #111111 !important;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .brand-box,
    .brand-box p,
    .brand-box span,
    .brand-box h1,
    .brand-box h2,
    .brand-box h3,
    .brand-box h4 {
        color: #111111 !important;
    }

    /* ======================
       SELECTBOX
       ====================== */

    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] * {
        color: #111111 !important;
    }

    div[data-baseweb="select"] svg {
        fill: #111111 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# LOGO
# ======================

col1, col2, col3 = st.columns(
    [1, 2, 1]
)

with col2:

    logo_path = (
        Path(__file__)
        .resolve()
        .parent
        .parent
        / "assets"
        / "logo_d912.png"
    )

    st.image(
        str(logo_path),
        width=450
    )

# ======================
# HERO
# ======================

st.markdown(
    """
    <div class="hero">

    <div class="hero-title">
    El arte de encontrar tu perfume
    </div>

    <br>

    <div class="hero-subtitle">
    Tu estilo. Tu perfume.
    </div>

    <div class="hero-text">

    Una colección curada de fragancias con carácter e identidad.

    Encuentra aquella que se convierta en parte de tu presencia.

    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# MÉTRICAS
# ======================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Fragancias Seleccionadas",
        cantidad_perfumes
    )

with col2:

    st.metric(
        "Casas de Perfumería",
        cantidad_marcas
    )

with col3:

    st.metric(
        "Cobertura Nacional",
        "Todo Chile"
    )

with col4:

    st.metric(
        "Mililitros Disponibles",
        f"{stock_total:,.0f} ml"
    )

st.divider()

# ======================
# BENEFICIOS
# ======================
st.subheader(
    "La experiencia D912"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        """
        <div class="feature-box">
        <h5>Exploración</h5>
        <p>Accede a un universo de fragancias de diseñador y nicho.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">
        <h5>Conexión</h5>
        <p>Encuentra fragancias que reflejen tu identidad.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">
        <h5>Experiencia</h5>
        <p>Una forma más consciente y personal de vivir la perfumería.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class="feature-box">
        <h5>Elección</h5>
        <p>Explora con libertad antes de dar el siguiente paso.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
 
# ======================
# MARCAS
# ======================

st.divider()

st.subheader(
    "Imprescindibles"
)

if len(ventas) > 0:

    top_ventas = (
        ventas
        .groupby("ID_Producto")["Cantidad"]
        .sum()
        .reset_index()
        .sort_values(
            "Cantidad",
            ascending=False
        )
        .head(6)
    )

    catalogo["ID_Producto"] = (
        catalogo["ID_Producto"]
        .astype(str)
    )

    top_ventas["ID_Producto"] = (
        top_ventas["ID_Producto"]
        .astype(str)
    )

    destacados = (
        top_ventas.merge(
            catalogo,
            on="ID_Producto",
            how="left"
        )
    )

else:

    destacados = (
        catalogo
        .head(6)
    )

cols = st.columns(3)

cols = st.columns(3)

for i, (_, perfume) in enumerate(
    destacados.iterrows()
):

    with cols[i % 3]:

        with st.container(border=True):

            if pd.notna(
                perfume["Imagen_URL"]
            ):

                st.image(
                    perfume["Imagen_URL"],
                    use_container_width=True
                )

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    margin-top:8px;
                ">

                <h4 style="
                    margin-bottom:4px;
                ">
                    {perfume['Perfume']}
                </h4>

                <div style="
                    color:#777777;
                    font-size:14px;
                ">
                    {perfume['Marca']}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Ver perfume",
                key=f"home_{i}"
            ):

                st.session_state[
                    "perfume_home"
                ] = perfume[
                    "Perfume"
                ]

                st.switch_page(
                    "pages/1_catalogo.py"
                )

# ======================
# MARCAS DISPONIBLES
# ======================

marcas = sorted(
    set(
        inventario_activo["Marca"]
        .astype(str)
        .str.strip()
        .str.title()
        .tolist()
    )
)

st.subheader(
    f"Nuestras Casas ({len(marcas)})"
)

with st.expander(
    f"Ver las {len(marcas)} marcas disponibles"
):

    cols = st.columns(4)

for i, marca in enumerate(
    marcas
):

    with cols[i % 4]:

        if st.button(
            marca,
            key=f"marca_{i}"
        ):

            st.session_state[
                "marca_home"
            ] = marca

            st.switch_page(
                "pages/1_catalogo.py"
            )

st.divider()

# ======================
# CTA
# ======================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:30px;
    ">

    <h2>
    Explora nuestro catálogo
    </h2>

    <p>
    Adéntrate en un universo de aromas 
    donde cada creación cuenta 
    una historia diferente.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    "Recorre el catálogo y conoce cada una de las fragancias disponibles en D912."
)