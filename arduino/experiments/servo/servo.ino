#include <Servo.h> 

const int servoPin = 9;   // (1)

Servo servo;            // (2)

void setup() {            
  servo.attach(servoPin);       // (3)
  servo.write(90);
  Serial.begin(9600);           // (4)
  Serial.println("Enter angle in degrees");
}

void loop() {       // (5)
  if (Serial.available()) {
    int angle = Serial.parseInt();
    servo.write(angle);        // (6)
  }
}
