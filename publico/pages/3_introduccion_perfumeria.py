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
    page_title="Introducción a la Perfumería",
    page_icon="📚",
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
    .feature-box h4,
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

piramide_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "La pirámide olfativa de lujo.png"
)

notas_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Notas populares de fragancias elegantes.png"
)

dulzor_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Diferentes dulces, distintas emociones.png"
)

frescura_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Comparación visual de fragancias frescas.png"
)

familias_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Mapa de familias olfativas.png"
)

familias_perfumes_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "Familias olfativas y perfumes icónicos.png"
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
    Introducción a la Perfumería
    </div>

    <br>

    <div class="hero-subtitle">
    Comprender las notas, familias y estructuras que dan vida a una fragancia.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# ¿COMO SE CONSTRUYE?
# ======================

st.header(
    "¿Cómo se construye un perfume?"
)

st.write(
    """
Cuando percibimos una fragancia, rara vez experimentamos todos sus aromas al mismo tiempo. Los perfumes están diseñados para evolucionar progresivamente sobre la piel, revelando diferentes facetas a medida que transcurren los minutos y las horas.

Esta evolución se conoce como pirámide olfativa y está compuesta por tres niveles principales: notas de salida, notas de corazón y notas de fondo.
"""
)

# ======================
# IMAGEN PIRAMIDE
# ======================

st.image(
    str(piramide_path),
    use_container_width=True
)

st.divider()

# ======================
# LAS NOTAS
# ======================

st.header(
    "Las notas de un perfume"
)

# ======================
# NOTAS DE SALIDA
# ======================

st.subheader(
    "Notas de salida"
)

st.write(
    """
Son los aromas que percibimos inmediatamente después de aplicar una fragancia. Constituyen la primera impresión y suelen estar formadas por ingredientes frescos y más volátiles.

Aunque son las primeras notas en aparecer, no desaparecen de forma abrupta. Dependiendo de la composición del perfume, pueden permanecer perceptibles desde algunos minutos hasta aproximadamente una hora, mientras comienzan a dar paso gradualmente a las notas de corazón.
"""
)

st.markdown(
    """
### Algunos ejemplos comunes son:

- Bergamota
- Limón
- Pomelo
- Mandarina
- Menta
- Jengibre
- Pimienta rosa
"""
)

# ======================
# IMAGEN SALIDA
# ======================

st.image(
    str(notas_path),
    use_container_width=True
)

st.divider()

# ======================
# NOTAS DE CORAZÓN
# ======================

st.subheader(
    "Notas de corazón"
)

st.write(
    """
Representan el núcleo de la fragancia y suelen aparecer una vez que las notas de salida comienzan a desaparecer.

Son las responsables de la personalidad principal del perfume y suelen mantenerse durante varias horas.

Entre las más comunes encontramos:
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Florales</h3>

        Rosa

        Jazmín

        Peonía

        Flor de azahar

        Ylang-ylang

        Tuberosa

        Iris

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Aromáticas</h3>

        Lavanda

        Salvia

        Romero

        Geranio

        Albahaca
 
        Esclarea

        Enebro

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Frutales</h3>

        Manzana

        Pera

        Durazno

        Frambuesa

        Mango

        Piña

        Cassis
 

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ======================
# NOTAS DE FONDO
# ======================

st.subheader(
    "Notas de fondo"
)

st.write(
    """
Son la base de la fragancia y las responsables de su duración y profundidad.

Aparecen varias horas después de la aplicación y pueden permanecer sobre la piel durante gran parte del día.

Las más habituales son:
"""
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Maderas</h3>

        Cedro

        Sándalo

        Vetiver

        Cachemira

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Resinas y bálsamos</h3>

        Incienso

        Mirra

        Benjuí

        Labdanum

        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

col3, col4 = st.columns(2)

with col3:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Dulces y cálidas</h3>

        Vainilla

        Haba tonka

        Ámbar

        Caramelo

        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Animálicas</h3>

        Almizcle (musk)

        Cuero

        Castóreo (actualmente sintético)

        Civeta

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ======================
# MÁS ALLÁ DE DULCE O FRESCO
# ======================

st.header(
    'Más allá de "dulce" o "fresco"'
)

st.write(
    """
Uno de los errores más comunes al comenzar en la perfumería es describir una fragancia utilizando únicamente términos generales como "dulce", "fresco" o "fuerte".

Aunque estas palabras pueden servir como punto de partida, el universo olfativo es mucho más amplio y complejo.

Por ejemplo, dos perfumes pueden considerarse dulces y, sin embargo, ser completamente diferentes.
"""
)

# ======================
# TIPOS DE DULZOR
# ======================

st.subheader(
    "Distintos tipos de dulzor"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Miel</h3>

        Cálida

        Densa

        Natural


        <strong>Ejemplo:</strong>

        Naxos de Xerjoff

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Vainilla</h3>

        Cremosa

        Suave

        Reconfortante


        <strong>Ejemplo:</strong>

        Armani Stronger With You

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Caramelo</h3>

        Gourmand

        Azucarado

        Postre

        <strong>Ejemplo:</strong>

        Prada Candy

        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

col4, col5 = st.columns(2)

with col4:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Frutal</h3>

        Jugoso

        Tropical

        Vibrante


        <strong>Ejemplo:</strong>

        God of Fire (SHL)

        </div>
        """,
        unsafe_allow_html=True
    )

