# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 05:14:38 2019

@author: lolly
"""

char filename[20];
sprintf(filename, "/dev/i2c-%d", 1);
file = open(filename, O_RDWR);
if (file<0) {
        printf("Unable to open I2C bus!");
        exit(1);
}

// Enable accelerometer.
writeAccReg(LSM303_CTRL_REG1_A, 0b01010111); //  z,y,x axis enabled , 100Hz data rate
writeAccReg(LSM303_CTRL_REG4_A, 0b00101000); // +/- 8G full scale: FS = 10 on DLHC, high resolution output mode

void readACC(int  *a)
{
    uint8_t block[6];
    selectDevice(file,LSM9DS0_ACC_ADDRESS);
    readBlock(0x80 |  LSM9DS0_OUT_X_L_A, sizeof(block), block);
     
    // Combine readings for each axis.
    *a = (int16_t)(block[0] | block[1] << 8);
    *(a+1) = (int16_t)(block[2] | block[3] << 8);
    *(a+2) = (int16_t)(block[4] | block[5] << 8);
 
    
    
}

//Convert Gyro raw to degrees per second
rate_gyr_x = (float) *gyr_raw * G_GAIN;
rate_gyr_y = (float) *(gyr_raw+1) * G_GAIN;
rate_gyr_z = (float) *(gyr_raw+2) * G_GAIN;

//Calculate the angles from the gyro
gyroXangle+=rate_gyr_x*DT;
gyroYangle+=rate_gyr_y*DT;
gyroZangle+=rate_gyr_z*DT;

AccXangle = (float) (atan2(*(acc_raw+1),*(acc_raw+2))+M_PI)*RAD_TO_DEG;
AccYangle = (float) (atan2(*(acc_raw+2),*acc_raw)+M_PI)*RAD_TO_DEG;

//Change the rotation value of the accelerometer to -/+ 180
if (AccXangle > 180)
{
          AccXangle -= (float)360.0;
}
         if (AccYangle > 180)
         AccYangle -= (float)360.0;
         
 startInt = mymillis();        
while(mymillis() - startInt < 20)
{
        usleep(100);
}