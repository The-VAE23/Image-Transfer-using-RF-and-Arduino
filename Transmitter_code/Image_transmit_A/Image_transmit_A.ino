// Include Libraries for Remote
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

//Initialize RF
RF24 radio(9,10); // CE, CSN Pins
const byte address[6] = "10010";

int stat=0;
String data="";
bool control=false;

void setup() {
  Serial.begin(9600);
  Serial.println("RF Image Transmit code");
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();

}

void loop() {
  if (Serial.available() > 0 && stat <1) {
    data = readSerialString();
    if (data == "2"){
      stat = 2;
    }
  }

  switch (stat){
    case 0:
      break;
    case 2:
      if (!control){
        sendRF("IMG");
        control = true;
        Serial.println(1);
      }
      else {
        if (Serial.available()){
          data=readSerialString();
          if (data !="e"){
            sendRF(data);
            Serial.println(1);
          }
          else {
            stat=0;
            sendRF("e");
          }
        }          
      }
      break;
  }

}

String readSerialString() {                        // Function that returns SerialData as String

  String output;                                // String to output

  while (Serial.available()) {
    delay(2);                                   // Delay to allow buffer to fill
    char c = char(Serial.read());               // Reading one byte from serial as char
    output += c;                                // Appending char to string
  }
  return output;
}

void sendRF(String str){
  char buf[32];
  str.toCharArray(buf,32);
  radio.write(&buf, sizeof(buf));
}
