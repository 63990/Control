#
# Title: BMP180
# Author: SRE
# Date: 13/07/2016
#
# Decription: This code is partly taken from Adafruit Industries (the original copy
#             can be found at https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code)
#

import ten_D_addresses

""" Calibration """
def calibration(self):
    self.cal_AC1 = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_AC1)  # INT16
    self.cal_AC2 = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_AC2)  # INT16
    self.cal_AC3 = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_AC3)  # INT16
    self.cal_AC4 = self._device.readU16BE(ten_D_addresses.BMP_180_CAL_AC4)  # UINT16
    self.cal_AC5 = self._device.readU16BE(ten_D_addresses.BMP_180_CAL_AC5)  # UINT16
    self.cal_AC6 = self._device.readU16BE(ten_D_addresses.BMP_180_CAL_AC6)  # UINT16
    self.cal_B1 = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_B1)  # INT16
    self.cal_B2 = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_B2)  # INT16
    self.cal_MB = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_MB)  # INT16
    self.cal_MC = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_MC)  # INT16
    self.cal_MD = self._device.readS16BE(ten_D_addresses.BMP_180_CAL_MD)  # INT16


def read_raw_temp(self):
    """Reads the raw (uncompensated) temperature from the sensor."""
    self._device.write8(ten_D_addresses.BMP_180_CONTROL, ten_D_addresses.BMP_180_READTEMPCMD)
    raw = self._device.readU16BE(ten_D_addresses.BMP_180_TEMPDATA)
    return raw

def read_temperature(self):
    """Gets the compensated temperature in degrees celsius."""
    UT = self.read_raw_temp()
    # Calculations below are taken straight from section 3.5 of the datasheet.
    X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
    X2 = (self.cal_MC << 11) // (X1 + self.cal_MD)
    B5 = X1 + X2
    temp = ((B5 + 8) >> 4) / 10.0
    return temp

def read_raw_pressure(self):
    """Reads the raw (uncompensated) pressure level from the sensor."""
    self._device.write8(ten_D_addresses.BMP_180_CONTROL, ten_D_addresses.BMP_180_READPRESSURECMD + (self._mode << 6))
    msb = self._device.readU8(ten_D_addresses.BMP_180_PRESSUREDATA)
    lsb = self._device.readU8(ten_D_addresses.BMP_180_PRESSUREDATA + 1)
    xlsb = self._device.readU8(ten_D_addresses.BMP_180_PRESSUREDATA + 2)
    raw = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - self._mode)
    return raw

def read_pressure(self):
    """Gets the compensated pressure in Pascals."""
    UT = self.read_raw_temp()
    UP = self.read_raw_pressure()
    # Datasheet values for debugging:
    # UT = 27898
    # UP = 23843
    # Calculations below are taken straight from section 3.5 of the datasheet.
    # Calculate true temperature coefficient B5.
    X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
    X2 = (self.cal_MC << 11) // (X1 + self.cal_MD)
    B5 = X1 + X2
    # Pressure Calculations
    B6 = B5 - 4000
    X1 = (self.cal_B2 * (B6 * B6) >> 12) >> 11
    X2 = (self.cal_AC2 * B6) >> 11
    X3 = X1 + X2
    B3 = (((self.cal_AC1 * 4 + X3) << self._mode) + 2) // 4
    X1 = (self.cal_AC3 * B6) >> 13
    X2 = (self.cal_B1 * ((B6 * B6) >> 12)) >> 16
    X3 = ((X1 + X2) + 2) >> 2
    B4 = (self.cal_AC4 * (X3 + 32768)) >> 15
    self._logger.debug('B4 = {0}'.format(B4))
    B7 = (UP - B3) * (50000 >> self._mode)
    if B7 < 0x80000000:
        p = (B7 * 2) // B4
    else:
        p = (B7 // B4) * 2
    X1 = (p >> 8) * (p >> 8)
    X1 = (X1 * 3038) >> 16
    X2 = (-7357 * p) >> 16
    p = p + ((X1 + X2 + 3791) >> 4)
    return p

def read_altitude(self, sealevel_pa=101325.0):
    """Calculates the altitude in meters."""
    # Calculation taken straight from section 3.6 of the datasheet.
    pressure = float(self.read_pressure())
    altitude = 44330.0 * (1.0 - pow(pressure / sealevel_pa, (1.0 / 5.255)))
    return altitude

def read_sealevel_pressure(self, altitude_m=0.0):
    """Calculates the pressure at sealevel when given a known altitude in
    meters. Returns a value in Pascals."""
    pressure = float(self.read_pressure())
    p0 = pressure / pow(1.0 - altitude_m / 44330.0, 5.255)
    return p0