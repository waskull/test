class Auto:
	def __init__(self, placa, modelo, color, radio):
		self.placa = placa
		self.modelo = modelo
		self.color = color
		self.radio = radio
	def mostrar_datos(self):
		print(f"El modelo del auto es {modelo}, su placa es {placa} y su color es: {color}")
		if radio: print("Tiene Radio 4K")
		else: print("No Tiene Radio 4K")
	def mostrar_datos(self,mostrar_radio: bool = True) ->:
		if mostrar_radio:
			print("Radio PRO 4K")
		else print("No Radio")

auto = Auto("5345-4324","Escarabajo","Blanco",True)
auto.mostrar_datos()
auto.mostrar_datos(True)
