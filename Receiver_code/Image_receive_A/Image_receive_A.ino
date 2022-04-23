// Include Libraries for Remote
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

//Initialize RF
RF24 radio(9,10); // CE, CSN Pins
const byte address[6] = "10010";

void setup() {
  Serial.begin(9600);
  Serial.println("RF Image Receive code");
  radio.begin();
  radio.openReadingPipe(1,address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
      char recvData[32] = "";
      radio.read(&recvData, sizeof(recvData));
      Serial.println(recvData);
    }
}
