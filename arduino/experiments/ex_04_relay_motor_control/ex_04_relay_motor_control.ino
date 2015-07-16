
const int controlPin = 9;

void setup() { 
  pinMode(controlPin, OUTPUT);
}

void loop() { 
  digitalWrite(controlPin, LOW);   // (1)
  delay(5000);
  digitalWrite(controlPin, HIGH);
  delay(2000);
}
