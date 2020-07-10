import struct
import snap7

class DTtime:
	def __init__(self, readBuffer):
		self.readBuffer=readBuffer


	def db_readTime(self,byteArray,index):
		data=byteArray[index:(index+4)]
		value=struct.unpack('>l' ,struct.pack('4B',*data))[0]
		return value

	def readValue (self,offset):		
		
		
		result=self.db_readTime(self.readBuffer,offset)
		return result
