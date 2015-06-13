import base64



class FileDecoder(object):

	def __init__(self):
		self.file = open("0-formatted.txt","r")
		self.recoveredfile = open("recoveredfile.rar", "wb")


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
		#self.getBuffer()
		self.decodeBuffer()




if __name__=="__main__":
	a = FileDecoder()
	a.rundecoder()