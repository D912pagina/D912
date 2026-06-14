import streamlit as st

from utils.data_manager import (
    cargar_inventario,
    cargar_precios,
    cargar_clientes
)

from utils.sales_manager import (
    obtener_precio,
    calcular_total,
    registrar_venta
)

from utils.pricing import (
    precio_venta,
    iva_cobrado
)

st.title("🛒 Ventas")

# ======================
# CARGAR DATOS
# ======================

inventario = cargar_inventario()
precios = cargar_precios()
clientes = cargar_clientes()

if len(clientes) == 0:

    st.warning(
        "No existen clientes registrados."
    )

    st.stop()

clientes["Cliente_Mostrar"] = (
    "ID "
    + clientes["ID_Cliente"]
    .astype(str)
    + " | "
    + clientes["Telefono"]
    .astype(str)
    + " | "
    + clientes["Nombre"]
    .fillna("")
    + " "
    + clientes["Apellido"]
    .fillna("")
) 
# ======================
# CLIENTE
# ======================

clientes["Cliente_Mostrar"] = (

    "ID "
    + clientes["ID_Cliente"]
    .astype(str)
    + " | "
    + clientes["Telefono"]
    .astype(str)
    + " | "
    + clientes["Nombre"]
    .fillna("")
    + " "
    + clientes["Apellido"]
    .fillna("")
)

cliente = st.selectbox(
    "🔎 Buscar Cliente",
    clientes["Cliente_Mostrar"].tolist(),
    index=None,
    placeholder="Escribe ID, teléfono o nombre..."
)

if cliente:

    cliente_seleccionado = clientes[
        clientes["Cliente_Mostrar"]
        == cliente
    ].iloc[0]

    id_cliente = cliente_seleccionado[
        "ID_Cliente"
    ]

    st.caption(
        f"📍 {cliente_seleccionado['Ciudad']}"
    )

else:

    st.info(
        "Selecciona un cliente para continuar."
    )

    st.stop()

# ======================
# MÉTODO DE PAGO
# ======================

metodo_pago = st.selectbox(
    "Método de Pago",
    [
        "Transferencia",
        "Mercadopago",
        "Efectivo"
    ]
)

# ======================
# TIPO DE ENTREGA
# ======================

tipo_entrega = st.radio(
    "🚚 Método de entrega",
    [
        "Región Metropolitana ($3.100)",
        "Otras regiones ($4.300)",
        "Zonas extremas ($5.200)",
        "Personalizado"
    ]
)

if tipo_entrega == "Región Metropolitana ($3.100)":

    costo_envio = 2605

    iva_envio = round(
        costo_envio * 0.19
    )

    total_envio = (
        costo_envio
        + iva_envio
    )

elif tipo_entrega == "Otras regiones ($4.300)":

    costo_envio = 3613

    iva_envio = round(
        costo_envio * 0.19
    )

    total_envio = (
        costo_envio
        + iva_envio
    )

elif tipo_entrega == "Zonas extremas ($5.200)":

    costo_envio = 4370

    iva_envio = round(
        costo_envio * 0.19
    )

    total_envio = (
        costo_envio
        + iva_envio
    )

else:

    costo_envio = st.number_input(
        "Costo envío",
        min_value=0,
        step=100
    )

    iva_envio = st.number_input(
        "IVA envío",
        min_value=0,
        step=100
    )

    total_envio = (
        costo_envio
        + iva_envio
    )


# ======================
# OBSERVACIONES
# ======================

observaciones = st.text_area(
    "Observaciones"
)

st.divider()

# ======================
# CARRITO ADMINISTRATIVO
# ======================

if "pedido_actual" not in st.session_state:

    st.session_state.pedido_actual = []

# ======================
# PERFUME
# ======================

producto = st.selectbox(
    "Perfume",
    inventario["Perfume"].tolist()
)

# ======================
# TAMAÑO
# ======================

tamano = st.selectbox(
    "Tamaño (ml)",
    [2, 3, 5, 10]
)

# ======================
# CANTIDAD
# ======================

cantidad = st.number_input(
    "Cantidad",
    min_value=1,
    value=1
)

# ======================
# OBTENER ID PRODUCTO
# ======================

id_producto = inventario.loc[
    inventario["Perfume"] == producto,
    "ID_Producto"
].iloc[0]

# ======================
# PRECIO
# ======================

precio_unitario = obtener_precio(
    precios,
    id_producto,
    tamano
)


# ======================
# IVA
# ======================

precio_unitario_final = precio_venta(
    precio_unitario
)

iva_unitario = round(
    precio_unitario * 0.19
)

# ======================
# TOTAL PRODUCTO
# ======================

