import re

class Reservation:
    def __init__(self, nombre, check_in, check_out, cantidad_pasajeros, numero_habitacion, monto_total, descripcion="", deposito_pagado=False):
        self.nombre = nombre
        self.check_in = check_in
        self.check_out = check_out
        self.cantidad_pasajeros = cantidad_pasajeros
        self.numero_habitacion = numero_habitacion
        self.monto_total = monto_total
        self.descripcion = descripcion
        self.deposito_pagado = deposito_pagado

class HostelReservation:
    def __init__(self):
        self.reservations = []

    def is_room_available(self, numero_habitacion, check_in, check_out):
        for reservation in self.reservations:
            if reservation.numero_habitacion == numero_habitacion:
                if not (check_out <= reservation.check_in or check_in >= reservation.check_out):
                    return False
        return True

    def convert_to_number(self, amount_str):
        amount_str = amount_str.lower().replace(' ', '')
        number = ''
        units = {'mil': '000', 'm': '000', 'k': '000'}
        parts = re.split('(\d+)', amount_str)
        for part in parts:
            if part.isdigit():
                number += part
            elif part in units:
                number += units[part]
        return int(number)

    def convert_to_readable(self, amount):
        if amount >= 1000:
            return f"{amount // 1000}mil"
        return str(amount)

    def add_reservation(self):
        nombre = input("Nombre del huésped: ")
        check_in = input("Fecha de entrada (YYYY-MM-DD): ")
        check_out = input("Fecha de salida (YYYY-MM-DD): ")
        cantidad_pasajeros = int(input("Cantidad de personas: "))
        numero_habitacion = input("Número de habitación: ")
        monto_por_persona_str = input("Monto por persona por noche (puede usar 'mil', 'k', etc.): ")
        monto_por_persona = self.convert_to_number(monto_por_persona_str)
        monto_total = monto_por_persona * cantidad_pasajeros
        descripcion = input("Ingrese una descripción (opcional, por ejemplo, 'Seña dejada', 'Debe abonar', etc.): ")
        deposito_pagado_str = input("¿Se ha pagado el depósito? (sí/no): ").strip().lower()
        deposito_pagado = deposito_pagado_str == "sí"

        if self.is_room_available(numero_habitacion, check_in, check_out):
            reservation = Reservation(nombre, check_in, check_out, cantidad_pasajeros, numero_habitacion, monto_total, descripcion, deposito_pagado)
            self.reservations.append(reservation)
            print(f"Reserva añadida: {nombre} - Habitación: {numero_habitacion}")
        else:
            print(f"La habitación {numero_habitacion} ya está reservada para las fechas seleccionadas.")

    def view_reservations(self):
        if not self.reservations:
            print("No hay reservas.")
        else:
            for idx, reservation in enumerate(self.reservations):
                monto_total_readable = self.convert_to_readable(reservation.monto_total)
                deposito_pagado_str = "Sí" if reservation.deposito_pagado else "No"
                print(f"{idx + 1}. {reservation.nombre} - Entrada: {reservation.check_in}, Salida: {reservation.check_out}, Personas: {reservation.cantidad_pasajeros}, Habitación: {reservation.numero_habitacion}, Monto Total: {monto_total_readable}, Descripción: {reservation.descripcion}, Depósito Pagado: {deposito_pagado_str}")

    def delete_reservation(self, index):
        if 0 <= index < len(self.reservations):
            removed = self.reservations.pop(index)
            print(f"Reserva eliminada: {removed.nombre} - Habitación: {removed.numero_habitacion}")
        else:
            print("Índice inválido.")

    def update_description(self, index, descripcion):
        if 0 <= index < len(self.reservations):
            self.reservations[index].descripcion = descripcion
            print(f"Descripción actualizada para la reserva {index + 1}.")
        else:
            print("Índice inválido.")

def main():
    hostel = HostelReservation()
    
    while True:
        print("\nGestión de Reservas del Hostel")
        print("1. Añadir Reserva")
        print("2. Ver Reservas")
        print("3. Actualizar Descripción de Reserva")
        print("4. Eliminar Reserva")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            hostel.add_reservation()
        
        elif choice == '2':
            hostel.view_reservations()
        
        elif choice == '3':
            index = int(input("Número de la reserva a actualizar: ")) - 1
            descripcion = input("Ingrese la nueva descripción: ")
            hostel.update_description(index, descripcion)
        
        elif choice == '4':
            index = int(input("Número de la reserva a eliminar: ")) - 1
            hostel.delete_reservation(index)
        
        elif choice == '5':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

