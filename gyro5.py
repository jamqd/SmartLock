 # Gyroscope L3GD20H Driver
# Returns Angle Values in dps
# Based on LSM303D driver from Fayetteville Free Library Robotics Group

# Group G - EME - University of Strathclyde

# import required libraries
from smbus:armhf import SMBus

# Defining any required functions
def twos_comp_combine(msb, lsb):
        twos_comp = 256*msb + lsb
        if twos_comp >= 32768:
            return twos_comp - 65536
        else:
            return twos_comp

# set I2C bus
busNum = 1
bus = SMBus(busNum)

L3G = 0x6b # I2C register

L3G_WHOAMI = 0b11010111

# Defining the control registers from L3GD20H Datasheet
CTRL_GYRO_1 = 0x20 #Page 36 of Datasheet;
CTRL_GYRO_2 = 0x21 #Page 38
CTRL_GYRO_3 = 0x22 #Page 39
CTRL_GYRO_4 = 0x23 #Page 39
CTRL_GYRO_5 = 0x24 #Page 40
CTRL_GYRO_6 = 0x39 #Page 48

# Registers holding twos complemented gyro values
GYRO_X_LSB = 0x28
GYRO_X_MSB = 0x29

GYRO_Y_LSB = 0x2A
GYRO_Y_MSB = 0x2B

GYRO_Z_LSB = 0x2C
GYRO_Z_MSB = 0x2D

# Temperature Data
TEMP_Out = 0x26

# Writing required settings to Gyro
if bus.read_byte_data(L3G, 0x0f) == L3G_WHOAMI:
    print ('L3GD20H successfully detected')
else:
    print ('L3GD20H not detected')

bus.write_byte_data(L3G, CTRL_GYRO_1, 0b00001111) #enable x,y,z; choose frequency and bandwidth
bus.write_byte_data(L3G, CTRL_GYRO_2, 0x00) # sets high pass filter
bus.write_byte_data(L3G, CTRL_GYRO_6, 0b000000) # sets LOW_ODR

Gyro_Sens = 0.00875 # Gyro Sensitivity Values based on Defined Range.

 # Reading 2's complemented results from gyroscope
gyrox = twos_comp_combine(bus.read_byte_data(L3G, GYRO_X_MSB), bus.read_byte_data(L3G, GYRO_X_LSB))
gyroy = twos_comp_combine(bus.read_byte_data(L3G, GYRO_Y_MSB), bus.read_byte_data(L3G, GYRO_Y_LSB))
gyroz = twos_comp_combine(bus.read_byte_data(L3G, GYRO_Z_MSB), bus.read_byte_data(L3G, GYRO_Z_LSB))

# Define Gyro Readings in dps
Gyro_X_dps = gyrox*Gyro_Sens
Gyro_Y_dps = gyroy*Gyro_Sens
Gyro_Z_dps = gyroz*Gyro_Sens
