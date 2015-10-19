const int popPin = 11;

const int minDelay = 20;   // Seconds (1)
const int maxDelay = 200;  // Seconds
const int onTime = 15;     // Seconds (2)

void setup() {
  pinMode(popPin, OUTPUT);
  randomSeed(analogRead(0));   // (3)
  long pause = random(minDelay, maxDelay+1);   // (4)
  delay(pause * 1000);             // (5)
  digitalWrite(popPin, HIGH);      // (6)
  delay(onTime * 1000);
  digitalWrite(popPin, LOW);
}

void loop() {
}
