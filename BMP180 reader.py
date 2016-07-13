/*
* Title: BMP180 reader
* Author: SRE
* Date: 13/07/2016
*
* Decription: ...
*
*/

import smbus, time

rasppi_smbus_version = ([l[12:-1] for l in open('/proc/cpuinfo','r').readline() if l[:8]=="Revision"]+['0000'])[0]
rasppi_smbus = smbus.SMBus(1 if int(rasppi_smbus_version, 16) <= 4 else 0)


/*
    Control register values for BMP180 measurements. The index after the pressure indicates which oversampling is used:
    0: 1 sample
    1: 2 samples
    2: 4 samples
    3: 8 samples
*/

TEMPERATURE     = 0x2E
PRESSURE_0      = 0x34  #Max 4.5ms
PRESSURE_1      = 0x74  #Max 7.5ms
PRESSURE_2      = 0xB4  #Max 13.5ms
PRESSURE_3      = 0xF4  #Max 25.5ms


class Temp:

    def get_temp(...):