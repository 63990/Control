#
# Title: LSM303
# Author: SRE
# Date: 13/07/2016
#
# Decription: Reads High (add if statement later and other opts etc...)
#             The addresses may be the wrong way around
#

import ten_D_addresses

def read_raw_x_mag(self):
    """Reads the raw from the sensor."""
    self._device.write8(ten_D_addresses.LSM303DLHC_MAG_I2C, ten_D_addresses.LSM303_MAG_SR_REG_M)
    raw_x = self._device.readU8(ten_D_addresses.LSM303_MAG_OUT_X_H_M) # H = High
    return raw_x

def read_raw_y_mag(self):
    """Reads the raw from the sensor."""
    self._device.write8(ten_D_addresses.LSM303DLHC_MAG_I2C, ten_D_addresses.LSM303_MAG_SR_REG_M)
    raw_y = self._device.readU8(ten_D_addresses.LSM303_MAG_OUT_Y_H_M) # H = High
    return raw_y

def read_raw_z_mag(self):
    """Reads the raw from the sensor."""
    self._device.write8(ten_D_addresses.LSM303DLHC_MAG_I2C, ten_D_addresses.LSM303_MAG_SR_REG_M)
    raw_z = self._device.readU8(ten_D_addresses.LSM303_MAG_OUT_Z_H_M) # H = High
    return raw_z


