import streamlit as st
import pandas as pd

import base64

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
	
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


from utils.pricing import (
    precio_venta,
    iva_cobrado
)


st.set_page_config(
    page_title="D912",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="expanded"
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

    [data-testid="stSidebarNav"] * {
        text-transform: capitalize;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>

    /* ======================
       FONDO GENERAL
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

    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
    }

    /* ======================
       TEXTO GENERAL
    ====================== */

    h1, h2, h3, h4, h5, h6,
    p, span, label {
        color: #111111 !important;
    }

    /* ======================
       SELECTBOX
    ====================== */

    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid #DADADA !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] * {
        color: #111111 !important;
    }

    div[data-baseweb="select"] svg {
        fill: #111111 !important;
    }

    /* ======================
       INPUTS
    ====================== */

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border-radius: 10px !important;
    }

    .stTextInput input::placeholder {
        color: #777777 !important;
    }

    /* ======================
       RADIO BUTTONS
    ====================== */

    [data-baseweb="radio"] * {
        color: #111111 !important;
    }

    /* ======================
       BOTONES
    ====================== */

    button {
        background-color: #232531 !important;
        color: #FFFFFF !important;
        border-radius: 10px !important;
        border: none !important;
    }

    button span {
        color: #FFFFFF !important;
    }

    button p {
        color: #FFFFFF !important;
    }

    button:hover {
        background-color: #232531 !important;
        color: #FFFFFF !important;
    }

    button:hover span {
        color: #FFFFFF !important;
    }

    /* ======================
       MÉTRICAS
    ====================== */

    [data-testid="stMetricValue"] {
        color: #111111 !important;
    }

    /* ======================
       ALERTAS D912
    ====================== */

    [data-testid="stAlert"] {
        background-color: #EAF3FF !important;
        border: 1px solid #BFD9FF !important;
        border-radius: 12px !important;
    }

    [data-testid="stAlert"] > div {
        background-color: #EAF3FF !important;
    }

    [data-testid="stAlert"] * {
        color: #111111 !important;
    }

    [data-testid="stAlert"] svg {
        fill: #2F6FED !important;
    }

    /* ======================
       EXPANDER
    ====================== */

    [data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }

    [data-testid="stExpander"] summary {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    [data-testid="stExpander"] summary * {
        color: #FFFFFF !important;
    }

    /* TEXTO DENTRO DEL EXPANDER */

    [data-testid="stExpander"] p,
    [data-testid="stExpander"] div,
    [data-testid="stExpander"] span {
        color: #111111 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

from utils.data_manager import (
    cargar_catalogo,
    cargar_precios,
    cargar_inventario,
    cargar_clientes,
    guardar_clientes
)

catalogo = cargar_catalogo()
precios = cargar_precios()
inventario = cargar_inventario()

# ======================
# SIDEBAR
# ======================

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

# ======================
# ENCABEZADO
# ======================

# ======================
# LOGO
# ======================

from pathlib import Path

logo_path = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "assets"
    / "logo_d912.png"
)

col1, col2, col3 = st.columns(
    [1, 2, 1]
)

with col2:

    st.image(
        str(logo_path),
        width=400
    )

st.markdown(
    """
    <h3 style="
        text-align:center;
        color:#222222;
        margin-top:-20px;
    ">
        Tu estilo. Tu perfume.
    </h3>
    """,
    unsafe_allow_html=True
    )

st.markdown(
    """
    <div style="
        background-color:#DCDCDC;
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:#111111;
        font-size:20px;
    ">
    
    Colección D912

    Perfumes de diseñador y nicho organizados para facilitar la exploración, comparación y descubrimiento de nuevas propuestas olfativas.
    
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    """
Una colección pensada para quienes disfrutan descubrir la perfumería.

Desde clásicos contemporáneos hasta creaciones de nicho con personalidad propia.
"""
)

catalogo = cargar_catalogo()
precios = cargar_precios()
inventario = cargar_inventario()

if "carrito" not in st.session_state:
    st.session_state.carrito = []

# ======================
# FILTROS
# ======================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    lista_marcas = (
        ["Todas"]
        + sorted(
            catalogo["Marca"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    marca_default = "Todas"

    if (
        "marca_home"
        in st.session_state
    ):

        marca_default = (
            st.session_state[
                "marca_home"
            ]
        )

    marca = st.selectbox(
        "Marca",
        lista_marcas,
        index=(
            lista_marcas.index(
                marca_default
            )
            if marca_default
            in lista_marcas
            else 0
        )
    )

    if (
        "marca_home"
        in st.session_state
    ):

        del st.session_state[
            "marca_home"
        ]

with col2:

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

with col3:

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

with col4:

    valor_busqueda = ""

    if (
        "perfume_home"
        in st.session_state
    ):

        valor_busqueda = (
            st.session_state[
                "perfume_home"
            ]
        )

    busqueda = st.text_input(
        "🔎 Buscar",
        value=valor_busqueda
    )

    if (
        "perfume_home"
        in st.session_state
    ):

        del st.session_state[
            "perfume_home"
        ]

with col5:

    ordenar = st.selectbox(
        "Ordenar",
        [
            "Predeterminado",
            "Precio ↑",
            "Precio ↓"
        ]
    )

# ======================
# FILTRADO
# ======================

catalogo_filtrado = catalogo.copy()

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

        |

        catalogo_filtrado["Marca"]
        .astype(str)
        .str.contains(
            busqueda,
            case=False,
            na=False
        )
    ]

catalogo_filtrado = catalogo_filtrado.merge(
    precios[
        [
            "ID_Producto",
            "Precio_5ml"
        ]
    ],
    on="ID_Producto",
    how="left"
)

catalogo_filtrado["Precio_5ml"] = pd.to_numeric(
    catalogo_filtrado["Precio_5ml"],
    errors="coerce"
)

if ordenar == "Precio ↓":

    catalogo_filtrado = (
        catalogo_filtrado
        .sort_values(
            "Precio_5ml",
            ascending=True
        )
    )

elif ordenar == "Precio ↑":

    catalogo_filtrado = (
        catalogo_filtrado
        .sort_values(
            "Precio_5ml",
            ascending=False
        )
    )

st.success(
    f" Fragancias para descubrir: {len(catalogo_filtrado)}"
)

# ======================
# CARRITO
# ======================

if "checkout" not in st.session_state:
    st.session_state.checkout = False

cantidad_total = sum(
    item.get("Cantidad", 1)
    for item in st.session_state.carrito
)

st.subheader(
    f"🛒 Carrito ({cantidad_total})"
)

total_carrito = 0

for i, item in enumerate(
    st.session_state.carrito
):

    fila_precio = precios[
        precios["ID_Producto"]
        == item["ID_Producto"]
    ].iloc[0]


    precio_item = precio_venta(
    fila_precio[
        f"Precio_{item['Tamano']}ml"
    ]
)

    cantidad = item.get(
        "Cantidad",
        1
    )

    subtotal_item = (
        precio_item
        * cantidad
    )
     
    total_carrito += subtotal_item

    col1, col2 = st.columns([8, 1])

    with col1:

        cantidad = item.get(
            "Cantidad",
            1
        )

        st.write(
           f"• {item['Perfume']} - "
           f"{item['Tamano']} ml "
           f"x{cantidad} "
           f"- ${subtotal_item:,.0f}"
        
        )

    with col2:

        if st.button(
            "❌",
            key=f"eliminar_{i}"
        ):

            st.session_state.carrito.pop(i)

            st.rerun()

st.write(
    f"### Total: ${total_carrito:,.0f}"
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🗑 Vaciar carrito"
    ):

        st.session_state.carrito = []

        st.rerun()

with col2:

    if len(st.session_state.carrito) > 0:

        if st.button(
            "➡️ Continuar con el pedido"
        ):

            st.session_state.checkout = True

            st.rerun()

# ======================
# CHECKOUT
# ======================

if st.session_state.checkout:

    st.divider()

    with st.expander(
        "📋 Completar datos para el envío",
        expanded=True
    ):

        nombre = st.text_input(
            "👤 Nombre Completo"
        )

        telefono = st.text_input(
            "📱 Teléfono"
        )

        instagram = st.text_input(
            "📸 Instagram (Opcional)"
        )

        correo = st.text_input(
            "📧 Correo Electrónico (Obligatorio)"
        )

        col_a, col_b = st.columns(2)

        with col_a:

            comuna = st.text_input(
                "📍 Comuna"
            )

        with col_b:

            region = st.text_input(
                "🌎 Región"
            )

        ciudad = st.text_input(
            "🏙 Ciudad"
        )

        direccion = st.text_input(
            "🏠 Dirección"
        )

        tipo_envio = st.radio(
            "🚚 Método de entrega",
            [
                "Región Metropolitana (+$3.100)",
                "Otras regiones (+$4.300)",
                "Zonas extremas (Arica y Parinacota, Tarapacá, Aysén y Magallanes) (+$5.200)"
            ]
        )

        if tipo_envio == "Región Metropolitana (+$3.100)":

            costo_envio = 2605

        elif tipo_envio == "Otras regiones (+$4.300)":

            costo_envio = 3613

        elif tipo_envio == (
            "Zonas extremas (Arica y Parinacota, Tarapacá, Aysén y Magallanes) (+$5.200)"
        ):

            costo_envio = 4370

        else:

            costo_envio = 0

        subtotal_productos = total_carrito

        iva_envio = round(
            costo_envio * 0.19
        )

        costo_envio_final = (
            costo_envio
            + iva_envio
        )

        total_final = (
            subtotal_productos
            + costo_envio_final
        )
	

        campos_completos = (
            nombre.strip()
            and telefono.strip()
            and comuna.strip()
            and region.strip()
            and ciudad.strip()
            and direccion.strip()
        )

        if campos_completos:

            st.markdown(
                "### 📋 Resumen del Pedido"
            )

            for item in st.session_state.carrito:

                fila_precio = precios[
                    precios["ID_Producto"]
                    == item["ID_Producto"]
                ].iloc[0]

                precio_item = precio_venta(
                    fila_precio[
                        f"Precio_{item['Tamano']}ml"
                    ]          
                )

                cantidad = item.get(
                    "Cantidad",
                    1
                )

                subtotal_item = (
                    precio_item
                    * cantidad
                )

                st.write(
                    f"• {item['Perfume']} - "
                    f"{item['Tamano']} ml "
                    f"x{cantidad} "
                    f"(${subtotal_item:,.0f})"
                )

            st.divider()

            subtotal_productos = total_carrito

            costo_envio_final = precio_venta(
                costo_envio
            ) if costo_envio > 0 else 0

            total_final = (
                subtotal_productos
                + costo_envio_final
            )

            st.write(
                f"**Subtotal productos:** ${subtotal_productos:,.0f}"
            )

            st.write(
                f"**Envío:** ${costo_envio_final:,.0f}"
            )

            st.markdown(
                f"## 💰 Total Final: ${total_final:,.0f}"
            )

            mensaje = (
                "Hola D912%0A%0A"
                "Me gustaría realizar el siguiente pedido:%0A%0A"
                "DATOS CLIENTE%0A%0A"
                f"Nombre: {nombre}%0A"
                f"Teléfono: {telefono}%0A"
                f"Instagram: {instagram}%0A"
                f"Correo: {correo}%0A"
                f"Dirección: {direccion}%0A"
                f"Comuna: {comuna}%0A"
                f"Ciudad: {ciudad}%0A"
                f"Región: {region}%0A%0A"
                "PEDIDO%0A%0A"
            )

            for item in st.session_state.carrito:

                cantidad = item.get(
                    "Cantidad",
                    1
                )

                mensaje += (
                    f"• {item['Perfume']} - "
                    f"{item['Tamano']} ml "
                    f"x{cantidad}%0A"
                )

            mensaje += (
                "%0A"
                "ENTREGA%0A%0A"
                f"Envío: ${costo_envio_final:,.0f}%0A%0A"
                "RESUMEN%0A%0A"
                f"Productos: ${subtotal_productos:,.0f}%0A"
                f"TOTAL: ${total_final:,.0f}"
            )

            url = (
                "https://wa.me/"
                "56995753146"
                f"?text={mensaje}"
            )

            url = (
                "https://wa.me/"
                "56995753146"
                f"?text={mensaje}"
            )

            if st.button(
                "📲 Finalizar pedido"
            ):

                clientes = cargar_clientes()

                telefono_limpio = str(
                    telefono
                ).strip()

                existe = clientes[
                    clientes["Telefono"]
                    .astype(str)
                    .str.strip()
                    == telefono_limpio
                ]

                if len(existe) == 0:

                    partes = nombre.split()

                    nombre_cliente = (
                        partes[0]
                        if len(partes) > 0
                        else ""
                    )

                    apellido_cliente = (
                        " ".join(partes[1:])
                        if len(partes) > 1
                        else ""
                    )

                    if len(
                        clientes
                    ) == 0:

                        nuevo_id = 1

                    else:

                        nuevo_id = (
                            pd.to_numeric(
                                clientes["ID_Cliente"],
                                errors="coerce"
                            ).max()
                            + 1
                        )
                    

                    nuevo_cliente = pd.DataFrame([
                        {
                            "ID_Cliente": nuevo_id,
                            "Nombre": nombre_cliente,
                            "Apellido": apellido_cliente,
                            "Telefono": telefono,
                            "Email": correo,
                            "Instagram": instagram,
                            "Ciudad": ciudad,
                            "Fecha_Registro": pd.Timestamp.now().strftime(
                                "%Y-%m-%d %H:%M:%S"
                            ),
                            "Ultima_Compra": pd.Timestamp.now().strftime(
                                "%Y-%m-%d %H:%M:%S"
                            ),
                            "Total_Compras": "0",
                            "Total_Pedidos": "1",
                            "Observaciones": "",
                            "Nombre_Completo": nombre
                        }
                    ])

                    clientes = pd.concat(
                        [
                            clientes,
                            nuevo_cliente
                        ],
                        ignore_index=True
                    )

                    guardar_clientes(
                        clientes
                    )

                    st.success(
                        "✅ Cliente registrado correctamente."
                    )

                else:

                    indice = existe.index[0]

                    clientes.loc[
                        indice,
                        "Ultima_Compra"
                    ] = pd.Timestamp.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                    clientes.loc[
                        indice,
                        "Total_Pedidos"
                    ] = str(
                        int(
                            clientes.loc[
                                indice,
                                "Total_Pedidos"
                            ]
                        )
                        + 1
                    )

                    guardar_clientes(
                        clientes
                    )

                    st.success(
                        "✅ Cliente actualizado."
                    )

                st.link_button(
                    "📲 Abrir WhatsApp",
                    url
                )

        else:

            st.warning(
                "Completa Nombre, Teléfono, Ciudad, Comuna y Región para continuar."
            )

# ======================
# PERFUMES
# ======================

cols = st.columns(3)

for i, (_, perfume) in enumerate(
    catalogo_filtrado.iterrows()
):

    with cols[i % 3]:

        with st.container(border=True):

            if perfume["Perfume"] == "Abejorro":

                st.image(
                    str(
                        Path(__file__)
                        .resolve()
                        .parent
                        .parent
                        .parent
                        / "assets"
                        / "abeja.png"
                    ),
                    width=200
                )

            elif perfume["Perfume"] == "Huemul":

                st.image(
                    str(
                        Path(__file__)
                        .resolve()
                        .parent
                        .parent
                        .parent
                        / "assets"
                        / "huemul.png"
                    ),
                    width=200
                )

            elif pd.notna(perfume["Imagen_URL"]):

                try:
                    st.image(
                        perfume["Imagen_URL"],
                        width=200
                    )
                except:
                    pass

            st.markdown(
                f"""
                <div style="
                    color:#777777;
                    font-size:14px;
                    margin-bottom:4px;
                ">
                    {perfume['Marca']}
                </div>

                <h3 style="
                    margin-top:0px;
                    margin-bottom:4px;
                    line-height:1.1;
                ">
                    {perfume['Perfume']}
                </h3>
                """,
                unsafe_allow_html=True
            )

            precio = precios[
                precios["ID_Producto"]
                == perfume["ID_Producto"]
            ]

            if len(precio) > 0:

                precio = precio.iloc[0]

                
                precio_2 = precio_venta(
                    precio["Precio_2ml"]
                )

                precio_3 = precio_venta(
                    precio["Precio_3ml"]
                )

                precio_5 = precio_venta(
                    precio["Precio_5ml"]
                )

                precio_10 = precio_venta(
                    precio["Precio_10ml"]
                )

                st.markdown(
                    f"""
                    <div style="
                        line-height:1.35;
                        margin-top:-5px;
                    ">
                        <strong>2 ml:</strong> ${precio_2:,.0f}<br>
                        <strong>3 ml:</strong> ${precio_3:,.0f}<br>
                        <strong>5 ml:</strong> ${precio_5:,.0f}<br>
                        <strong>10 ml:</strong> ${precio_10:,.0f}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                tamano_carrito = st.selectbox(
                    "Tamaño",
                    [2, 3, 5, 10],
                    key=f"tamano_{perfume['ID_Producto']}"
                )

                col_btn1, col_btn2 = st.columns([1.3, 1.5])

                with col_btn1:

                    if st.button(
                        "🛒 Agregar",
                        key=f"agregar_{perfume['ID_Producto']}"
                    ):

                        encontrado = False

                        for item in st.session_state.carrito:

                            if (
                                item["ID_Producto"]
                                == perfume["ID_Producto"]
                                and item["Tamano"]
                                == tamano_carrito
                            ):

                                item["Cantidad"] = (
                                    item.get(
                                        "Cantidad",
                                        1
                                    ) + 1
                                )

                                encontrado = True

                                break

                        if not encontrado:

                            st.session_state.carrito.append(
                                {
                                    "ID_Producto": perfume["ID_Producto"],
                                    "Marca": perfume["Marca"],
                                    "Perfume": perfume["Perfume"],
                                    "Tamano": tamano_carrito,
                                    "Cantidad": 1
                                }
                            )

                        st.success(
                            "Agregado"
                        )

                        st.rerun()

                with col_btn2:

                    if st.button(
                        "⚖️ Compara",
                        key=f"comparar_{perfume['ID_Producto']}"
                    ):

                        if (
                            "comparar_base" in st.session_state
                            and
                            st.session_state[
                                "comparar_base"
                            ]
                            == perfume[
                                "ID_Producto"
                            ]
                        ):

                            del st.session_state[
                                "comparar_base"
                            ]

                        else:

                            st.session_state[
                                "comparar_base"
                            ] = perfume[
                                "ID_Producto"
                            ]

                        st.rerun()

            with st.expander(
                "Ver detalles"
            ):

                if (
                    "comparar_base" in st.session_state
                    and
                    st.session_state["comparar_base"]
                    == perfume["ID_Producto"]
                ):

                    lista_perfumes = (
                        catalogo[
                            catalogo["ID_Producto"]
                            != perfume["ID_Producto"]
                        ]["Perfume"]
                        .tolist()
                    )

                    perfume_comparado_nombre = st.selectbox(
                        "Comparar con",
                        lista_perfumes,
                        key=f"comparador_{perfume['ID_Producto']}"
                    )

                    perfume_comparado = catalogo[
                        catalogo["Perfume"]
                        == perfume_comparado_nombre
                    ].iloc[0]

                    st.markdown(
                        "<hr style='margin:8px 0;'>",
                        unsafe_allow_html=True
                    )

                    col1, col2, col3 = st.columns([0.4,1.6,1.6])

                    with col1:
                        st.write("")

                    with col2:
                        st.caption(
                            perfume["Perfume"]
                        )

                    with col3:
                        st.caption(
                            perfume_comparado["Perfume"]
                        )

                    campos = [
                        ("☀️", "Estacion"),
                        ("⬆️", "Notas_Salida"),
                        ("❤️", "Notas_Corazon"),
                        ("⬇️", "Notas_Fondo")                  
                    ]
                    for nombre, campo in campos:

                        col1, col2, col3 = st.columns(
                            [0.4, 1.6, 1.6]
                        )

                        with col1:

                            st.markdown(
                                f"""
                                <div style="
                                    font-size:11px;
                                    text-align:center;
                                ">
                                    {nombre}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        with col2:

                            st.markdown(
                                f"""
                                <div style="
                                    font-size:13px;
                                    line-height:1.2;
                                ">
                                    {perfume[campo]}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        with col3:

                            st.markdown(
                                f"""
                                <div style="
                                    font-size:13px;
                                    line-height:1.2;
                                ">
                                    {perfume_comparado[campo]}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        st.markdown(
                            """
                            <hr style="
                                margin:6px 0;
                                border:none;
                                border-top:1px solid #DDDDDD;
                            ">
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown(
                        "<hr style='margin:4px 0;'>",
                        unsafe_allow_html=True
                    )

                st.markdown(
    f"""
    <div style="font-size:14px; line-height:1.4;">

    <b>Familia:</b> {perfume['Familia_Olfativa']}<br>
    <b>Duración:</b> {perfume['Duracion']}<br>
    <b>Proyección:</b> {perfume['Proyeccion']}<br>
    <b>Estación:</b> {perfume['Estacion']}<br>
    <b>Uso:</b> {perfume['Uso']}<br>

    </div>
    """,
    unsafe_allow_html=True
)

                st.markdown(
    f"""
    <div style="font-size:14px; line-height:1.4;">

    <b>Pirámide Olfativa</b><br>
    <b>Salida:</b> {perfume['Notas_Salida']}<br>
    <b>Corazón:</b> {perfume['Notas_Corazon']}<br>
    <b>Fondo:</b> {perfume['Notas_Fondo']}<br>

    </div>
    """,
    unsafe_allow_html=True
)

                st.markdown(
                    """
                    <div style="
                        font-size:14px;
                        font-weight:600;
                        margin-bottom:0px;
                    ">
                        Descripción
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div style="
                        font-size:13px;
                        line-height:1.5;
                        text-align:justify;
                    ">
                        {perfume["Descripcion"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
