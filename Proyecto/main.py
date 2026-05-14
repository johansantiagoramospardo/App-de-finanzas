from usuarios import registrar_usuario, iniciar_sesion
from gastos import registrar_gasto, ver_gastos, total_gastado


# =========================
# MENÚ DE GASTOS
# =========================
def menu_finanzas(usuario):

    while True:
        print("\n===== APP FINANZAS =====")
        print("1. Registrar gasto")
        print("2. Ver gastos")
        print("3. Ver total gastado")
        print("4. Cerrar sesión")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_gasto(usuario)

        elif opcion == "2":
            ver_gastos(usuario)

        elif opcion == "3":
            total_gastado(usuario)

        elif opcion == "4":
            print("Cerrando sesión...")
            break

        else:
            print("Opción inválida")


# =========================
# MENÚ PRINCIPAL (LOGIN)
# =========================
def main():

    while True:
        print("\n===== BIENVENIDO A LA APP =====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elige: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            usuario = iniciar_sesion()

            if usuario:
                menu_finanzas(usuario)

        elif opcion == "3":
            print("Adiós")
            break

        else:
            print("Opción inválida")

# EJECUCIÓN DEL PROGRAMA
main()
