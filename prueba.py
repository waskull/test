class Auto:
	def __init__(self, placa, modelo, color):
		self.placa = placa
		self.modelo = modelo
		self.color = color
	def mostrar_datos(self):
		print(f"El modelo del auto es {modelo}, su placa es {placa} y su color es: {color}")

auto = Auto()
auto.mostrar_datos()
