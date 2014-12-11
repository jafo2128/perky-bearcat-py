#
# Title:bc780.py
# Description:bearcat bc780 scanner
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
#import serial


class Bc780:
    def __init__(self, serialPort, serialSpeed, serialTimeOut):
        self.serialPort = serialPort
        self.serialSpeed = serialSpeed
        self.serialTimeOut = serialTimeOut

    def invokeRadio(self, command, argument):
        buffer = "SI\r"
        print buffer

#        device = serial.Serial(self.serialPort, self.serialSpeed, timeout=self.serialTimeOut)
#        device.write(buffer)
#        buffer = device.read(self.serialTimeOut)
#        print buffer
#        device.close()
