const int enablePin = 11;
const int in1Pin = 10;
const int in2Pin = 9;

void setup() {
  pinMode(enablePin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Enter s (stop) or f or r followed by Duty Cycle (0 to 255). E.g. f120");
}

void loop() {
  if (Serial.available()) {
    char direction = Serial.read();
    if (direction == 's') {
      stop();
      return;
    }
    int pwm = Serial.parseInt();
    if (direction == 'f') {
      forward(pwm);
    }
    else if (direction == 'r') {
      reverse(pwm);
    }
  }
}

void forward(int pwm)
{
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  analogWrite(enablePin, pwm);    
  Serial.print("Forward ");
  Serial.println(pwm);
}

void reverse(int pwm)
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, HIGH);
  analogWrite(enablePin, pwm);
  Serial.print("Reverse ");
  Serial.println(pwm);
}

void stop()
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  analogWrite(enablePin, 0);
  Serial.println("Stop");
}
