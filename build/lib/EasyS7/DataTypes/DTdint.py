import struct
import snap7
import random

class DTdint:
	def __init__(self, readBuffer):
		self.readBuffer=readBuffer


	def db_readDint(self,byteArray,index):
		data=byteArray[index:(index+4)]
		value=struct.unpack('>l' ,struct.pack('4B',*data))[0]
		return value

	def db_readUDint(self,byteArray,index):
		data=byteArray[index:(index+4)]
		value=struct.unpack('>L' ,struct.pack('4B',*data))[0]
		return value

	def readValue (self,offset):		
		
		
		result=self.db_readDint(self.readBuffer,offset)
		return result

	def readValueU (self,offset):		
		
		
		result=self.db_readDint(self.readBuffer,offset)
		return result
	def set_dint(self,_bytearray,byte_index):
		
		
		real = struct.pack('>l',random.randint(1,10))
		_bytes = struct.unpack('4B', real)
		for i, b in enumerate(_bytes):
			_bytearray[byte_index + i] = b
		return _bytearray