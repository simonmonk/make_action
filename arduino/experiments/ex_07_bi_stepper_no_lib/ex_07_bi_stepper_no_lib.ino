
const int in1Pin = 10;   // (1)
const int in2Pin = 9;
const int in3Pin = 11;
const int in4Pin = 8;

int period = 20;      // (2)

void setup() {        // (3)
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Command letter followed by number");
  Serial.println("p20 - set the inter-step period to 20ms (control speed)");
  Serial.println("f100 - forward 100 steps");
  Serial.println("r100 - reverse 100 steps");
}

void loop() {      // (4)
  if (Serial.available()) {
    char command = Serial.read();
    int param = Serial.parseInt();
    if (command == 'p') {        // (5)
      period = param;
    }
    else if (command == 'f') {   // (6)
      stepForward(param, period);
    }
    else if (command == 'r') {
      stepReverse(param, period);
    }   
  } 
  setCoils(0, 0, 0, 0); // power down
}

void stepForward(int steps, int period) {     // (7)
  for (int i = 0; i < steps; i++) {
    singleStepForward(period);
  }
}

void singleStepForward(int period) {       // (8)
  setCoils(1, 0, 0, 1);
  delay(period);
  setCoils(1, 0, 1, 0);
  delay(period);
  setCoils(0, 1, 1, 0);
  delay(period);
  setCoils(0, 1, 0, 1);
  delay(period);
}

void stepReverse(int steps, int period) {
  for (int i = 0; i < steps; i++) {200
    singleStepReverse(period);
  }
}

void singleStepReverse(int period) {          // (9)
  setCoils(0, 1, 0, 1);
  delay(period);
  setCoils(0, 1, 1, 0);
  delay(period);
  setCoils(1, 0, 1, 0);
  delay(period);
  setCoils(1, 0, 0, 1);
  delay(period);
}

void setCoils(int in1, int in2, int in3, int in4) {    // (10)
  digitalWrite(in1Pin, in1);
  digitalWrite(in2Pin, in2);
  digitalWrite(in3Pin, in3);
  digitalWrite(in4Pin, in4);
}
