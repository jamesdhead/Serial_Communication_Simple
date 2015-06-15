#####Arduino file:

Created with Sublime Text 3 & Stino (Arduino IDE 1.0.5).
Deviations may be followed by errors.

#####Python file:

Created with Sublime Text 3, tested with Python 2.

#####How it works

The Python script waits for the Arduino Uno on the serial port. If it's available, the serial communication will be initialized. Please note that this part of the code is written for Windows OS. You can change this part of the code very quick, because it is an own function. The rest of the code is for every platform.
After this, the script sends a message to the Arduino board which will receive the message as a string. After the processing of this string, the Arduino will send a message back, which is awaited by the Python script.

This is all, just a basic communication.