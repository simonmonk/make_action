#include <OneWire.h>
#include <DallasTemperature.h>
#include <PID_v1.h>

const int tempPin = 2;
const int heatPin = 9;
const long period = 1000; // >750

double kp = 0.0;     // (1)
double ki = 0.0;
double kd = 0.0;


OneWire oneWire(tempPin);
DallasTemperature sensors(&oneWire);

double setTemp = 0.0;
double measuredTemp = 0.0;
double outputPower = 0.0;     // (2)
long lastSampleTime = 0;

PID myPID(&measuredTemp, &outputPower, &setTemp, kp, ki, kd, DIRECT); // (3)

void setup() {
  pinMode(heatPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("t30 - sets the temperature to 30");
  Serial.println("k50 20 10 - sets kp, ki and kd respectively");
  sensors.begin();
  myPID.SetSampleTime(1000); // (4)
  myPID.SetMode(AUTOMATIC);  
}

void loop() { 
  checkForSerialCommands();  // (5)
  
  long now = millis();
  if (now > lastSampleTime + period) { // (6)
    lastSampleTime = now;
    measuredTemp = readTemp();
    myPID.Compute();
    analogWrite(heatPin, outputPower);
  
    Serial.print(measuredTemp);  // (7)
    Serial.print(", ");
    Serial.print(setTemp);
    Serial.print(", ");
    Serial.println(outputPower);
  }
}

void checkForSerialCommands() {  // (8)
    if (Serial.available()) {
    char command = Serial.read();
    if (command == 't') {
      setTemp = Serial.parseFloat();
      Serial.print("Set Temp=");
      Serial.println(setTemp);
    }
    if (command == 'k') {
      kp = Serial.parseFloat();
      ki = Serial.parseFloat();
      kd = Serial.parseFloat();
      myPID.SetTunings(kp, ki, kd);
      Serial.print("Set Constants kp=");
      Serial.print(kp);
      Serial.print(" ki=");
      Serial.print(ki);
      Serial.print(" kd=");
      Serial.println(kd);
    }
  }
}

double readTemp() {
  sensors.requestTemperatures(); 
  return sensors.getTempCByIndex(0);  
}
