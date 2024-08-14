from PIL import Image
import os

##############
# Constants #
##############

IN_PATH	= "SinLogo"
OUT_PATH = "ConLogo"

LOGO = "Assets/logo.png"

IMG_FORMAT = []

MARGIN = [100, 100]

#############
# Functions #
#############

def loadFormats(array):
	f = open("Assets/formatFile.txt", "r")
	array.extend(f.read().splitlines())

def listPhotos(array):
	# Each element in the dir
	for i in os.listdir("SinLogo"):
		# Test if the format matchs with any IMG_FORMAT
		for j in IMG_FORMAT:
			if i.endswith(j):
				array.append(i)
				break

############
# · MAIN · #
############

loadFormats(IMG_FORMAT)
print(IMG_FORMAT)

arrayPhotos = []
listPhotos(arrayPhotos)

logo = Image.open(LOGO)

x = 0
y = 0

###################################

# Choose position
while(True):
	print("Posiciones:\n")
	print(" 0. Arriba, Izquierda\n")	# [0, 0]
	print(" 1. Abajo, Izquierda\n")		# [0, height]
	print(" 2. Arriba, Derecha\n")		# [width, 0]
	print(" 3. Abajo, Derecha\n")		# [width, height]

	option = input("Selecciona una posición para todas las fotos: ")

	if option in ("0","1","2","3"):
		break;
	else:
		print("Introduce una posición válida.\n")


# Work with the files
for f in arrayPhotos:
	inFile 	= IN_PATH 	+ "/" + f #In PATH
	outFile = OUT_PATH 	+ "/" + f #Out path

	#Load IMG
	img = Image.open(inFile)
	width, height = img.size # (x, y) size of img

	# Calculation of the resize of the logo

	actLogo = logo.copy()


	# Vertical Images
	if (width < height):
		basewidth = int(width / 3.5)

		wpercent = (basewidth / float(actLogo.size[0]))
		hsize = int( (float(actLogo.size[1]) * float(wpercent) ))
		actLogo = actLogo.resize((basewidth,hsize), Image.ANTIALIAS)

	#Horizontal Images
	else:
		baseheight = int(height / 8)

		hpercent = (baseheight / float(actLogo.size[1]))
		wsize = int( (float(actLogo.size[0]) * float(hpercent) ))
		actLogo = actLogo.resize((wsize, baseheight), Image.ANTIALIAS)


	logoWidth, logoHeight = actLogo.size

	if option == "0":
		x = 0
		y = 0
	elif option == "1":
		x = 0
		y = height - logoHeight
	elif option == "2":
		x = width - logoWidth
		y = 0
	else:
		x = width - logoWidth
		y = height - logoHeight



	# Place logo
	Image.Image.paste(img, actLogo, (abs(x - MARGIN[0]), abs(y - MARGIN[1]) ), actLogo)

	#img.show()

	img.save(outFile)
	os.remove(inFile)