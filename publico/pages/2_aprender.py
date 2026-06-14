import streamlit as st
from pathlib import Path

import base64
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

imagen_sidebar = get_base64_image(
    "assets/sidebardark.png"
)

imagen_fondo = get_base64_image(
    "assets/fondodark.png"
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

st.set_page_config(
    page_title="Guía D912",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# ESTILO
# ======================

st.markdown(
    """
    <style>

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

    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] * {
        color: #111111 !important;
    }

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
    }

    .feature-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        height: 100%;
    }

    .feature-box h3,
    .feature-box p {
        color: #111111 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# LOGO
# ======================

logo_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "logo_d912.png"
)

decants_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Decants.png"
)

eau_premiere_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Chanel_N5_Eau_Premiere.png"
)

bleu_chanel = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Chanel_Bleu.png"
)

col1, col2, col3 = st.columns([1,2,1])

with col2:

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
    ¿Qué es un decant?
    </div>

    <br>

    <div class="hero-subtitle">
    Una forma más consciente de descubrir la perfumería.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# IMAGEN
# ======================

st.image(
    str(decants_path),
    use_container_width=True
)

st.divider()

# ======================
# QUÉ ES UN DECANT
# ======================

st.header(
    "¿Qué es un decant?"
)

st.write(
    """
En perfumería, un decant es una cantidad de fragancia cuidadosamente transferida desde su frasco original a un atomizador de menor tamaño, manteniendo intacta la fórmula, concentración y calidad del perfume.

Su principal ventaja es permitir una experiencia real con la fragancia antes de adquirir una presentación de mayor tamaño. A diferencia de una muestra tradicional, un decant ofrece la cantidad suficiente para utilizar el perfume durante varios días o incluso semanas, permitiendo apreciar su evolución completa sobre la piel y conocer con mayor profundidad su carácter, rendimiento y versatilidad.
"""
)

st.divider()

# ======================
# EXPERIENCIA PERSONAL
# ======================

st.header(
    "¿Por qué probar una fragancia durante varios días?"
)

st.write(
    """
La perfumería es una experiencia profundamente personal.

Factores como la química de la piel, el clima, el entorno y las preferencias individuales pueden influir en la percepción de una misma fragancia.

Por ello, probar un perfume durante más de una aplicación resulta fundamental para tomar una decisión informada.
"""
)

st.image(
    str(eau_premiere_path),
    use_container_width=True
)

st.divider()

# ======================
# FORMATOS
# ======================

st.header(
    "Nuestros formatos"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-box">
        <h3>2/3 ml</h3>
        <p>
        Ideal para una primera aproximación a una fragancia. Permite conocer sus notas principales, su evolución y su comportamiento sobre la piel durante varias aplicaciones.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">
        <h3>5 ml</h3>
        <p>
        Una excelente opción para quienes desean explorar una fragancia con mayor profundidad. Ofrece suficientes aplicaciones para utilizarla en distintos contextos y momentos antes de decidir una compra futura.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">
        <h3>10 ml</h3>
        <p>
        Pensado para quienes disfrutan alternar entre diferentes perfumes o desean llevar una fragancia consigo de manera práctica. Su tamaño permite un uso prolongado manteniendo la comodidad de un formato compacto.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.divider()

# ======================
# DURACIÓN APROXIMADA
# ======================

st.header(
    "¿Cuánto dura un decant?"
)

st.write(
    """
La duración de un decant puede variar según la cantidad de aplicaciones diarias, el tipo de atomizador y la forma de uso de cada persona.

Considerando un uso regular de entre 4 y 6 atomizaciones por día, estos son valores aproximados:
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-box">
        <h3>2/3 ml</h3>
        <p>
        Entre <strong>20 y 30 atomizaciones</strong>.
        <br><br>
        Aproximadamente
        <strong>4 a 7 días</strong>
        de uso diario.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">
        <h3>5 ml</h3>
        <p>
        Entre <strong>50 y 75 atomizaciones</strong>.
        <br><br>
        Aproximadamente
        <strong>1 a 2 semanas</strong>
        de uso diario.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">
        <h3>10 ml</h3>
        <p>
        Entre <strong>100 y 150 atomizaciones</strong>.
        <br><br>
        Aproximadamente
        <strong>3 a 4 semanas</strong>
        de uso diario.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.caption(
    "Los valores son referenciales y pueden variar según el atomizador utilizado y la cantidad de aplicaciones realizadas en cada uso."
)

st.divider()

# ======================
# EXPERIENCIA D912
# ======================

st.header(
    "La experiencia D912"
)

st.image(
    str(bleu_chanel),
    use_container_width=True
)

st.write(
    """
Cada decant es preparado individualmente a partir del frasco original de la fragancia, utilizando atomizadores de calidad y un proceso cuidadoso que busca preservar la experiencia del perfume tal como fue concebida por su creador.

Nuestro objetivo es ofrecer una forma más accesible y consciente de descubrir la perfumería, permitiéndote explorar nuevas creaciones, ampliar tu colección y encontrar aquella fragancia que realmente se convierta en parte de tu estilo.
"""
)

st.divider()

# ======================
# CIERRE
# ======================

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.image(
        str(logo_path),
        width=350
    )

st.markdown(
    """
    <div class="hero">

    <div class="hero-title">
    Tu estilo. Tu perfume.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)