precio_neto_producto = (
    precio_unitario
    * cantidad
)

iva_producto = (
    iva_unitario
    * cantidad
)

precio_total_producto = (
    precio_unitario_final
    * cantidad
)

# ======================
# STOCK
# ======================

ml_necesarios = tamano * cantidad

stock_actual = inventario.loc[
    inventario["ID_Producto"] == id_producto,
    "Stock_Actual_ml"
].iloc[0]

st.info(
    f"📦 Stock disponible: {stock_actual} ml"
)

if ml_necesarios > stock_actual:

    st.error(
        "❌ Stock insuficiente para agregar al pedido."
    )

else:

    st.success(
        f"✅ Stock suficiente ({ml_necesarios} ml requeridos)"
    )

# ======================
# PREVISUALIZACIÓN
# ======================

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Precio Unitario",
        f"${precio_unitario_final:,.0f}"
    )

with col2:

    st.metric(
        "Total Producto",
        f"${precio_total_producto:,.0f}"
    )

# ======================
# AGREGAR AL PEDIDO
# ======================

if ml_necesarios <= stock_actual:

    if st.button(
        "➕ Agregar al Pedido"
    ):

        st.session_state.pedido_actual.append(
            {
                "ID_Producto": id_producto,
                "Perfume": producto,
                "Tamano": tamano,
                "Cantidad": cantidad,
                "Precio_Neto": precio_neto_producto,
                "IVA": iva_producto,
                "Precio_Total": precio_total_producto
            }
        )

        st.rerun()

st.divider()

# ======================
# PEDIDO ACTUAL
# ======================

st.subheader(
    "🛒 Pedido Actual"
)

subtotal_neto = 0
subtotal_iva = 0
subtotal_productos = 0

for i, item in enumerate(
    st.session_state.pedido_actual
):

    subtotal_neto += item[
        "Precio_Neto"
    ]

    subtotal_iva += item[
        "IVA"
    ]

    subtotal_productos += item[
        "Precio_Total"
    ]

    col1, col2 = st.columns(
        [8, 1]
    )

    with col1:

        st.write(
            f"• {item['Perfume']} | "
            f"{item['Tamano']} ml | "
            f"x{item['Cantidad']} | "
            f"${item['Precio_Total']:,.0f}"
        )

    with col2:

        if st.button(
            "❌",
            key=f"pedido_{i}"
        ):

            st.session_state.pedido_actual.pop(
                i
            )

            st.rerun()

# ======================
# TOTALES PEDIDO
# ======================

total_facturado = (
    subtotal_productos
    + total_envio
)

st.info(
    f"""
🧾 Subtotal Neto: ${subtotal_neto:,.0f}

🧾 Subtotal IVA: ${subtotal_iva:,.0f}

🧴 Subtotal Productos: ${subtotal_productos:,.0f}

🚚 Total envío: ${total_envio:,.0f}

💰 Total facturado: ${total_facturado:,.0f}
"""
)

# ======================
# REGISTRAR PEDIDO
# ======================

if len(
    st.session_state.pedido_actual
) > 0:

    if st.button(
        "💾 Registrar Pedido"
    ):

        id_productos = []
        tamanos = []
        cantidades = []

        precios_netos = []
        ivas = []
        precios_totales = []

        for item in (
            st.session_state.pedido_actual
        ):

            id_productos.append(
                str(
                    item["ID_Producto"]
                )
            )

            tamanos.append(
                str(
                    item["Tamano"]
                )
            )

            cantidades.append(
                str(
                    item["Cantidad"]
                )
            )

            precios_netos.append(
                str(
                    int(
                        item["Precio_Neto"]
                    )
                )
            )

            ivas.append(
                str(
                    int(
                        item["IVA"]
                    )
                )
            )

            precios_totales.append(
                str(
                    int(
                        item["Precio_Total"]
                    )
                )
            )

        id_venta = registrar_venta(
            clientes=clientes,
            inventario=inventario,
            id_cliente=id_cliente,

            id_productos=id_productos,
            tamanos=tamanos,
            cantidades=cantidades,

            precios_netos=precios_netos,
            ivas=ivas,
            precios_totales=precios_totales,

            subtotal_neto=subtotal_neto,
            subtotal_iva=subtotal_iva,
            subtotal_productos=subtotal_productos,

            metodo_pago=metodo_pago,
            observaciones=observaciones,

            costo_envio=costo_envio,
            iva_envio=iva_envio,
            total_envio=total_envio,

            total_facturado=total_facturado,

            tipo_entrega=tipo_entrega
        )

        st.session_state.pedido_actual = []

        st.success(
            f"✅ Pedido #{id_venta} registrado correctamente"
        )

        st.rerun()