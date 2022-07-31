#include <SoftwareSerial.h>

char data[20];
byte chPos = 0;
byte ch = 0;

SoftwareSerial link(8,9);

void setup() {
  // put your setup code here, to run once:
  link.begin(9600);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()){
    ch = Serial.read();
    data[chPos] = ch;
    chPos++;
    delay(5);
  }
  data[chPos] = 0;
  chPos = 0;
  Serial.println(data);
  link.println(data);
  delay(24);
  
  
//  if(Serial.available()){
//    x = Serial.readString();
//    strcat(text, x);
//    Serial.println(text);
//    link.println(text);
//    delay(200);
//  }
}
