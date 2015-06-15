# #############################################################################################################################
# ########################################## SERIAL COMMUNICATION #############################################################
# #############################################################################################################################
import time
import serial
import serial.tools.list_ports as AvailablePorts
# #############################################################################################################################
# ########################################## GET SERIAL PORT ##################################################################
# #############################################################################################################################
def getSerialPort(Parameter_Key_Word):
    # Observing the serial port for the keyword
    while True:    
    	# Run, until a port has been found
        if len(list(AvailablePorts.comports())) > 0:
        	# Get the port list
            for X in list(AvailablePorts.comports()):
            	# Check, if the Arduino board is on the serial port
                if Parameter_Key_Word in X[1]:
                    # Delay is neccessary, otherwise it won't work
                    time.sleep(0.1)
                    # Return the port name
                    return str(X[0])
                else:
                    pass
        else:
            pass
# #############################################################################################################################
# ########################################## MAIN #############################################################################
# #############################################################################################################################
if __name__ == "__main__":

    print "\n  Waiting for Arduino Uno on serial port."
    # Watch the serial port for the arduino
    Serial_Port      = getSerialPort("Arduino Uno")
    Serial_Baud_Rate = 9600
    
    print "\n  Arduino has been found, initializing serial communication."
    # If the arduino is available, initialize the communication
    Serial_Communication = serial.Serial(str(Serial_Port), int(Serial_Baud_Rate))
    # The arduino restarts during the initializion, wait this time
    time.sleep(1.5)
    
    raw_input("\n  Press ENTER to send message.")
    # Send the data block
    Serial_Communication.write("DATA_FROM_PC" + "\n")
    # Wait until the arduino answers
    while True:
        Serial_Input = Serial_Communication.readline()
        if "DATA_FROM_ARDUINO" in Serial_Input:
            print "\n  Serial input:", Serial_Input,
            break;
    
    raw_input("\n  Press ENTER to end communication.")
    # End the serial communication        
    Serial_Communication.close()
# #############################################################################################################################
# ########################################## END OF CODE ######################################################################
# #############################################################################################################################