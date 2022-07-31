#include <Mouse.h>

#include <SoftwareSerial.h>

SoftwareSerial link(8, 9); // Rx, Tx


char cString[20];
byte chPos = 0;
byte ch = 0;

void setup() {
  // put your setup code here, to run once:
  link.begin(9600); //setup software serial
  Serial.begin(9600);    //setup serial monitor
  Mouse.begin();
  
  // zero the mouse
  Mouse.move(-127, -127, 0);
  delay(200);
  Mouse.move(-127, -127, 0);
  delay(200);
  Mouse.move(-127, -127, 0);
  delay(200);
  Mouse.move(-127, -127, 0);
  delay(200);
  Mouse.move(10, 54, 0);
//  delay(1000);
//  Mouse.move(0, -4, 0);
//  Mouse.move(0,0,0);
//  Mouse.move(0, -4, 0);
//  Mouse.move(0, 8, 0);
  Mouse.end();
}

void loop() {
  // put your main code here, to run repeatedly:
  while (link.available())
  {
    //read incoming char by char:
    ch = link.read();
    cString[chPos] = ch;
    chPos++;
    delay(5);
  }
  cString[chPos] = 0; //terminate cString
  chPos = 0;
  checkSwipe(cString);
  delay(12);
}

void checkSwipe(char x[]) {
  Serial.print(cString);
  if (x[0] =='0') { // up
    Mouse.move(0, -14, 0);
  }
  else if (x[0] == '1') { // up right
    Mouse.move(14, -14, 0);
//    Mouse.move(1, -1, 0);
//    Mouse.move(-1, 1, 0);
  }
  else if (x[0] == '2') { // right
    Mouse.move(14, 0, 0);
//    Mouse.move(1, 0, 0);
//    Mouse.move(-1, 0, 0);
  }
  else if (x[0] == '3') { // down right
    Mouse.move(14, 14, 0);
//    Mouse.move(1, 1, 0);
//    Mouse.move(-1, -1, 0);
  }
  else if (x[0] == '4') { // down
    Mouse.move(0, 14, 0);
//    Mouse.move(0, 1, 0);
//    Mouse.move(0, -1, 0);
  }
  else if (x[0] == '5') { // down left
    Mouse.move(-14, 14, 0);
//    Mouse.move(-1, 1, 0);
//    Mouse.move(1, -1, 0);
  }
  else if (x[0] == '6') { // left
    Mouse.move(-14, 0, 0);
//    Mouse.move(-1, 0, 0);
//    Mouse.move(1, 0, 0);
  }
  else if (x[0] == '7') { // up left
    Mouse.move(-14, -14, 0);
//    Mouse.move(-1, -1, 0);
//    Mouse.move(1, 1, 0);
  }
  else if (x[0] == '8') { // press
    Mouse.press();
  }
  else if (x[0] == '9') { // release
    Mouse.release();
  }
  else if(x[0] == 'a'){ // re zero
    Mouse.move(-127, -127, 0);
    Mouse.move(0,0,0);
    Mouse.move(0 -127, 0);
    Mouse.move(0,0,0);
    Mouse.move(-127, -127, 0);
    Mouse.move(0,0,0);
    Mouse.move(-127, -127, 0);
    Mouse.move(0,0,0);
    delay(20);
    Mouse.move(10, 54, 0);
  }
  Mouse.move(0,0,0);
}
