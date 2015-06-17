
const int lightPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int lightReading = analogRead(lightPin);
  Serial.println(lightReading);
  delay(500);
}

