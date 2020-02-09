void setup()

{

pinMode(LED_BUILTIN, OUTPUT);

Serial.begin(9600);

while (!Serial); //wait for serial port to connect, needed for native usb only

Serial.println("Input 1 to Turn LED on and 0 to off");

}

void loop() {

if (Serial.available()) //returns the number of characters (i.e. bytes of data) 
                       //which have arrived in the serial buffer and that are ready to be read.
//Serial.read() returns the first (oldest) character in the buffer and removes that byte of data from the buffer.
//So when all the bytes of data are read and no new serial data have arrived, the buffer is empty and Serial.available() will return 0.
{

int state = Serial.parseInt();//Looks for the next valid integer in the incoming serial. The function terminates if it times out

if (state == 1)

{

digitalWrite(LED_BUILTIN, HIGH);

Serial.println("Command completed LED turned ON");

}

if (state == 0)

{

digitalWrite(LED_BUILTIN, LOW);

Serial.println("Command completed LED turned OFF");

}

}

}
