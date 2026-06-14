import streamlit as st

from utils.data_manager import (
    cargar_ventas,
    guardar_ventas,
    cargar_inventario,
    cargar_clientes
)

st.title(
    "📦 Gestión de Pedidos"
)

ventas = cargar_ventas()
inventario = cargar_inventario()
clientes = cargar_clientes()

ventas["Numero_Seguimiento"] = (
    ventas["Numero_Seguimiento"]
    .fillna("")
    .astype(str)
)

# ======================
# TABLA RESUMEN
# ======================

resumen = ventas.copy()

resumen["Cliente"] = ""

for i in resumen.index:

    cliente_id = resumen.loc[
        i,
        "ID_Cliente"
    ]

    cliente = clientes[
        clientes["ID_Cliente"]
        == cliente_id
    ]

    if len(
        cliente
    ) > 0:

        resumen.loc[
            i,
            "Cliente"
        ] = (
            str(
                cliente.iloc[0][
                    "Nombre"
                ]
            )
            + " "
            + str(
                cliente.iloc[0][
                    "Apellido"
                ]
            )
        )

    else:

        resumen.loc[
            i,
            "Cliente"
        ] = "Desconocido"

st.subheader(
    "📋 Pedidos"
)

st.dataframe(
    resumen[
        [
            "ID_Venta",
            "Fecha",
            "Cliente",
            "Total_Facturado",
            "Estado_Pedido"
        ]
    ].sort_values(
        by="ID_Venta",
        ascending=False
    ),
    use_container_width=True
)

st.divider()

# ======================
# BUSCADOR
# ======================

modo_busqueda = st.radio(
    "🔎 Buscar Pedido",
    [
        "Cliente",
        "ID Venta"
    ],
    horizontal=True
)

# ======================
# CLIENTE
# ======================

if modo_busqueda == "Cliente":

    telefono = st.text_input(
        "📞 Teléfono Cliente"
    )

    if telefono == "":

        st.info(
            "Ingrese un número de teléfono."
        )

        st.stop()

    cliente_fila = clientes[
        clientes[
            "Telefono"
        ]
        .astype(str)
        .str.strip()
        ==
        telefono
    ]

    if len(
        cliente_fila
    ) == 0:

        st.warning(
            "Cliente no encontrado."
        )

        st.stop()

    cliente_fila = (
        cliente_fila
        .iloc[0]
    )

    st.success(
        (
            f"👤 "
            f"{cliente_fila['Nombre']} "
            f"{cliente_fila['Apellido']}"
        )
    )

    id_cliente = cliente_fila[
        "ID_Cliente"
    ]

    ventas_cliente = ventas[
        ventas[
            "ID_Cliente"
        ]
        ==
        id_cliente
    ].copy()

    if len(
        ventas_cliente
    ) == 0:

        st.warning(
            "Este cliente no tiene pedidos."
        )

        st.stop()

    ventas_cliente[
        "Pedido_Mostrar"
    ] = ""

    for i in ventas_cliente.index:

        ventas_cliente.loc[
            i,
            "Pedido_Mostrar"
        ] = (
            f"#{ventas_cliente.loc[i,'ID_Venta']}"
            f" | "
            f"{ventas_cliente.loc[i,'Fecha']}"
            f" | "
            f"{ventas_cliente.loc[i,'Estado_Pedido']}"
            f" | "
            f"${float(ventas_cliente.loc[i,'Total_Facturado']):,.0f}"
        )

    pedido = st.selectbox(
        "📦 Pedido",
        ventas_cliente[
            "Pedido_Mostrar"
        ].tolist()
    )

    fila = ventas_cliente[
        ventas_cliente[
            "Pedido_Mostrar"
        ]
        ==
        pedido
    ].iloc[0]

# ======================
# ID VENTA
# ======================

