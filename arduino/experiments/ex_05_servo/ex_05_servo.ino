#include <Servo.h> 

const int servoPin = 9;

Servo servo;

void setup() {
  servo.attach(servoPin);
  servo.write(90);
  Serial.begin(9600);
  Serial.println("Enter angle in degrees");
}

void loop() {
  if (Serial.available()) {
    int angle = Serial.parseInt();
    servo.write(angle);
  }
}
