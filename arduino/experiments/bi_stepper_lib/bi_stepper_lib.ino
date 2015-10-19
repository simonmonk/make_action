#include <Stepper.h>    // (1)

const int in1Pin = 10;
const int in2Pin = 9;
const int in3Pin = 8;
const int in4Pin = 11;

Stepper motor(200, in1Pin, in2Pin, in3Pin, in4Pin);     // (2)

void setup() {       // (3)
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  while (!Serial);
  Serial.begin(9600);
  Serial.println("Command letter followed by number");
  Serial.println("p20 - set the motor speed to 20");
  Serial.println("f100 - forward 100 steps");
  Serial.println("r100 - reverse 100 steps");
  motor.setSpeed(20);       // (4)
}

void loop() {        // (5)
    if (Serial.available()) {
    char command = Serial.read();
    int param = Serial.parseInt();
    if (command == 'p') {
      motor.setSpeed(param);
    }
    else if (command == 'f') {
      motor.step(param);
    }
    else if (command == 'r') {
      motor.step(-param);
    }   
  } 
}
