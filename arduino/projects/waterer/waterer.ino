const int motorPin = 9;   // (1)
const int lightPin = A0;

const long onTime = 10 * 1000; // 60 seconds  (2)
const int dayThreshold = 200;              // (3)
const int nightThreshold = 70;

boolean isDay = true;                      // (4)

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {        // (5)
  int lightReading = analogRead(lightPin);
  if (isDay && lightReading < nightThreshold) { // it went dark (6)
    pump();
    isDay = false;
  }
  if (!isDay && lightReading > dayThreshold) {   // (7)
    isDay = true;
  }
}

void pump() {   // (8)
  digitalWrite(motorPin, HIGH);
  delay(onTime);
  digitalWrite(motorPin, LOW);
}
