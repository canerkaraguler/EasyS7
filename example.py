from PLC import PLC


plc = PLC('192.168.1.100',0,1)
plc.connect()
data = plc.readDb('layout.txt',130)
print(data)