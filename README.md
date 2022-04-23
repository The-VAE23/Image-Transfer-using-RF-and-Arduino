# Image-Transfer-using-RF-and-Arduino
This repo stores and documents the code required for transmitting an image over RF. This code is a Proof of Concept and might not be optimal to use for commercial applications

The code consits of two parts the receiver and transmitter codes. To use, make the necessary circuit on the Arduino's and upload one of the Arduinos with the transmitter code and one with the receiver code. Note the port in the Arduino IDE during the upload process.

Once uploaded launch the pyhton program for the respective boards and change the port in the code to match the one shown in Arduino IDE. Make sure the path points to a valid directory and the image being read exists in the location.

Launch the reciver code and wait for a print from the Arduino. Once the arduino print is done, the code can be exited by pressing the 'q' key. Run the transmitter code once the receiver is setup. The code prints the current pixel sent/total pixels in the image during operation. The transfer speed is limited by the serial connection and in my testing was observed around 83-89 px/sec.

Once image is received the image will be saved with current date and time as its name and the code will print an acknowledgement of the same.

Supported image sizes are,

16:9 - 240p,360p,480p,720p,1080p

4:3 - 480p,600p,720p,768p,960p,1050p,1080p

Sample image 135x180p
