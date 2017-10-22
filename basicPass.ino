void setup(){

	Serial.begin(9600);

}

void loop(){

	int signal = analogRead(A0);
	Serial.println(signal);
  delay(200);
	
}
