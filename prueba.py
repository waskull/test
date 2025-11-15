class Auto:
	def __init__(self, placa, modelo, color, radio,cambios):
		self.placa = placa
		self.modelo = modelo
		self.color = color
		self.radio = radio
		self.nuevocambio = cambios
		print("Xd")
	def mostrar_datos(self):
		print(f"El grflñgmdfñgmdsfkñgmodelo del auto es {self.modelo}, su placa es {self.placa} y su color es: {self.color}")
		if self.radio: print("Tiene Radio 4K")
		else: print("No Tiene Radio 4K")
	def mostrar_datos(self,mostrar_radio: bool = True) -> None:
		if mostrar_radio:
			print("Radio PRO 8K")
		else: print("No Radio")

auto = Auto("5345-4334","Bettle","Blanco",True)
auto.mostrar_datos()
auto.mostrar_datos(True)
qwe
asd
