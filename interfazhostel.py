import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
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

    def add_reservation(self, nombre, check_in, check_out, cantidad_pasajeros, numero_habitacion, monto_por_persona_str, descripcion, deposito_pagado_str):
        monto_por_persona = self.convert_to_number(monto_por_persona_str)
        monto_total = monto_por_persona * cantidad_pasajeros
        deposito_pagado = deposito_pagado_str.lower() == "sí"

        if self.is_room_available(numero_habitacion, check_in, check_out):
            reservation = Reservation(nombre, check_in, check_out, cantidad_pasajeros, numero_habitacion, monto_total, descripcion, deposito_pagado)
            self.reservations.append(reservation)
            return True
        else:
            return False

    def view_reservations(self):
        return self.reservations

    def delete_reservation(self, index):
        if 0 <= index < len(self.reservations):
            removed = self.reservations.pop(index)
            return removed
        else:
            return None

    def update_description(self, index, descripcion):
        if 0 <= index < len(self.reservations):
            self.reservations[index].descripcion = descripcion
            return True
        else:
            return False

class HostelApp:
    def __init__(self, root, hostel):
        self.root = root
        self.hostel = hostel
        self.root.title("Gestión de Reservas del Hostel")

        self.add_reservation_button = tk.Button(root, text="Añadir Reserva", command=self.add_reservation)
        self.add_reservation_button.pack()

        self.view_reservations_button = tk.Button(root, text="Ver Reservas", command=self.view_reservations)
        self.view_reservations_button.pack()

        self.update_description_button = tk.Button(root, text="Actualizar Descripción de Reserva", command=self.update_description)
        self.update_description_button.pack()

        self.delete_reservation_button = tk.Button(root, text="Eliminar Reserva", command=self.delete_reservation)
        self.delete_reservation_button.pack()

    def add_reservation(self):
        nombre = simpledialog.askstring("Nombre del huésped", "Nombre del huésped:")
        check_in = simpledialog.askstring("Fecha de entrada", "Fecha de entrada (YYYY-MM-DD):")
        check_out = simpledialog.askstring("Fecha de salida", "Fecha de salida (YYYY-MM-DD):")
        cantidad_pasajeros = simpledialog.askinteger("Cantidad de personas", "Cantidad de personas:")
        numero_habitacion = simpledialog.askstring("Número de habitación", "Número de habitación:")
        monto_por_persona_str = simpledialog.askstring("Monto por persona", "Monto por persona por noche (puede usar 'mil', 'k', etc.):")
        descripcion = simpledialog.askstring("Descripción", "Ingrese una descripción (opcional, por ejemplo, 'Seña dejada', 'Debe abonar', etc.):")
        deposito_pagado_str = simpledialog.askstring("Depósito pagado", "¿Se ha pagado el depósito? (sí/no):")

        if nombre and check_in and check_out and cantidad_pasajeros and numero_habitacion and monto_por_persona_str:
            if self.hostel.add_reservation(nombre, check_in, check_out, cantidad_pasajeros, numero_habitacion, monto_por_persona_str, descripcion, deposito_pagado_str):
                messagebox.showinfo("Éxito", f"Reserva añadida: {nombre} - Habitación: {numero_habitacion}")
            else:
                messagebox.showerror("Error", f"La habitación {numero_habitacion} ya está reservada para las fechas seleccionadas.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos requeridos.")

    def view_reservations(self):
        reservations = self.hostel.view_reservations()
        if not reservations:
            messagebox.showinfo("Reservas", "No hay reservas.")
        else:
            reservation_list = "\n".join([f"{idx + 1}. {r.nombre} - Entrada: {r.check_in}, Salida: {r.check_out}, Personas: {r.cantidad_pasajeros}, Habitación: {r.numero_habitacion}, Monto Total: {self.hostel.convert_to_readable(r.monto_total)}, Descripción: {r.descripcion}, Depósito Pagado: {'Sí' if r.deposito_pagado else 'No'}" for idx, r in enumerate(reservations)])
            messagebox.showinfo("Reservas", reservation_list)

    def delete_reservation(self):
        index = simpledialog.askinteger("Número de reserva", "Número de la reserva a eliminar:") - 1
        removed = self.hostel.delete_reservation(index)
        if removed:
            messagebox.showinfo("Éxito", f"Reserva eliminada: {removed.nombre} - Habitación: {removed.numero_habitacion}")
        else:
            messagebox.showerror("Error", "Índice inválido.")

    def update_description(self):
        index = simpledialog.askinteger("Número de reserva", "Número de la reserva a actualizar:") - 1
        descripcion = simpledialog.askstring("Descripción", "Ingrese la nueva descripción:")
        if self.hostel.update_description(index, descripcion):
            messagebox.showinfo("Éxito", f"Descripción actualizada para la reserva {index + 1}.")
        else:
            messagebox.showerror("Error", "Índice inválido.")

if __name__ == "__main__":
    root = tk.Tk()
    hostel = HostelReservation()
    app = HostelApp(root, hostel)
    root.mainloop()
