#
# Title: ten_D_addresses
# Author: SRE
# Date: 12/09/2016
#
# Decription: This file contains the addresses used to access the data
#

""" BMP 180 Registers """

BMP_180_I2C               = 0x77  # i2c Pressure and Temp
BMP_180_CAL_AC1           = 0xAA  # R   Calibration data (16 bits)
BMP_180_CAL_AC2           = 0xAC  # R   Calibration data (16 bits)
BMP_180_CAL_AC3           = 0xAE  # R   Calibration data (16 bits)
BMP_180_CAL_AC4           = 0xB0  # R   Calibration data (16 bits)
BMP_180_CAL_AC5           = 0xB2  # R   Calibration data (16 bits)
BMP_180_CAL_AC6           = 0xB4  # R   Calibration data (16 bits)
BMP_180_CAL_B1            = 0xB6  # R   Calibration data (16 bits)
BMP_180_CAL_B2            = 0xB8  # R   Calibration data (16 bits)
BMP_180_CAL_MB            = 0xBA  # R   Calibration data (16 bits)
BMP_180_CAL_MC            = 0xBC  # R   Calibration data (16 bits)
BMP_180_CAL_MD            = 0xBE  # R   Calibration data (16 bits)
BMP_180_CONTROL           = 0xF4
BMP_180_TEMPDATA          = 0xF6
BMP_180_PRESSUREDATA      = 0xF6
BMP_180_READTEMPCMD       = 0x2E
BMP_180_READPRESSURECMD   = 0x34


""" L3GD20 Registers """

L3GD20_I2C = 0x6B                  # i2c Gyro
L3GD20_WHO_AM_I = 0x0F
L3GD20_CTRL_REG1 = 0x20
L3GD20_CTRL_REG2 = 0x21
L3GD20_CTRL_REG3 = 0x22
L3GD20_CTRL_REG4 = 0x23
L3GD20_CTRL_REG5 = 0x24
L3GD20_REFERENCE = 0x25
L3GD20_OUT_TEMP = 0x26
L3GD20_STATUS_REG = 0x27
L3GD20_OUT_X_L = 0x28
L3GD20_OUT_X_H = 0x29
L3GD20_OUT_Y_L = 0x2A
L3GD20_OUT_Y_H = 0x2B
L3GD20_OUT_Z_L = 0x2C
L3GD20_OUT_Z_H = 0x2D
L3GD20_FIFO_CTRL_REG = 0x2E
L3GD20_FIFO_SRC_REG = 0x2F
L3GD20_INT1_CFG = 0x30
L3GD20_INT1_SRC = 0x31
L3GD20_TSH_XH = 0x32
L3GD20_TSH_XL = 0x33
L3GD20_TSH_YH = 0x34
L3GD20_TSH_YL = 0x35
L3GD20_TSH_ZH = 0x36
L3GD20_TSH_ZL = 0x37
L3GD20_INT1_DURATION = 0x38

""" LSM303DLHC Registers """

LSM303DLHC_ACC_I2C = 0x19   # i2c Accelerometer ?Might be 0x32
LSM303DLHC_MAG_I2C = 0x1E   # i2c Magnetometer  ?Might be 0x3C

LSM303_ACCEL_CTRL_REG1_A = 0x20
LSM303_ACCEL_CTRL_REG2_A = 0x21
LSM303_ACCEL_CTRL_REG3_A = 0x22
LSM303_ACCEL_CTRL_REG4_A = 0x23
LSM303_ACCEL_CTRL_REG5_A = 0x24
LSM303_ACCEL_CTRL_REG6_A = 0x25
LSM303_ACCEL_REFERENCE_A = 0x26
LSM303_ACCEL_STATUS_REG_A = 0x27
LSM303_ACCEL_OUT_X_L_A = 0x28
LSM303_ACCEL_OUT_X_H_A = 0x29
LSM303_ACCEL_OUT_Y_L_A = 0x2A
LSM303_ACCEL_OUT_Y_H_A = 0x2B
LSM303_ACCEL_OUT_Z_L_A = 0x2C
LSM303_ACCEL_OUT_Z_H_A = 0x2D
LSM303_ACCEL_FIFO_CTRL_REG_A = 0x2E
LSM303_ACCEL_FIFO_SRC_REG_A = 0x2F
LSM303_ACCEL_INT1_CFG_A = 0x30
LSM303_ACCEL_INT1_SOURCE_A = 0x31
LSM303_ACCEL_INT1_THS_A = 0x32
LSM303_ACCEL_INT1_DURATION_A = 0x33
LSM303_ACCEL_INT2_CFG_A = 0x34
LSM303_ACCEL_INT2_SOURCE_A = 0x35
LSM303_ACCEL_INT2_THS_A = 0x36
LSM303_ACCEL_INT2_DURATION_A = 0x37
LSM303_ACCEL_CLICK_CFG_A = 0x38
LSM303_ACCEL_CLICK_SRC_A = 0x39
LSM303_ACCEL_CLICK_THS_A = 0x3A
LSM303_ACCEL_TIME_LIMIT_A = 0x3B
LSM303_ACCEL_TIME_LATENCY_A = 0x3C
LSM303_ACCEL_TIME_WINDOW_A = 0x3D
LSM303_MAG_CRA_REG_M = 0x00
LSM303_MAG_CRB_REG_M = 0x01
LSM303_MAG_MR_REG_M = 0x02
LSM303_MAG_OUT_X_H_M = 0x03
LSM303_MAG_OUT_X_L_M = 0x04
LSM303_MAG_OUT_Z_H_M = 0x05
LSM303_MAG_OUT_Z_L_M = 0x06
LSM303_MAG_OUT_Y_H_M = 0x07
LSM303_MAG_OUT_Y_L_M = 0x08
LSM303_MAG_SR_REG_M = 0x09
LSM303_MAG_IRA_REG_M = 0x0A
LSM303_MAG_IRB_REG_M = 0x0B
LSM303_MAG_IRC_REG_M = 0x0C
LSM303_MAG_TEMP_OUT_H_M = 0x31
LSM303_MAG_TEMP_OUT_L_M = 0x32
