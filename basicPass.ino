int threshold = 400;

void setup(){

	Serial.begin(9600);

}

void loop(){

	int signal = analogRead(A0);
	Serial.print(signal);

	if(signal > threshold){
		Serial.println("Contracted");	
	}else{
		Serial.println("");
	}

}
