#include <OneWire.h>
#include <DallasTemperature.h>
#include <PID_v1.h>

const double minTemp = 0.0;  
const double maxTemp = 20.0;
const float tempOKMargin = 0.5; 

double kp = 1500;     
double ki = 50.0;
double kd = 0.0;

const int tempPin = 2;
const int coolPin = 9;
const int ledPin = 10;       
const int potPin = A0;
const long period = 1000; // >750

OneWire oneWire(tempPin);
DallasTemperature sensors(&oneWire);

double setTemp = 0.0;
double measuredTemp = 0.0;
double outputPower = 0.0;     
long lastSampleTime = 0;

PID myPID(&measuredTemp, &outputPower, &setTemp, kp, ki, kd, REVERSE); 

void setup() {
  pinMode(coolPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  sensors.begin();
  myPID.SetSampleTime(1000); // (4)
  myPID.SetMode(AUTOMATIC);  
}

void loop() { 
  long now = millis();         
  if (now > lastSampleTime + period) {
      checkTemperature();
      lastSampleTime = now;
  }
  setTemp = readSetTempFromPot(); 
}

void checkTemperature() {      
  measuredTemp = readTemp();  
  Serial.print(measuredTemp);
  Serial.print(", ");
  Serial.print(setTemp);
  Serial.print(", ");
  Serial.println(outputPower);
  myPID.Compute();
  analogWrite(coolPin, outputPower);
  float error = setTemp - measuredTemp;
  if (abs(error) < tempOKMargin) {        
    digitalWrite(ledPin, HIGH);
  }
  else {
    digitalWrite(ledPin, LOW);
  }
}

double readSetTempFromPot() {   
  int raw = analogRead(potPin);
  double temp = map(raw, 0, 1023, minTemp, maxTemp);
  return temp;
} 

double readTemp() {
  sensors.requestTemperatures(); 
  return sensors.getTempCByIndex(0);  
}
