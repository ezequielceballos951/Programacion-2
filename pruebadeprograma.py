class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un nuevo producto con su nombre, precio y cantidad.
        
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        
        :return: Una cadena con la información del producto.
        """
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        """
        Inicializa un nuevo producto electrónico con atributos específicos.
        
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        :param marca: Marca del producto electrónico.
        :param modelo: Modelo del producto electrónico.
        """
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        """
        Muestra la información completa del producto electrónico.
        
        :return: Una cadena con la información completa del producto electrónico.
        """
        info_producto = super().mostrar_informacion()
        return f"{info_producto}, Marca: {self.marca}, Modelo: {self.modelo}"

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        """
        Inicializa un nuevo producto alimenticio con atributos específicos.
        
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        :param fecha_expiracion: Fecha de expiración del producto alimenticio.
        """
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        """
        Muestra la información completa del producto alimenticio.
        
        :return: Una cadena con la información completa del producto alimenticio.
        """
        info_producto = super().mostrar_informacion()
        return f"{info_producto}, Fecha de Expiración: {self.fecha_expiracion}"

# Crear instancias de cada clase hija
producto_electronico = Electronico("Laptop", 1500.00, 10, "Dell", "XPS 15")
producto_alimento = Alimento("Manzana", 0.50, 100, "2024-12-31")

# Mostrar información de cada producto
print(producto_electronico.mostrar_informacion())
print(producto_alimento.mostrar_informacion())
