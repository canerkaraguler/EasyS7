#-*- coding: utf-8 -*-
import struct
import snap7
from snap7 import util
import urllib
import os
import time


def getItemsFromDbLayout(path):
    itemlistt=[]
    with open(path,'r',encoding="utf-8") as fileObject :
        for line in fileObject:
            itemlistt.append(line)

    deliminator='\t'

    items = [
            {
            "name":x.split(deliminator)[0],
            "datatype":x.split(deliminator)[1],
            "bytebit":x.split(deliminator)[2]
            } for x in itemlistt
    ]
    #get length of datablock
    #print(str(items[0]))

    return items



def getDbSize(array,bytekey,datatypekey):
    offsets = { "Bool":1,"Int": 2,"Real":4,"Time":4,"DInt":4,"UDInt":4}#yeni offset degerleri eklenicek
    seq,length = [x[bytekey] for x in array],[x[datatypekey] for x in array]

    maximum=max(seq, key=float)

    idx = seq.index(maximum)
    if length[idx].startswith('String'):
        lastByte = int(maximum.split('.')[0])+(int(length[idx].split('[')[1][:-1]))

    else:

        lastByte = int(maximum.split('.')[0])+(offsets[length[idx]])
    #print(lastByte)
    return lastByte









