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

st.set_page_config(
    page_title="Nuestra Historia",
    page_icon="🖤",
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
        margin-bottom: 20px;
    }

    .feature-box h2,
    .feature-box h3,
    .feature-box h4,
    .feature-box p,
    .feature-box span {
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
    Nuestra Historia
    </div>

    <br>

    <div class="hero-subtitle">
    El origen, la filosofía y la visión detrás de D912.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# D912
# ======================

st.header(
    "D912"
)

st.write(
    """
Toda pasión comienza con un descubrimiento.

Antes de convertirse en una marca, D912 nació de la curiosidad. De horas explorando fragancias, comparando notas, aprendiendo sobre familias olfativas y descubriendo un universo que hasta entonces había pasado desapercibido.

Como muchos entusiastas de la perfumería, comenzamos nuestro recorrido a través de los decants. No solo como consumidores, sino también como estudiantes de este arte. Cada pequeño atomizador representaba una oportunidad para conocer nuevas creaciones, ampliar nuestros gustos y comprender que elegir un perfume es una experiencia mucho más personal de lo que parece.

Con el tiempo surgió una idea simple: crear el tipo de espacio que nosotros mismos habríamos querido encontrar cuando dimos nuestros primeros pasos en la perfumería.

Así nació D912.

Nuestro objetivo nunca ha sido únicamente ofrecer fragancias. Buscamos acercar la perfumería a más personas, hacerla más accesible para quienes desean explorar nuevas propuestas y compartir el conocimiento que hemos adquirido durante este camino.

Creemos que muchas personas desconocen qué es un decant y el enorme valor que puede tener como herramienta de descubrimiento. Un perfume no se comprende en una sola aplicación ni en una tira de papel. Requiere tiempo, experiencia y la libertad de convivir con él antes de tomar una decisión.

Por eso seleccionamos cuidadosamente cada fragancia y preparamos cada decant con el mismo cuidado con el que nosotros mismos querríamos recibirlo.
"""
)

st.divider()

# ======================
# EL ORIGEN DEL NOMBRE
# ======================

st.header(
    "El origen del nombre"
)

st.write(
    """
Detrás de D912 existe una historia sencilla que nos acompaña desde el inicio.

El nombre proviene del departamento 912, un lugar que durante mucho tiempo fue parte importante de los primeros pasos del proyecto. Aunque ese espacio ya no forma parte de nuestras operaciones, su número permaneció como símbolo de nuestros comienzos.

Hoy, D912 representa mucho más que una dirección.

Representa la curiosidad por descubrir, el aprendizaje constante y la convicción de que cada persona merece encontrar una fragancia que realmente conecte con su estilo.
"""
)

st.divider()

# ======================
# NUESTRA FILOSOFÍA
# ======================

st.header(
    "Nuestra Filosofía"
)

st.write(
    """
La perfumería no debería sentirse exclusiva por ser inaccesible.

Debería ser exclusiva por las experiencias que es capaz de crear.

Por eso creemos en explorar antes de elegir, aprender antes de comprar y descubrir antes de decidir.

Porque encontrar tu perfume ideal no es una compra.

Es un proceso.

Es una búsqueda.

Y, para muchos de nosotros, termina convirtiéndose en una pasión.
"""
)

st.markdown(
    """
    <div class="feature-box">

    <h2>
    Tu estilo. Tu perfume.
    </h2>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# CONTACTO
# ======================

st.header(
    "Contacto"
)

st.write(
    """
Estamos disponibles para ayudarte, resolver tus dudas y acompañarte en el proceso de descubrir tu próxima fragancia.
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3>
        Instagram
        </h3>

        @decant.912

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3>
        WhatsApp
        </h3>

        +56 9 9575 3146

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="feature-box">

        <h3>
        Correo
        </h3>

        d912.contacto@gmail.com

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ======================
# HORARIO DE ATENCIÓN
# ======================

st.header(
    "Horario de atención"
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="feature-box">

        <h3>
        Lunes a viernes
        </h3>

        09:00 a 13:00 hrs - 15:00 a 19:00 hrs

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="feature-box">

        <h3>
        Sábados y domingos
        </h3>

        10:00 a 14:00 hrs

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ======================
# ENVÍOS
# ======================

st.header(
    "Envíos"
)

st.info(
    """
Realizamos envíos a todo Chile a través de Blue Express, llevando la experiencia D912 a cada rincón del país.
"""
)

st.divider()

# ======================
# AGRADECIMIENTO
# ======================

st.markdown(
    """
    <div class="hero">

    <div class="hero-subtitle">
    Agradecemos tu confianza y el interés por formar parte de esta comunidad de amantes de la perfumería.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

# ======================
# LOGO FINAL
# ======================

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.image(
        str(logo_path),
        width=350
    )

# ======================
# CIERRE
# ======================

st.markdown(
    """
    <div class="hero">

    <div class="hero-title">
    D912
    </div>

    <br>

    <div class="hero-subtitle">
    Tu estilo. Tu perfume.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)