with col5:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Chocolate</h3>

        Oscuro

        Intenso

        Gourmand


        <strong>Ejemplo:</strong>

        Chocolate Greedy de Montale

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    "<br><br>",
    unsafe_allow_html=True
)

st.image(
    str(dulzor_path),
    use_container_width=True
)

st.divider()

# ======================
# TIPOS DE FRESCURA
# ======================

st.write(
    """
Lo mismo ocurre con las fragancias frescas.
"""
)

st.subheader(
    "Distintos tipos de frescura"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3> Cítrica</h3>

        Limón

        Bergamota

        Mandarina

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3> Marina</h3>

        Agua salada

        Brisa oceánica

        Notas 	Minerales

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">

        <h3> Verde</h3>

        Hojas

        Césped

        Té verde

        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class="feature-box">

        <h3> Limpia</h3>

        Aldehídico

        Almizcles blancos

        Algodón

        </div>
        """,
        unsafe_allow_html=True
    )

st.write(
    """
Dos perfumes frescos pueden parecer completamente distintos dependiendo de qué tipo de frescura predomine.
"""
)

st.image(
    str(frescura_path),
    use_container_width=True
)

st.divider()

# ======================
# FAMILIAS OLFATIVAS
# ======================

st.header(
    "Familias olfativas"
)

st.image(
    str(familias_path),
    use_container_width=True
)

st.write(
    """
Además de Floral, Cítrica, Amaderada, Fougère, Chipre, Oriental, Gourmand, Frutal y Acuática, también existen otras familias que ayudan a describir con mayor precisión el carácter de una fragancia.
"""
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Aromática</h3>

        Lavanda, romero, salvia y hierbas frescas.


        <strong>Ejemplos:</strong>

        Dior Sauvage

        Azzaro Pour Homme

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Cuero</h3>

        Evoca chaquetas de cuero, gamuza y artesanía.


        <strong>Ejemplos:</strong>

        Nishane Safran Colognisé

        Tuscan Leather

        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

col3, col4 = st.columns(2)

with col3:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Almizclada</h3>

        Limpia, suave y cercana a la piel.


        <strong>Ejemplos:</strong>

        Narciso Rodriguez For Her

        Musk Therapy

        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class="feature-box">

        <h3>Verde</h3>

        Inspirada en hojas, tallos y naturaleza viva.


        <strong>Ejemplos:</strong>

        Green Irish Tweed

        Philosykos

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)
st.image(
    str(familias_perfumes_path),
    use_container_width=True
)

st.divider()

# ======================
# COMO ENCONTRAR TU ESTILO
# ======================

st.header(
    "Cómo encontrar tu estilo"
)

st.write(
    """
No existe una familia olfativa mejor que otra.

La elección de una fragancia depende de factores como:
"""
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    st.markdown(
        """
        <div class="feature-box">
        <strong>Estilo</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">
        <strong>Clima</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">
        <strong>Ocasión</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class="feature-box">
        <strong>Experiencia</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

with col5:

    st.markdown(
        """
        <div class="feature-box">
        <strong>Gustos</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

st.write(
    """
Algunas personas se sienten atraídas por la frescura cítrica de una colonia clásica, mientras que otras prefieren la profundidad de una fragancia ambarada o el carácter envolvente de un gourmand.

Conocer las notas y familias olfativas no busca limitar la exploración, sino ofrecer herramientas para comprender mejor aquello que disfrutamos y descubrir nuevas facetas del fascinante mundo de la perfumería.
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