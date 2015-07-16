#include <OneWire.h>
#include <DallasTemperature.h>

const double minTemp = 0.0;  // (1)
const double maxTemp = 20.0;
const float tempOKMargin = 0.5; 

const int tempPin = 2;
const int coolPin = 9;
const int ledPin = 10;       // (2)
const int potPin = A0;
const long period = 1000; // >750

OneWire oneWire(tempPin);
DallasTemperature sensors(&oneWire);

double setTemp = 0.0;
double measuredTemp = 0.0;
double outputPower = 0.0;     
long lastSampleTime = 0;

void setup() {
  pinMode(coolPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);

  sensors.begin();
}

void loop() { 
  long now = millis();         // (3)
  if (now > lastSampleTime + period) {
      checkTemperature();
      lastSampleTime = now;
  }0 and 20
  setTemp = readSetTempFromPot(); // (4)
}

void checkTemperature() {       // (5)
  float measuredTemp = readTemp();    
  float error = setTemp - measuredTemp;
  Serial.print(measuredTemp);
  Serial.print(", ");
  Serial.print(setTemp);
  if (error < 0) {                    
      digitalWrite(coolPin, HIGH);
      Serial.println(", 1");
  }
  else {
    digitalWrite(coolPin, LOW);
    Serial.println(", 0");
  }
  
  if (abs(error) < tempOKMargin) {        // (6)
    digitalWrite(ledPin, HIGH);
  }
  else {
    digitalWrite(ledPin, LOW);
  }
}

double readSetTempFromPot() {    // (7)
  int raw = analogRead(potPin);
  double temp = map(raw, 0, 1023, minTemp, maxTemp);
  return temp;
} 

double readTemp() {
  sensors.requestTemperatures(); 
  return sensors.getTempCByIndex(0);  
}
