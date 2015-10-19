const int controlPin = 9;

void setup() {                    // (1)
  pinMode(controlPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Enter Duty Cycle (0 to 100)");
}

void loop() {                     // (2)
  if (Serial.available()) {       // (3)
    int duty = Serial.parseInt();
    if (duty < 0 || duty > 100) {  // (4)
      Serial.println("0 to 100");
    }
    else {
      int pwm = duty * 255 / 100;
      analogWrite(controlPin, pwm);
      Serial.print("duty set to ");
      Serial.println(duty);
    }
  }
}
