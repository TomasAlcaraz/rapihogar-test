class TrabajoPedido:
    def __init__(self, title, description):
        self.title = title
        self.description = description

# Crear objetos de trabajo con títulos y descripciones
trabajo1 = TrabajoPedido("Desarrollo de aplicación web", "Desarrollar una aplicación web utilizando Django y React.")
trabajo2 = TrabajoPedido("Resolución de problemas de red", "Diagnosticar y resolver problemas de conectividad en la red de la oficina.")
trabajo3 = TrabajoPedido("Configuración de servidor", "Configurar un servidor Linux para hosting de aplicaciones.")
trabajo4 = TrabajoPedido("Mantenimiento de base de datos", "Realizar tareas de mantenimiento en la base de datos, incluyendo optimización y respaldos regulares.")
trabajo5 = TrabajoPedido("Desarrollo de aplicación móvil", "Crear una aplicación móvil nativa para iOS y Android utilizando Flutter.")
trabajo6 = TrabajoPedido("Instalación de software de seguridad", "Configurar y instalar software de seguridad en los sistemas para proteger contra amenazas cibernéticas.")
trabajo7 = TrabajoPedido("Actualización de sistema operativo", "Actualizar el sistema operativo de los servidores a la última versión estable.")
trabajo8 = TrabajoPedido("Optimización de rendimiento", "Identificar y mejorar el rendimiento de una aplicación existente, incluyendo la reducción de tiempos de carga.")

# Crear una lista de trabajos
pedidos_list = [trabajo1, trabajo2, trabajo3, trabajo4, trabajo5, trabajo6, trabajo7, trabajo8]