# models/factura.py

from datetime import datetime

class Factura:
    def __init__(self, orden_pago):
        self.__orden_pago = orden_pago
        self.__fecha_emision = datetime.now()
        self.__pagada = False

    def pagar(self):
        self.__pagada = True

    def esta_pagada(self) -> bool:
        return self.__pagada

    def mostrar_factura(self) -> str:
        estado = "Pagada" if self.__pagada else "Pendiente"
        detalle = f"FACTURA - Fecha: {self.__fecha_emision.strftime('%d/%m/%Y %H:%M')} - Estado: {estado}\n"
        detalle += self.__orden_pago.mostrar_detalle()
        return detalle
