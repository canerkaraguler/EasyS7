import struct
import snap7

class DTint:
	def __init__(self, readBuffer):
		self.readBuffer=readBuffer


	def db_readInt(self,byteArray,index):
		data=byteArray[index:(index+2)]
		value=struct.unpack('>h' ,struct.pack('2B',*data))[0]
		return value

	def readValue (self,offset):		
		
		
		result=self.db_readInt(self.readBuffer,offset)
		return result
