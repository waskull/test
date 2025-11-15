class Auto:
	def __init__(self, placa, modelo, color, radio):
		self.placa = placa
		self.modelo = modelo
		self.color = color
		self.radio = radio
	def mostrar_datos(self):
		print(f"El modelo del auto es {modelo}, su placa es {placa} y su color es: {color}")
		if radio: print("Tiene Radio")
		else: print("No Tiene Radio")

auto = Auto("5345-4324","Escarabajo","Blanco",True)
auto.mostrar_datos()
