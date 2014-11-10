# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:59:03 2014

@author: Dan
"""

import serial

class LaunchPad(object):
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.term = '\n'
        
    def openPort(self):
        self.ser = serial.Serial(self.port, self.baud)
        
    def writePort(self, command):
        self.ser.write(command + self.term)
        
    def closePort(self):
        self.ser.close()

if __name__ == '__main__':
    foo = LaunchPad('/dev/tty.uart-43FF4D53F40B3639', 9600)
    foo.openPort()
    foo.writePort('n2\nn1\n')
    foo.closePort()