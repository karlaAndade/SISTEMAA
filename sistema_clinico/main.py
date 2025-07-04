from datetime import datetime, date

# Modelos
from models.paciente import Paciente
from models.medico import Medico
from models.laboratorista import Laboratorista
from models.usuario_sistema import UsuarioSistema
from models.examen import Examen

# Servicios
from services.autenticacion import ServicioAutenticacion
from services.gestion_citas import ServicioCitas
from services.gestion_reportes import ServicioReportes

# =============================
# 1. Crear usuarios y personas
# =============================

print("== Sistema Clínico Iniciado ==")

# Crear paciente, médico, laboratorista
paciente1 = Paciente("Ana", "Martínez", "12345678", "321654987", date(1995, 6, 1), "F", "Calle Falsa 123")

#paciente1 = Paciente("Ana", "Martínez", "12345678", "321654987",
                     #, "F", "Calle Falsa 123")

medico1 = Medico("Carlos", "Ramírez", "98765432", "314789654", "MED001", "Cardiología")
laboratorista1 = Laboratorista("Luis", "Gómez", "74125896", "300741258", "LAB123", "Noche")

# Crear usuario del sistema para el paciente
usuario_paciente = UsuarioSistema("ana123", "pass123", paciente1)

# =============================
# 2. Registrar y autenticar usuario
# =============================

auth_service = ServicioAutenticacion()
auth_service.registrar_usuario(usuario_paciente)

usuario_autenticado = auth_service.autenticar("ana123", "pass123")

if usuario_autenticado:
    print(f"[✓] Usuario autenticado: {usuario_autenticado.get_persona().mostrar_info()}")
else:
    print("[X] Autenticación fallida")
    exit()

# =============================
# 3. Agendar una cita médica
# =============================

gestion_citas = ServicioCitas()
fecha_cita = datetime(2025, 6, 10, 9, 30)

cita1 = gestion_citas.agendar_cita(paciente1, medico1, fecha_cita, "Dolor en el pecho")
print(f"\n[✓] Cita agendada:\n{cita1.mostrar_detalle()}")

# =============================
# 4. Registrar examen y resultado
# =============================

# Crear un examen clínico
examen1 = Examen("Colesterol", "mg/dL", 120, 200, 45.50)

# El laboratorista registra un resultado
resultado1 = laboratorista1.registrar_resultado(examen1, 210)  # Valor fuera del rango

print("\n[✓] Resultado registrado:")
print(resultado1.mostrar_detalle())

# =============================
# 5. Generar reporte médico y firmarlo
# =============================

gestion_reportes = ServicioReportes()
reporte1 = gestion_reportes.generar_reporte(paciente1, medico1)
reporte1.agregar_resultado(resultado1)

# El médico firma el reporte
medico1.firmar_reporte(reporte1)

print("\n[✓] Reporte generado:")
print(reporte1.mostrar_resumen())

# =============================
# 6. Generar orden de pago y factura
# =============================

from models.orden_pago import OrdenPago
from models.factura import Factura

orden_pago = OrdenPago(paciente1)
orden_pago.agregar_examen(examen1)

factura = Factura(orden_pago)
print("\n[✓] Factura generada (sin pagar):")
print(factura.mostrar_factura())

# Pagar factura
factura.pagar()
print("\n[✓] Factura después del pago:")
print(factura.mostrar_factura())

print("\n== Fin del proceso clínico ==")
