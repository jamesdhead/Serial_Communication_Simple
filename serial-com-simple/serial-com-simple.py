# ######################################################################################################################
# ########################################## SERIAL COMMUNICATION ######################################################
# ###################################################################################################################### 
import time
import serial
import serial.tools.list_ports as AvailablePorts

def getSerialPort(keyword):
    # Observing the serial port for the keyword
    while True:    
    	# Run, until a port has been found
        if len(list(AvailablePorts.comports())) > 0:
        	# Get the port list
            for i in list(AvailablePorts.comports()):
            	# Check, if the Arduino board is on the serial port
                if keyword in i[1]:
                    # Delay is neccessary for a stable communication
                    time.sleep(0.1)
                    # Return the port name
                    return str(i[0])
                else:
                    pass
        else:
            pass
 
if __name__ == "__main__":

    print "\n  Waiting for Arduino on serial port."
    # Watch the serial port for the arduino
    serialPort = getSerialPort("Arduino Uno")
    baudRate = 9600
    
    print "\n  Arduino has been found, initializing serial communication."
    # If the arduino is available, initialize the communication
    com = serial.Serial(str(serialPort), int(baudRate))
    # The arduino restarts during the initializion, wait this time
    time.sleep(1.5)
    
    raw_input("\n  Press ENTER to send message.")
    # Send the data block
    com.write("DATA_FROM_PC" + "\n")
    # Wait until the arduino answers
    while True:
        Serial_Input = com.readline()
        if "DATA_FROM_ARDUINO" in Serial_Input:
            print "\n  Serial input:", Serial_Input,
            break;
    
    raw_input("\n  Press ENTER to end communication.")
    # End the serial communication        
    com.close()
# ###################################################################################################################### 
# ########################################## END OF CODE ###############################################################
# ###################################################################################################################### 