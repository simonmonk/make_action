const int in1Pin = 10;
const int in2Pin = 9;

const long crushTime = 30000;  // (1)

void setup() {     // (2)
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  
  crush();
  stop();
  delay(1000);
  reverse();
  stop();
}

void loop() {    
}

void crush()      // (3)
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, HIGH);   
  delay(crushTime);
}

void reverse()   // (4)
{
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  delay(crushTime);
}

void stop()       // (5)   
{
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
}
