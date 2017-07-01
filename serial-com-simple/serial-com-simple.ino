// #####################################################################################################################
// ######################################### SERIAL COMMUNICATION ######################################################
// ##################################################################################################################### 
/*
	This is the very basic code for a running serial communication.

	The serialEvent() is called after the loop.
*/
void setup()
{
	// Setup serial communication at baud rate: 9600
	Serial.begin(9600);
}

void loop()
{
	// Nothing to do here
}

void serialEvent()
{
	if (Serial.available())
	{
		// Get serial input
		String Serial_Input = Serial.readStringUntil('\n');
		// Otherwise send back the input
		if (Serial_Input == "DATA_FROM_PC")
			Serial.print("DATA_FROM_ARDUINO\n");
		// If nothing matches, do nothing
		else
			Serial.read();
		/*
			If you want to shorten your code, you can also write the if-else condition as:

			Serial_Input == "DATA_FROM_PC" ? Serial.print("DATA_FROM_ARDUINO\n") : Serial.read();

			As you see, I used the ternary operator: 

				condition ? true : false;

			By the way, I really like this operator, even if it doesn't make the code more readable, but it looks nice.
		*/
	}
}