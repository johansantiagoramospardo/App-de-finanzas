from archivo_json import cargar_json, guardar_json
from datetime import date

ARCHIVO_GASTOS = "datos.json"


# =========================
# REGISTRAR GASTO
# =========================
def registrar_gasto(usuario):
    datos = cargar_json(ARCHIVO_GASTOS)

    descripcion = input("Descripción del gasto: ")
    monto = float(input("Monto: "))

    gasto = {
        "usuario": usuario,
        "fecha": str(date.today()),
        "descripcion": descripcion,
        "monto": monto
    }

    datos.append(gasto)
    guardar_json(ARCHIVO_GASTOS, datos)

    print("Gasto registrado")


# =========================
# VER GASTOS
# =========================
def ver_gastos(usuario):
    datos = cargar_json(ARCHIVO_GASTOS)

    filtrados = [g for g in datos if g["usuario"] == usuario]

    if not filtrados:
        print("No tienes gastos registrados")
        return

    print("\nTus gastos:")
    for g in filtrados:
        print(f"{g['fecha']} - {g['descripcion']} - ${g['monto']}")


# =========================
# TOTAL GASTADO
# =========================
def total_gastado(usuario):
    datos = cargar_json(ARCHIVO_GASTOS)

    total = sum(g["monto"] for g in datos if g["usuario"] == usuario)

    print(f"\nTotal gastado: ${total}")