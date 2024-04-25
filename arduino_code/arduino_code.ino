int val = 0;
void setup() {
  Serial.begin(9600); 
  pinMode(2, INPUT);          
  digitalWrite(2, HIGH);

}

void loop() {
  val = digitalRead(2);
  Serial.write(45);
  delay(2);
}
