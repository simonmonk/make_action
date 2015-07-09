// Experiment 1. Basic Motor Control

const int motorPin = 9;

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  digitalWrite(motorPin, LOW);
  delay(5000);
  digitalWrite(motorPin, HIGH);
  delay(2000);
}
