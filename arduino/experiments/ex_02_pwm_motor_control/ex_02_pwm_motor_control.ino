// Experiment 2. PWM Motor Control

const int motorPin = 9;

void setup() {
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Enter Duty Cycle (0 to 100)");
}

void loop() {
  if (Serial.available()) {
    int duty = Serial.parseInt();
    if (duty < 0 || duty > 100) {
      Serial.println("0 to 100");
    }
    else {
      int pwm = duty * 255 / 100;
      analogWrite(motorPin, pwm);
      Serial.print("duty set to ");
      Serial.println(duty);
    }
  }
}
