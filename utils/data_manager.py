from pathlib import Path

import pandas as pd
import streamlit as st

import gspread
from gspread_dataframe import set_with_dataframe

# ======================
# RUTAS
# ======================

BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

DATA_DIR = (
    BASE_DIR
    / "data"
)

gc = gspread.service_account_from_dict(
    st.secrets["gcp_service_account"]
)

sheet_db = gc.open(
    "D912 Database"
)

# ======================
# CARGAR
# ======================

@st.cache_data
def cargar_inventario():

    hoja = sheet_db.worksheet(
        "Inventario"
    )

    return pd.DataFrame(
        hoja.get_all_records()
    )

@st.cache_data
def cargar_clientes():

    hoja = sheet_db.worksheet(
        "Clientes"
    )

    datos = hoja.get_all_values()

    if len(datos) == 0:

        return pd.DataFrame()

    if len(datos) == 1:

        return pd.DataFrame(
            columns=datos[0]
        )

    return pd.DataFrame(
        datos[1:],
        columns=datos[0]
    )



@st.cache_data
def cargar_ventas():

    hoja = sheet_db.worksheet(
        "Ventas"
    )

    datos = hoja.get_all_values()

    if len(datos) == 0:

        return pd.DataFrame()

    if len(datos) == 1:

        return pd.DataFrame(
            columns=datos[0]
        )

    ventas = pd.DataFrame(
        datos[1:],
        columns=datos[0]
    )

    if "Numero_Seguimiento" in ventas.columns:

        ventas["Numero_Seguimiento"] = (
            ventas["Numero_Seguimiento"]
            .fillna("")
            .astype(str)
        )

    return ventas

@st.cache_data
def cargar_precios():

    hoja = sheet_db.worksheet(
        "Precios"
    )

    return pd.DataFrame(
        hoja.get_all_records()
    )


@st.cache_data
def cargar_catalogo():

    hoja = sheet_db.worksheet(
        "Catalogo_Perfumes"
    )

    return pd.DataFrame(
        hoja.get_all_records()
    )

# ======================
# GUARDAR
# ======================

def guardar_ventas(
    df
):

    hoja = sheet_db.worksheet(
        "Ventas"
    )

    hoja.clear()

    from gspread_dataframe import (
        set_with_dataframe
    )

    set_with_dataframe(
        hoja,
        df
    )

    cargar_ventas.clear()

def guardar_inventario(
    df
):

    hoja = sheet_db.worksheet(
        "Inventario"
    )

    hoja.clear()

    from gspread_dataframe import (
        set_with_dataframe
    )

    set_with_dataframe(
        hoja,
        df
    )

    cargar_inventario.clear()


def guardar_clientes(
    df
):

    df["Telefono"] = (
        df["Telefono"]
        .astype(str)
    )

    hoja = sheet_db.worksheet(
        "Clientes"
    )

    hoja.clear()

    set_with_dataframe(
        hoja,
        df
    )

    cargar_clientes.clear()


def guardar_precios(
    df
):

    hoja = sheet_db.worksheet(
        "Precios"
    )

    hoja.clear()

    set_with_dataframe(
        hoja,
        df
    )

    cargar_precios.clear()


def guardar_catalogo(
    df
):

    hoja = sheet_db.worksheet(
        "Catalogo_Perfumes"
    )

    hoja.clear()

    set_with_dataframe(
        hoja,
        df
    )

    cargar_catalogo.clear()