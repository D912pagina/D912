from datetime import datetime
import pandas as pd

from utils.data_manager import (
    cargar_ventas,
    guardar_ventas,
    guardar_inventario,
    guardar_clientes
)


def obtener_precio(precios, id_producto, tamano):
    fila_precio = precios[
        precios["ID_Producto"] == id_producto
    ]

    return fila_precio[
        f"Precio_{tamano}ml"
    ].iloc[0]


def calcular_total(precio_unitario, cantidad):
    return precio_unitario * cantidad


def calcular_iva(total):
    return round(total * 0.19)


def calcular_neto(total):
    return total - calcular_iva(total)


def generar_id_venta(ventas):

    if len(ventas) == 0:
        return 1

    return int(
        ventas["ID_Venta"].max()
    ) + 1


def registrar_venta(
    clientes,
    inventario,
    id_cliente,
    id_productos,
    tamanos,
    cantidades,
    precios_netos,
    ivas,
    precios_totales,
    subtotal_neto,
    subtotal_iva,
    subtotal_productos,
    metodo_pago,
    observaciones,
    costo_envio,
    iva_envio,
    total_envio,
    total_facturado,
    tipo_entrega
):

    ventas = cargar_ventas()

    nuevo_id = generar_id_venta(
        ventas
    )

    fecha_actual = str(
        datetime.now().strftime(
            "%d-%m-%Y"
        )
    )

    nueva_venta = pd.DataFrame([
        {
            "ID_Venta": nuevo_id,
            "Fecha": fecha_actual,
            "ID_Cliente": id_cliente,

            "ID_Producto": "|".join(
                id_productos
            ),

            "Tamano_Decant_ml": "|".join(
                tamanos
            ),

            "Cantidad": "|".join(
                cantidades
            ),

            "Precio_Neto": "|".join(
                precios_netos
            ),

            "IVA": "|".join(
                ivas
            ),

            "Precio_Total": "|".join(
                precios_totales
            ),

            "Subtotal_Neto": int(
                subtotal_neto
            ),

            "Subtotal_IVA": int(
                subtotal_iva
            ),

            "Subtotal_Productos": int(
                subtotal_productos
            ),

            "Costo_Envio": costo_envio,

            "IVA_Envio": iva_envio,

            "Total_Envio": total_envio,

            "Total_Facturado": total_facturado,

            "Tipo_Entrega": tipo_entrega,

            "Metodo_Pago": metodo_pago,

            "Estado_Pedido": "Pendiente",

            "Numero_Seguimiento": "",

            "Observaciones": observaciones
        }
    ])

    ventas = pd.concat(
        [
            ventas,
            nueva_venta
        ],
        ignore_index=True
    )

    guardar_ventas(
        ventas
    )

    # ======================
    # DESCONTAR STOCK
    # ======================

    for i in range(
        len(id_productos)
    ):

        id_producto = int(
            id_productos[i]
        )

        tamano = int(
            tamanos[i]
        )

        cantidad = int(
            cantidades[i]
        )

        ml_descontar = (
            tamano
            * cantidad
        )

        inventario.loc[
            inventario["ID_Producto"]
            == id_producto,
            "Stock_Actual_ml"
        ] -= ml_descontar

    print(inventario.dtypes)

    guardar_inventario(
        inventario
    )

    # ======================
    # CLIENTE
    # ======================

    indice = clientes[
        clientes["ID_Cliente"]
        == str(id_cliente)
    ].index[0]

    clientes.at[
        indice,
        "Ultima_Compra"
    ] = fecha_actual

    print(clientes.dtypes)
    print(clientes.head())

    indice = clientes[
        clientes["ID_Cliente"]
        == str(id_cliente)
    ].index[0]

    clientes.loc[
        indice,
        "Total_Compras"
    ] = str(
        int(
            clientes.loc[
                indice,
                "Total_Compras"
            ]
        )
        + int(
            total_facturado
        )
    )

    if "Total_Pedidos" in clientes.columns:

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

    return nuevo_id