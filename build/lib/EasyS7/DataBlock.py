#-*- coding: utf-8 -*-

import snap7
import random



from EasyS7.Utility import *
from EasyS7.DataTypes.DTdint import  DTdint
from EasyS7.DataTypes.DTbool import  DTbool
from EasyS7.DataTypes.DTtime import  DTtime
from EasyS7.DataTypes.DTint import  DTint




class DataBlockObj(object):
		pass



def dbRead(plc,db_num,length,dbitems):

    data=plc.db_read(db_num,0,length)
    obj = DataBlockObj()

    for item in dbitems:
        value = (None,item['name'])
        offset = int(item['bytebit'].split('.')[0])

        if item['datatype']=='Real':
            value = (snap7.util.get_real(data,offset),item['name'].replace(" ","_").replace("/","_"))
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])

        if item['datatype']=='Bool':
            bit =int(item['bytebit'].split('.')[1])
            BoolObj=DTbool(data,bit)
            value = (snap7.util.get_bool(data,offset,bit),item['name'].replace(" ","_").replace("/","_"))
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])

        if item['datatype']=='DInt' :

            DintObj=DTdint(data)
            value=(DintObj.readValue(offset),item['name'].replace(" ","_").replace("/","_"))
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])

        if item['datatype']=='UDInt':

            DintObj=DTdint(data)
            value=(DintObj.readValueU(offset),item['name'].replace(" ","_").replace("/","_"))
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])

        if item['datatype']=='Int':

            IntObj=DTint(data)
            value=(IntObj.readValue(offset),item['name'].replace(" ","_").replace("/","_"))
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])


        if item['datatype']=='Time':

            TimeObj=DTtime(data)
            value=(TimeObj.readValue(offset),item['name'].replace(" ","_").replace("/","_"))
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])



        if item['datatype'].startswith('String'):
            value = snap7.util.get_string(data, offset,int(item['datatype'].split('[')[1][:-1])+1)
            obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value)

        #obj.__setattr__(item['name'].replace(" ","_").replace("/","_"), value[0])


    return obj


