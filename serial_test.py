#Import serial control module
#read the docs at https://pyserial.readthedocs.io/en/latest/shortintro.html
import serial
import time

#initialise a serial port (name of port, baud rate). The name will likely be different on your computer
ser = serial.Serial('/dev/cu.usbmodem14101',9600) # open serial port
print(ser.name)         # check which port was really used

#read initial serial message
answer = ser.readline() # read a '\n' terminated line
print(answer.decode('utf-8')) #transform the unicode to readable code


#turn LED off and on in infinite loop
LED_status = 1
while True: #infinite loop 
    LED_status = int(not LED_status) #close led
    command = str(LED_status) #string of status
    print(f'Sent: {command}') #f-strings: formatted string literal, and write 
                              #expressions in {}
    ser.write(command.encode('utf-8'))#write the command above after change it into utf-8
    response = ser.readline() #read in the status of port
    print(f'Response: {response.decode("utf-8")}')
    time.sleep(1) #Suspend execution of the loop for the given number of seconds.



