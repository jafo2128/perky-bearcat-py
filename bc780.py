#
# Title:bc780.py
# Description:bearcat bc780 scanner
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import serial


class Bc780:
    def __init__(self, serialPort, serialSpeed, serialTimeOut):
        self.serialPort = serialPort
        self.serialSpeed = serialSpeed
        self.serialTimeOut = serialTimeOut

    def __str__(self):
        return "uniden:%s" % self.serialPort

    def floatFreqToInt(self, frequency):
        """
        convert from floating point frequency in MHz to Uniden format
        """
        return int(frequency * 10000)

    def intFreqToFloat(self, frequency):
        """
        convert from uniden integer freq to MHz
        """
        return float(frequency)/10000.0

    def invokeRadio(self, command, argument):
        """
        invoke remote device via serial port
        """
        buffer = "%s%s\r" % (command, argument)
        print buffer

        device = serial.Serial(self.serialPort, self.serialSpeed, timeout=self.serialTimeOut)
        device.write(buffer)
        buffer = device.readline()
        device.close()

        return buffer

    def sampleRadio(self):
        return self.invokeRadio('SG', '')

    def testRadio(self):
        return self.invokeRadio('SI', '')

    def tuneRadio(self, frequency):
        """
        tune scanner to specified frequency
        returns frequency as integer
        """
        argument = "%8.8d?" % self.floatFreqToInt(frequency)
        result = self.invokeRadio('RF', argument)
        return result
