/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO 
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino model, check
  the Technical Specs of your board  at https://www.arduino.cc/en/Main/Products
  
  1This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
  
  modified 2 Sep 2016
  by Arturo Guadalupi
  
  modified 8 Sep 2016
  by Colby Newman
*/

#include <SPI.h>
#include <RH_RF24.h>

#define DEBUGSerial Serial
RH_RF24 rf24;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  DEBUGSerial.begin(115200);
  while (!DEBUGSerial) ; // Wait for serial port to be available
  DEBUGSerial.println("Serial Test1.");

  if (!rf24.init()) {
    DEBUGSerial.println("RADIO init failed");
    while(1);
  }
}

uint32_t count = 0;
uint32_t tcount = 0;

// the loop function runs over and over again forever
void loop() {
  while(count<3) { 
  //uint8_t data[] = {0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
  //uint8_t data[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
  //uint8_t data[] = {0xff, 0x00, 0xff, 0x00, 0xff, 0x00, 0xff};
  //uint8_t data[] = {0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77};
  //uint8_t data[] = {0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77};
  //uint8_t data[] = {0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77};
  //uint8_t data[] = "ZakHell";
  uint8_t data[] = {0x5a, 0x61, 0x6b, 0x48, 0x65, 0x6c, 0x6c};

  DEBUGSerial.print("Loop:");

  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//  delay(500);                       // wait for a second

  DEBUGSerial.println("Sending to rf24_server");
//  delay(500);                       // wait for a second
  rf24.send(data, 7);

  DEBUGSerial.println("Waiting");
  //rf24.waitPacketSent();
  DEBUGSerial.println("Done");

  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
  rf24.setMode(RHGenericDriver::RHModeIdle);
  count++;
  DEBUGSerial.println(tcount++);
  }
  delay(10000);
  count=0;

}
