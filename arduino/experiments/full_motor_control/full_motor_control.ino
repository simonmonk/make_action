const int enablePin = 11;  // (1)
const int in1Pin = 10;
const int in2Pin = 9;

void setup() {                 // (2)
  pinMode(enablePin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Enter s (stop) or f or r followed by Duty Cycle (0 to 255). E.g. f120");
}

void loop() {                         // (3)
  if (Serial.available()) {
    char direction = Serial.read();   // (4)
    if (direction == 's') {           // (5)
      stop();                         // (6)
      return;
    }
    int pwm = Serial.parseInt();      // (7)
    if (direction == 'f') {           // (8)
      forward(pwm);
    }
    else if (direction == 'r') {
      reverse(pwm);
    }
  }
}

void forward(int pwm)          // (9)
{
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  analogWrite(enablePin, pwm);    
  Serial.print("Forward ");
  Serial.println(pwm);
}

void reverse(int pwm)          // (10)
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, HIGH);
  analogWrite(enablePin, pwm);
  Serial.print("Reverse ");
  Serial.println(pwm);
}

void stop()                    // (11)
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  analogWrite(enablePin, 0);
  Serial.println("Stop");
}
