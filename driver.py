#! /usr/bin/python
#
# Title:Driver.py
# Description:BearCat driver
# Development Environment:OS X 10.9.3/Python 2.7.7
# Legalise:Copyright (C) 2014 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import yaml

import bc780


class BearCatDriver:

    def execute(self, command, argument, receiver):
        if command == 'status':
            print receiver.testRadio()
        elif command == 'sample':
            print receiver.sampleRadio()
        elif command == 'tune':
            print receiver.tuneRadio(float(argument))

print 'start driver'

#
# argv[1] = command
# argv[2] = optional arguments
# argv[3] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        print 'must supply command'
        sys.exit(-1)

    if len(sys.argv) > 2:
        argument = sys.argv[2]
    else:
        argument = 'empty'

    if len(sys.argv) > 3:
        yamlFileName = sys.argv[3]
    else:
        yamlFileName = 'config.yaml'

    configuration = yaml.load(file(yamlFileName))

    serialPort = configuration['serialPort']
    serialSpeed = configuration['serialSpeed']
    serialTimeOut = configuration['serialTimeOut']

    receiver = bc780.Bc780(serialPort, serialSpeed, serialTimeOut)

    driver = BearCatDriver()
    driver.execute(command, argument, receiver)

print 'stop driver'
