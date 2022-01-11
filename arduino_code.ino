int data;
int LED = 13;
void setup() {
  Serial.begin(9600);                               //initialize serial COM at 9600 baudrate
  pinMode(LED, OUTPUT);                    //declare the LED pin (13) as output
  digitalWrite (LED, LOW);                     //Turn OFF the Led in the beginning

  Serial.println("Hello!,How are you Python ?");
}
String full_data = "", command = "";
void loop() {
  
  while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”
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
  if (command == "111110")
    digitalWrite (LED, HIGH);                  //Turn On the Led
  else if (command == "111102102")
    digitalWrite (LED, LOW);                  //Turn OFF the Led
}
