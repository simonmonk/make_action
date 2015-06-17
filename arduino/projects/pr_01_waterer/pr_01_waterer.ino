const int motorPin = 9;
const int lightPin = A0;

const long onTime = 10 * 1000; // 60 seconds
const int dayThreshold = 200;
const int nightThreshold = 70;

boolean isDay = true;

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  int lightReading = analogRead(lightPin);
  if (isDay && lightReading < nightThreshold) { // it went dark
    pump();
    isDay = false;
  }
  if (!isDay && lightReading > dayThreshold) {
    isDay = true;
  }
}

void pump() {
  digitalWrite(motorPin, HIGH);
  delay(onTime);
  digitalWrite(motorPin, LOW);
}
