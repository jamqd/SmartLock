#include <wiringPi.h>
#include <string.h>
#include <stdio.h>

#define m1 29
#define sw 12

void gate_open()
{
     digitalWrite(m1, HIGH);
}

void gate_close()
{
     digitalWrite(m2, LOW);
}

void setup(){
     pinMode(m1, OUTPUT);
     pinMode(sw, OUTPUT);
}

void pressSwitch(){
    if (digitalRead(sw) == 1){
        gate_close();        
    } else {
        gate_open();    
    }       
}

void main(void)
{
    setup();
    gate_close();
    delay(2000);
    gate_open();
}