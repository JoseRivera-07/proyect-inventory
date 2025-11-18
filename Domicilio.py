# Programa que ejecuta el pedido de un domicilio

# Función que imprime la carta
def carta(menu, precios_menu):
    global select
    select = 0
    for producto in menu:
        print(f"{menu[select]}: ${precios_menu[select]}")
        select += 1


# Función que ejecuta el pago
def pagar():
    global select, precio_carrito, precios_menu, metodos_pago

    metodo_pago = input(f"Estos son los metodos de pago que tenemos: {metodos_pago}. ¿Cuál vas a utilizar? Digite el número al que corresponda: ")

    if metodo_pago == "1":
        print("El total de tu compra es de: $", precio_carrito)
        eleccion = input("¿Necesitas devuelta? Digite 1 para sí, 2 para no: ")
        if eleccion == "1":
            pago = int(input("¿De cuánto?: "))
            devuelta = pago - precio_carrito
            if devuelta < 0:
                print("El dinero no es suficiente para cubrir el total.")
                return
            print("El pedido se ha pagado exitosamente, se le entregará una devuelta de: $", devuelta)
        else:
            print("El pedido se ha pagado exitosamente.")
    elif metodo_pago == "2":
        tarjeta = input("Ingrese los dígitos de su tarjeta de crédito en cuartetos. Ej: XXXX XXXX XXXX XXXX: ")
        print("El pedido se ha pagado exitosamente.")

    print("Tu pedido está en preparación y te llegará próximamente a domicilio.")


# Función que toma el pedido
def tomarPedido():
    global precio_carrito
    continuar = "1"
    while continuar == "1":
        id_producto_elegido = int(input("Digita el número de producto: "))
        id_producto_elegido = id_producto_elegido - 1  # ajustar índice
        carrito_prod.append(menu[id_producto_elegido])
        precio_carrito += precios_menu[id_producto_elegido]
        print("Tu pedido fue tomado exitosamente:", menu[id_producto_elegido])
        continuar = input("¿Deseas agregar otro producto? Digita 1 para sí, 2 para no: ")
    print("Los productos seleccionados son:", carrito_prod)
    print("El total acumulado es de: $", precio_carrito)


def espaciado():
    print(" " * 30)


# Creamos un menú ficticio
menu = ["1.Hamburguesa", "2.Pizza", "3.Pollo"]
precios_menu = [15, 20, 10]
carrito_prod = []
precio_carrito = 0
metodos_pago = ["1. Efectivo", "2. Tarjeta"]

# Verificamos que el menú funcione y se pueda escoger para añadir al carrito
print("Bienvenido al programa de domicilios")

espaciado()
espaciado()

print("Este es el menú que tenemos para ofrecerte")

espaciado()

carta(menu, precios_menu)

espaciado()
espaciado()

# Empezamos con la creación del carrito y que el usuario pueda escoger su comida
eleccion = input("¿Ya sabes qué quieres comer?: Digita 1 para sí, 2 para no: ")

espaciado()
espaciado()

# Empezamos registro de elecciones y las guardamos en el carrito
if eleccion == "1":
    tomarPedido()

    eleccion = input("¿Deseas cambiar tu elección? Digita 1 para sí, 2 para no: ")
    espaciado()
    espaciado()

    if eleccion == "2":
        espaciado()
        espaciado()
        pagar()

    elif eleccion == "1":
        tomarPedido()
        espaciado()
        espaciado()
        pagar()

elif eleccion == "2":
    print("Este es el menú que tenemos para ofrecerte")
    carta(menu, precios_menu)

    espaciado()
    espaciado()

    tomarPedido()

    espaciado()
    espaciado()

    pagar()
