const int redPin = 11;           // (1)
const int orangePin = 10;
const int greenPin = 9;

void setup() {                    // (2)
  pinMode(redPin, OUTPUT);
  pinMode(orangePin, OUTPUT);  
  pinMode(greenPin, OUTPUT);  
}

void loop() {                 // (3)
  setLEDs(1, 0, 0);
  delay(3000);
  setLEDs(1, 1, 0);
  delay(500);
  setLEDs(0, 0, 1);
  delay(5000);
  setLEDs(0, 1, 0);
  delay(500);
}
  
void setLEDs(int red, int orange, int green) {   // (4)
 digitalWrite(redPin, red);
 digitalWrite(orangePin, orange);
 digitalWrite(greenPin, green);
}
