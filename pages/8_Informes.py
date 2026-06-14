import streamlit as st
from datetime import datetime

from utils.report_generator import (
    generar_pdf_mensual
)

from utils.excel_generator import (
    generar_excel_mensual
)

st.title("📊 Informes")

st.info(
    """
Genera informes mensuales de D912 Perfumes
en formato PDF y Excel.
    """
)

# ======================
# SELECCIÓN PERÍODO
# ======================

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

col1, col2 = st.columns(2)

with col1:

    mes = st.selectbox(
        "📅 Mes",
        meses,
        index=datetime.now().month - 1
    )

with col2:

    anio = st.number_input(
        "📆 Año",
        min_value=2024,
        max_value=2100,
        value=datetime.now().year
    )

st.divider()

# ======================
# GENERACIÓN
# ======================

st.subheader(
    "📄 Generación de Informes"
)

col1, col2 = st.columns(2)

with col1:

    generar_pdf = st.button(
        "📄 Generar PDF",
        use_container_width=True
    )

with col2:

    generar_excel = st.button(
        "📊 Generar Excel",
        use_container_width=True
    )

# ======================
# GENERAR PDF
# ======================

if generar_pdf:

    ruta_pdf = generar_pdf_mensual(
        mes,
        anio
    )

    st.success(
        "✅ Informe PDF generado correctamente."
    )

    st.caption(
        ruta_pdf
    )

# ======================
# GENERAR EXCEL
# ======================

if generar_excel:

    ruta = generar_excel_mensual(
        mes,
        anio
    )

    st.success(
        f"Excel generado: {ruta}"
    )

# ======================
# CONTENIDO
# ======================

st.subheader(
    "ℹ️ Contenido del Informe"
)

st.markdown(
    """
✅ Portada con logo D912

✅ Resumen Ejecutivo

✅ Facturación Total

✅ Ventas Productos

✅ Ingresos por Envíos

✅ IVA Productos

✅ IVA Envíos

✅ IVA Total

✅ Top Clientes

✅ Top Perfumes

✅ Inventario y Stock Bajo

✅ Ventas del Mes

✅ Resumen Tributario
"""
)

st.divider()

st.info(
    f"""
📌 Período seleccionado

Mes: {mes}

Año: {anio}
"""
)