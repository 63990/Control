#
# Title: L3GD20
# Author: SRE
# Date: 13/07/2016
#
# Decription: Reads High (add if statement later and other opts etc...)
#             The addresses may be the wrong way around
#

import ten_D_addresses

def read_raw_x_gyro(self):
    """Reads the raw from the sensor."""
    self._device.write8(ten_D_addresses.L3GD20_WHO_AM_I, ten_D_addresses.L3GD20_TSH_XH)
    raw_x = self._device.readU8(ten_D_addresses.L3GD20_OUT_X_H) # H = High
    return raw_x

def read_raw_y_gyro(self):
    """Reads the raw from the sensor."""
    self._device.write8(ten_D_addresses.L3GD20_WHO_AM_I, ten_D_addresses.L3GD20_TSH_YH)
    raw_y = self._device.readU8(ten_D_addresses.L3GD20_OUT_Y_H) # H = High
    return raw_y

def read_raw_z_gyro(self):
    """Reads the raw from the sensor."""
    self._device.write8(ten_D_addresses.L3GD20_WHO_AM_I, ten_D_addresses.L3GD20_TSH_ZH)
    raw_z = self._device.readU8(ten_D_addresses.L3GD20_OUT_Z_H) # H = High
    return raw_z
