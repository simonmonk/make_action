
const int controlPin = 9; // (1)

void setup() {  // (2)
  pinMode(controlPin, OUTPUT);
}

void loop() {  // (3)
  digitalWrite(controlPin, HIGH);
  delay(5000);
  digitalWrite(controlPin, LOW);
  delay(2000);
}
