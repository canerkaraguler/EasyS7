import struct
import snap7
from snap7 import util


class DTbool:
	def __init__(self, readBuffer,boolIndex):
		self.readBuffer=readBuffer
		self.boolIndex=boolIndex
		


	def readValue (self,offset):		
		
		result=snap7.util.get_bool(self.readBuffer,offset,self.boolIndex)
		return result

	