import streamlit as st
import pandas as pd
from datetime import datetime

from utils.data_manager import (
    cargar_inventario,
    cargar_precios,
    cargar_catalogo,
    guardar_inventario,
    guardar_precios,
    guardar_catalogo
)

st.title("⚙️ Administración")

inventario = cargar_inventario()
precios = cargar_precios()
catalogo = cargar_catalogo()

st.subheader("➕ Agregar Nuevo Perfume")

marca = st.text_input("Marca")

perfume = st.text_input("Perfume")

tipo_producto = st.selectbox(
    "Tipo Producto",
    [
        "Decant",
        "Frasco"
    ]
)

concentracion = st.selectbox(
    "Concentración",
    [
        "EDT",
        "EDP",
        "Parfum",
        "Extrait"
    ]
)

genero = st.selectbox(
    "Género",
    [
        "Hombre",
        "Mujer",
        "Unisex"
    ]
)

familia = st.text_input(
    "Familia Olfativa"
)

tamano_frasco = st.number_input(
    "Tamaño Frasco (ml)",
    min_value=1,
    value=100
)

stock_inicial = st.number_input(
    "Stock Inicial (ml)",
    min_value=0,
    value=0
)

stock_minimo = st.number_input(
    "Stock Mínimo (ml)",
    min_value=0,
    value=10
)

st.divider()

st.subheader("💰 Precios")

precio_2ml = st.number_input(
    "Precio 2 ml",
    min_value=0
)

precio_3ml = st.number_input(
    "Precio 3 ml",
    min_value=0
)

precio_5ml = st.number_input(
    "Precio 5 ml",
    min_value=0
)

precio_10ml = st.number_input(
    "Precio 10 ml",
    min_value=0
)

if st.button("💾 Guardar Perfume"):

    if len(
        inventario
    ) == 0:

        nuevo_id = 1

    else:

        nuevo_id = (
            int(
                inventario[
                    "ID_Producto"
                ].max()
            )
            + 1
        )

    # INVENTARIO

    nueva_fila_inventario = pd.DataFrame([
        {
            "ID_Producto": nuevo_id,
            "Marca": marca,
            "Perfume": perfume,
            "Tipo_Producto": tipo_producto,
            "Concentracion": concentracion,
            "Genero": genero,
            "Familia_Olfativa": familia,
            "Tamano_Frasco_ml": tamano_frasco,
            "Stock_Actual_ml": stock_inicial,
            "Stock_Minimo_ml": stock_minimo,
            "Costo_Neto_Compra": 0,
            "IVA_Compra": 0,
            "Costo_Total_Compra": 0,
            "Fecha_Compra": "",
            "ID_Proveedor": "",
            "Pais_Origen": "",
            "Estado": "Activo",
            "Notas": ""
        }
    ])

    inventario = pd.concat(
        [inventario, nueva_fila_inventario],
        ignore_index=True
    )

    guardar_inventario(inventario)

    # PRECIOS

    nueva_fila_precio = pd.DataFrame([
        {
            "ID_Producto": nuevo_id,
            "Precio_2ml": precio_2ml,
            "Precio_3ml": precio_3ml,
            "Precio_5ml": precio_5ml,
            "Precio_10ml": precio_10ml,
            "Fecha_Actualizacion": datetime.now().strftime("%d-%m-%Y")
        }
    ])

    precios = pd.concat(
        [precios, nueva_fila_precio],
        ignore_index=True
    )

    guardar_precios(precios)

    # CATALOGO

    nueva_fila_catalogo = pd.DataFrame([
        {
            "ID_Producto": nuevo_id,
            "Marca": marca,
            "Perfume": perfume,
            "Genero": genero,
            "Familia_Olfativa": familia,
            "Notas_Salida": "",
            "Notas_Corazon": "",
            "Notas_Fondo": "",
            "Duracion": "",
            "Proyeccion": "",
            "Estacion": "",
            "Uso": "",
            "Descripcion": "",
            "Imagen_URL": ""
        }
    ])

    catalogo = pd.concat(
        [catalogo, nueva_fila_catalogo],
        ignore_index=True
    )

    guardar_catalogo(catalogo)

    st.success(
        f"✅ Perfume agregado correctamente (ID {nuevo_id})"
    )

st.divider()

# ======================
# EDITAR PERFUME
# ======================

st.subheader("✏️ Editar Perfume")

st.caption(
    "Agregar precios sin calculo de IVA."
)

perfume_editar = st.selectbox(
    "Seleccionar Perfume",
    inventario["Perfume"].tolist()
)

fila = inventario[
    inventario["Perfume"] == perfume_editar
].iloc[0]

id_producto = fila["ID_Producto"]

marca_edit = st.text_input(
    "Marca",
    value=fila["Marca"],
    key="edit_marca"
)

familia_edit = st.text_input(
    "Familia Olfativa",
    value=fila["Familia_Olfativa"],
    key="edit_familia"
)

stock_minimo_edit = st.number_input(
    "Stock Mínimo",
    min_value=0,
    value=int(fila["Stock_Minimo_ml"]),
    key="edit_stock"
)

estado_edit = st.selectbox(
    "Estado",
    ["Activo", "Inactivo"],
    index=0 if fila["Estado"] == "Activo" else 1,
    key="edit_estado"
)

fila_precio = precios[
    precios["ID_Producto"] == id_producto
].iloc[0]

precio2 = st.number_input(
    "Precio 2 ml",
    value=int(fila_precio["Precio_2ml"]),
    key="p2"
)

precio3 = st.number_input(
    "Precio 3 ml",
    value=int(fila_precio["Precio_3ml"]),
    key="p3"
)

precio5 = st.number_input(
    "Precio 5 ml",
    value=int(fila_precio["Precio_5ml"]),
    key="p5"
)

precio10 = st.number_input(
    "Precio 10 ml",
    value=int(fila_precio["Precio_10ml"]),
    key="p10"
)

if st.button("💾 Guardar Cambios"):

    inventario.loc[
        inventario["ID_Producto"] == id_producto,
        "Marca"
    ] = marca_edit

    inventario.loc[
        inventario["ID_Producto"] == id_producto,
        "Familia_Olfativa"
    ] = familia_edit

    inventario.loc[
        inventario["ID_Producto"] == id_producto,
        "Stock_Minimo_ml"
    ] = stock_minimo_edit

    inventario.loc[
        inventario["ID_Producto"] == id_producto,
        "Estado"
    ] = estado_edit

    guardar_inventario(inventario)

    precios.loc[
        precios["ID_Producto"] == id_producto,
        "Precio_2ml"
    ] = precio2

    precios.loc[
        precios["ID_Producto"] == id_producto,
        "Precio_3ml"
    ] = precio3

    precios.loc[
        precios["ID_Producto"] == id_producto,
        "Precio_5ml"
    ] = precio5

    precios.loc[
        precios["ID_Producto"] == id_producto,
        "Precio_10ml"
    ] = precio10

    guardar_precios(precios)

    st.success(
        "✅ Perfume actualizado correctamente"
    )