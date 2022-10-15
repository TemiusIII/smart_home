int data;
int LED = 13;
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite (LED, LOW);

}
String full_data = "", command = "";
void loop() {
  
  while (Serial.available())
  {
    data = Serial.read();
    if (data != 13)
      full_data += data;
     else {
      Serial.println(full_data);
      command = full_data;
      full_data = "";
  }

  }
  if (command == "on")
    digitalWrite (LED, HIGH);
  else if (command == "off")
    digitalWrite (LED, LOW);
}
