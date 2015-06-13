import base64



class FileDecoder(object):

	def __init__(self,inputfile,outputfile):
		self.file = open(inputfile,"r")
		self.recoveredfile = open(outputfile, "wb")


	def getBuffer(self,bytecounter=10):
		with self.file as f :
			readBuffer = f.read().splitlines()
		self.file.close()
		return ''.join(readBuffer)
			

	def decodeBuffer(self):
		#decodedBuffer = self.getBuffer()
		decodedBuffer = base64.b64decode(self.getBuffer())
		self.recoveredfile.write(decodedBuffer)
		self.recoveredfile.close()

	def rundecoder(self):
		self.decodeBuffer()


