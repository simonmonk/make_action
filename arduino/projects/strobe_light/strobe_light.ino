const int controlPin = 11;  
const int potPin = A0;

const int pulseLen = 20; 
const int minPeriod = 30;
const int maxPeriod = 250;

void setup() {                    
  pinMode(controlPin, OUTPUT);
  digitalWrite(controlPin, HIGH);
}

void loop() {
  int raw = analogRead(potPin);
  int period = map(raw, 0, 1023, minPeriod, maxPeriod);
  digitalWrite(controlPin, LOW);
  delay(pulseLen);
  digitalWrite(controlPin, HIGH);
  delay(period - pulseLen);
}
