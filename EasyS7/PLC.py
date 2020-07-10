#-*- coding: utf-8 -*-
import snap7
import sys
from EasyS7.Utility import *
from EasyS7.DataBlock import *


class PLC:

    def __init__(self,plc_address , plc_rack , plc_slot , plc_tcpport=102):
        print("[INFO] : Initialization started...")
        self.plc_address = str(plc_address)
        self.plc_rack = int(plc_rack)
        self.plc_slot = int(plc_slot)
        self.plc_tcpport = plc_tcpport
        self.plc = snap7.client.Client()
        print("[INFO] : Initialization done...")





    def setPlcAdress(plc_address):
        self.plc_address = str(plc_address)

    def setPlcRack(plc_rack):
        self.plc_rack = plc_rack

    def setPlcSlot(plc_slot):
        self.plc_slot = plc_slot

    def setPlcTcpport(plc_tcpport):
        self.plc_tcpport = plc_tcpport

    def connect(self):
        print("[INFO] : Establishing PLC connection...")
        try:

            self.plc.connect(self.plc_address,self.plc_rack,self.plc_slot,self.plc_tcpport)
            if self.plc.get_connected():
                print("[INFO] : Connection succeed.")
            else:
                print("[ERROR] : Connection failed.")
                sys.exit()

        except Exception as e:

            print("[ERROR] : ",str(e))
            print("[ERROR] : Connection failed.")
            sys.exit()


    def readDb(self,layout_path, db_no):
            print("[INFO] : Data block read operation started...")
            db_items = getItemsFromDbLayout(layout_path)
            db_size = getDbSize(db_items,'bytebit','datatype')
            db_data = dbRead(self.plc,db_no,db_size,db_items).__dict__
            print("[INFO] : Data block read operation done...")
            return db_data