else:

    id_venta = st.selectbox(
        "🔢 ID Venta",
        sorted(
            ventas[
                "ID_Venta"
            ].tolist(),
            reverse=True
        )
    )

    fila = ventas[
        ventas[
            "ID_Venta"
        ]
        ==
        id_venta
    ].iloc[0]

# ======================
# PRODUCTOS
# ======================

productos = []

ids = str(
    fila["ID_Producto"]
).split("|")

tamanos = str(
    fila["Tamano_Decant_ml"]
).split("|")

cantidades = str(
    fila["Cantidad"]
).split("|")

precios = str(
    fila["Precio_Total"]
).split("|")

for (
    id_producto,
    tamano,
    cantidad,
    precio
) in zip(
    ids,
    tamanos,
    cantidades,
    precios
):

    perfume = inventario[
        inventario[
            "ID_Producto"
        ]
        ==
        int(
            id_producto
        )
    ]

    if len(
        perfume
    ) > 0:

        nombre_perfume = (
            perfume.iloc[0][
                "Perfume"
            ]
        )

    else:

        nombre_perfume = (
            "Perfume desconocido"
        )

    productos.append(
        (
            f"• {nombre_perfume}"
            f" | {tamano} ml"
            f" | x{cantidad}"
            f" | ${int(float(precio)):,.0f}"
        )
    )

# ======================
# INFORMACIÓN
# ======================

st.subheader(
    "📋 Información del Pedido"
)

cliente_id = fila[
    "ID_Cliente"
]

cliente = clientes[
    clientes[
        "ID_Cliente"
    ]
    ==
    cliente_id
]

if len(
    cliente
) > 0:

    nombre_cliente = (
        str(
            cliente.iloc[0][
                "Nombre"
            ]
        )
        + " "
        + str(
            cliente.iloc[0][
                "Apellido"
            ]
        )
    )

else:

    nombre_cliente = (
        "Cliente desconocido"
    )

st.write(
    f"Cliente: {nombre_cliente}"
)

st.write(
    f"ID Cliente: {cliente_id}"
)

st.write(
    f"Fecha: {fila['Fecha']}"
)

st.write(
    f"Método Pago: {fila['Metodo_Pago']}"
)

st.write(
    f"Tipo Entrega: {fila['Tipo_Entrega']}"
)

st.divider()

# ======================
# PRODUCTOS
# ======================

st.subheader(
    "🧴 Productos"
)

for producto in productos:

    st.write(
        producto
    )

st.divider()

# ======================
# TOTALES
# ======================

col1, col2, col3 = st.columns(
    3
)

with col1:

    st.metric(
        "Productos",
        f"${float(fila['Subtotal_Productos']):,.0f}"
    )

with col2:

    st.metric(
        "Envío",
        f"${float(fila['Total_Envio']):,.0f}"
    )

with col3:

    st.metric(
        "Facturado",
        f"${float(fila['Total_Facturado']):,.0f}"
    )

st.divider()

# ======================
# ESTADO
# ======================

estado = st.selectbox(
    "Estado",
    [
        "Pendiente",
        "Preparando",
        "Enviado",
        "Entregado",
        "Cancelado"
    ],
    index=[
        "Pendiente",
        "Preparando",
        "Enviado",
        "Entregado",
        "Cancelado"
    ].index(
        fila[
            "Estado_Pedido"
        ]
    )
)

seguimiento = st.text_input(
    "Número de Seguimiento",
    value=str(
        fila[
            "Numero_Seguimiento"
        ]
    )
)

if st.button(
    "💾 Guardar Cambios",
    use_container_width=True
):

    ventas.loc[
        ventas["ID_Venta"]
        ==
        fila["ID_Venta"],
        "Estado_Pedido"
    ] = estado

    ventas.loc[
        ventas["ID_Venta"]
        ==
        fila["ID_Venta"],
        "Numero_Seguimiento"
    ] = str(
        seguimiento
    )

    guardar_ventas(
        ventas
    )

    st.success(
        "✅ Pedido actualizado correctamente"
    )

    st.rerun()