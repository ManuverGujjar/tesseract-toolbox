# command line Argments


#path to textfile
#path to save
#mainSubject 
#no of topic



import sys
import os;
workingPath = '/Users/manuver/programs/project/tesseract/backend/'

# sys.stdout = open(workingPath + 'output.txt', 'w');
try:

	# def print(s):
	# 	pass
	# 	# try:
	# 	# 	file = open(workingPath + "output.txt", 'w')
			
	# 	# 	file.write(str(s))
	# 	# except:
	# 	# 	print(e)



	import urllib
	try:
		import pytesseract
	except:
		print('Error While Importing pytesseract')
		sys.exit()


	try:
		import pdfkit
	except:
		print('please install module pdfkit')
		sys.exit()


	try:
		from PIL import Image
	except:
		print('please install module PIL')
		sys.exit()




	try: 
		from googlesearch import search 
	except:
		print("Please install module google using 'pip install google'")
		sys.exit()







	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""UNIVERSAL VARIABLES"""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



	mainCounter = 0
	total = 0
	text_file = sys.argv[1]

	#Starting and Ending Word both Excluded
	starting_word = 'start'
	ending_word = 'end'


	path_to_save = sys.argv[2]

	main_subject = sys.argv[3]

	if main_subject != '':
		path_to_save = path_to_save+'/'
	else:
		path_to_save = path_to_save+'/'

	no_of_result_per_topic = int(sys.argv[4])

	sperator = ','

	websites_must_contains = ['geeks', 'tut', 'study', 'math']



	# path_to_image = input('Enter Path To Image :')
	# path_to_save = input('Enter Path to Save :')
	# main_subject = input('Enter Main Subject of the Topics :')
	# no_of_result_per_topic = int(input('Enter No. of Result per topic :'))



	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#"""""""""""""""""END OF UNIVERSAL VARIABLE DECLARATION""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""









	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""FUCTION DEFINATIONS"""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



	def extractor(query):
		try:
			global mainCounter
			print("Q : ", query)
			results = [x for x in search(query, tld="com", num=no_of_result_per_topic, stop=no_of_result_per_topic, pause=1)]
			counter = ''
			if(len(results) > 1):
				counter = 0
			else:
				counter = ''
			for j in results:
					try:
						mainCounter += 1
						pdfkit.from_url(j, path_to_save + " " + query + str(counter)+'.pdf')
						# progress = open(workingPath+'progress.prog','w')
						# progress.write(str(mainCounter*100/total))
						# progress.close()
						print(f'Saving {path_to_save}{query}{str(counter)}.pdf<br>')
						if(len(results) > 1):
							counter += 1
					except Exception as e:
						print(e)
		except Exception as e:
			raise e


	def search_topic_save(queries):
			
		counter = 0

		for query in queries:
			try:
				extractor(query)
			except Exception as e:
				raise e
				# sys.exit()
			



	def image_OCR():
		# Define config parameters.
		# '-l eng'  for using the English language
		# '--oem 1' for using LSTM OCR Engine
		config = ('-l eng --oem 1 --psm 3')


		#importing Image
		try:
			image = Image.open(path_to_image)
		except:
			print('unable to get the image. Make Sure You have set correct image path with correct extention<br>')
			sys.exit()



		#Gettting text From Image
		text_from_image = pytesseract.image_to_string(image, config = config)

		return text_from_image



	def topic_sperator(text_from_image):
		try:
			#list of all topic sperated by sperator 
			list_of_all_topics = text_from_image.split(sperator)


			#temp variable
			start_index = 0

			#list of usful queries
			queries = []


			for topic in list_of_all_topics:
				if ending_word.lower() in topic.lower():
					break

				if start_index:
					topic = list(topic)
					while '\n' in topic:
						topic.remove('\n')
					topic = ''.join(topic)
					queries.append(topic+" "+main_subject)
				if starting_word.lower() in topic.lower():
					start_index = 1
			return queries
		except Exception as e:
			raise e

	def topic_sperator_main(text_from_image):
		try:
			return text_from_image.split(sperator)
		except Exception as e:
			print(e)






	#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#""""""""""""""""""""""""""""""END OF FUNCTION DEFINATIONS""""""""""""""""""
	#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""








	try:
		file = open(text_file, 'r')
		text_from_image = file.read()
		queries = topic_sperator_main(text_from_image)
		total = len(queries)*no_of_result_per_topic;
		print('Searching On Web...<br>')
		search_topic_save(queries)
	except Exception as e:
		raise e
except Exception as e:
	raise e