 # Gyroscope L3GD20H Driver
# Returns Angle Values in dps
# Based on LSM303D driver from Fayetteville Free Library Robotics Group

# Group G - EME - University of Strathclyde

# import required libraries
from smbus2 import SMBus
import time

class motion_detect:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0
        # set I2C bus
        busNum = 1
        self.bus = SMBus(busNum)

        self.L3G = 0x6b # I2C register

        L3G_WHOAMI = 0b11010111

        # Defining the control registers from L3GD20H Datasheet
        CTRL_GYRO_1 = 0x20 #Page 36 of Datasheet;
        CTRL_GYRO_2 = 0x21 #Page 38
        CTRL_GYRO_3 = 0x22 #Page 39
        CTRL_GYRO_4 = 0x23 #Page 39
        CTRL_GYRO_5 = 0x24 #Page 40
        CTRL_GYRO_6 = 0x39 #Page 48

        # Registers holding twos complemented gyro values
        self.GYRO_X_LSB = 0x28
        self.GYRO_X_MSB = 0x29

        self.GYRO_Y_LSB = 0x2A
        self.GYRO_Y_MSB = 0x2B

        self.GYRO_Z_LSB = 0x2C
        self.GYRO_Z_MSB = 0x2D

        # Temperature Data
        TEMP_Out = 0x26

        # Writing required settings to Gyro
        if self.bus.read_byte_data(self.L3G, 0x0f) == L3G_WHOAMI:
            print ('L3GD20H successfully detected')
        else:
            print ('L3GD20H not detected')

        self.bus.write_byte_data(self.L3G, CTRL_GYRO_1, 0b00001111) #enable x,y,z; choose frequency and bandwidth
        self.bus.write_byte_data(self.L3G, CTRL_GYRO_2, 0x00) # sets high pass filter
        self.bus.write_byte_data(self.L3G, CTRL_GYRO_6, 0b000000) # sets LOW_ODR

        self.Gyro_Sens = 0.00875 # Gyro Sensitivity Values based on Defined Range.
    def sample(self):
        self.x1 = self.x2
        self.y1 = self.y2
        self.z1 = self.z2
         # Reading 2's complemented results from gyroscope
        gyrox = self.twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_X_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_X_LSB))
        gyroy = self.twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_Y_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_Y_LSB))
        gyroz = self.twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_Z_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_Z_LSB))

        # Define Gyro Readings in dps
        Gyro_X_dps1 = gyrox*self.Gyro_Sens
        Gyro_Y_dps1 = gyroy*self.Gyro_Sens
        Gyro_Z_dps1 = gyroz*self.Gyro_Sens
#        print (Gyro_X_dps1)
#        print (Gyro_Y_dps1)
#        print (Gyro_Z_dps1)
        self.x2 = Gyro_X_dps1
        self.y2 = Gyro_X_dps1
        self.z2 = Gyro_X_dps1

        
    # Defining any required functions
    def twos_comp_combine(self, msb, lsb):
            twos_comp = 256*msb + lsb
            if twos_comp >= 32768:
                return twos_comp - 65536
            else:
                return twos_comp
    def calcDist(self):
        return pow(pow(self.x2-self.x1, 2)+pow(self.y2-self.y1, 2)+pow(self.z2-self.z1, 2), 1/2)

#    def detectMotion(self):
#        
#
#        dist = 0
#        
#        print("Stationary")
#         # Reading 2's complemented results from gyroscope
#        gyrox = twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_X_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_X_LSB))
#        gyroy = twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_Y_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_Y_LSB))
#        gyroz = twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_Z_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_Z_LSB))
#
#        # Define Gyro Readings in dps
#        Gyro_X_dps1 = gyrox*self.Gyro_Sens
#        Gyro_Y_dps1 = gyroy*self.Gyro_Sens
#        Gyro_Z_dps1 = gyroz*self.Gyro_Sens
#        print (Gyro_X_dps1)
#        print (Gyro_Y_dps1)
#        print (Gyro_Z_dps1)
#        print("paused")
#        time.sleep(1.5)
#
#        gyrox = twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_X_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_X_LSB))
#        gyroy = twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_Y_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_Y_LSB))
#        gyroz = twos_comp_combine(self.bus.read_byte_data(self.L3G, self.GYRO_Z_MSB), self.bus.read_byte_data(self.L3G, self.GYRO_Z_LSB))
#
#        Gyro_X_dps2 = gyrox*self.Gyro_Sens
#        Gyro_Y_dps2 = gyroy*self.Gyro_Sens
#        Gyro_Z_dps2 = gyroz*self.Gyro_Sens
#        print (Gyro_X_dps2)
#        print (Gyro_Y_dps2)
#        print (Gyro_Z_dps2)
#        dist = calcDiff(Gyro_X_dps1,Gyro_Y_dps1,Gyro_Z_dps1,Gyro_X_dps2,Gyro_Y_dps2,Gyro_Z_dps2)
#        print("dist: "+str(dist))
#        return dist
#

