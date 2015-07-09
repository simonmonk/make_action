#include <OneWire.h>
#include <DallasTemperature.h>

const int tempPin = 2;
const int heatPin = 9;
const long period = 1000; 

OneWire oneWire(tempPin);
DallasTemperature sensors(&oneWire);

float setTemp = 0.0;
long lastSampleTime = 0;

void setup() {
  pinMode(heatPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("t30 - sets the temperature to 30");
  sensors.begin();
}

void loop() { 
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 't') {
      setTemp = Serial.parseInt();
      Serial.print("Set Temp=");
      Serial.println(setTemp);
    }
  }
  long now = millis();
  if (now > lastSampleTime + period) {
    lastSampleTime = now;
    float measuredTemp = readTemp();
    float error = setTemp - measuredTemp;
    Serial.print(measuredTemp);
    Serial.print(", ");
    Serial.print(setTemp);
    if (error > 0) {
        digitalWrite(heatPin, HIGH);
        Serial.println(", 1");
    }
    else {
      digitalWrite(heatPin, LOW);
      Serial.println(", 0");
    }
  }
}

float readTemp() {
  sensors.requestTemperatures(); 
  return sensors.getTempCByIndex(0);  
}
