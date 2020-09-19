entrada =  input("Ingrese dígitos: ")

f1, f2, f3, f4, f5 = "","","","",""

numeros = [
	"###-# #-# #-# #-###", # 0
	"  #-  #-  #-  #-  #", # 1
	"###-  #-###-#  -###", # 2
	"###-  #-###-  #-###", # 3
	"# #-# #-###-  #-  #", # 4
	"###-#  -###-  #-###", # 5
	"###-#  -###-# #-###", # 6
	"###-  #-  #-  #-  #", # 7
	"###-# #-###-# #-###", # 8
	"###-# #-###-  #-###"  # 9
]

def escoger_rodajas(entrada,fila,numeros):
	global f1, f2, f3, f4, f5
	if fila == 0:	
		f1 += numeros[entrada][0:3] + " "
	elif fila == 1:
		f2 += numeros[entrada][4:7] + " "
	elif fila == 2:
		f3 += numeros[entrada][8:11] + " "
	elif fila == 3:
		f4 += numeros[entrada][12:15] + " "
	elif fila == 4:
		f5 += numeros[entrada][16:19] + " "


def main():
	global entrada
	global numeros
	global f1, f2, f3, f4, f5
	
	for i in entrada:
		for j in range(0,5):
			escoger_rodajas(int(i),j,numeros)

	print(f1,f2,f3,f4,f5,sep="\n")
main()