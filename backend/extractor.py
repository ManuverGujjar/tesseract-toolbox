import sys
path_to_image = sys.argv[1]
out = open('/Users/manuver/programs/project/tesseract/backend/out.txt', 'w');
# sys.stdout = out
try:
	import pytesseract
	from PIL import Image
except Exception as e:
	print(e);
	sys.exit()

def image_OCR():
	try:
		# Define config parameters.
		# '-l eng'  for using the English language
		# '--oem 1' for using LSTM OCR Engine
		config = ('-l eng --oem 1 --psm 3')


		#importing Image
		try:
			image = Image.open(path_to_image)
		except Exception as e:
			print(e)
			sys.exit()



		#Gettting text From Image
		text_from_image = pytesseract.image_to_string(image, config = config)

		return text_from_image
	except Exception as e:
		print(e)
		sys.exit()

print(image_OCR())
