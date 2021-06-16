# barcoderelayctrl
Requirement is for a barcode presented to a usb barcode reader to trigger a 240v mains powered appliance. 

A handheld, USB attached barcode reader is connected to a raspberry pi zero (or raspberry pi). The pi also has a relay hat fitted. I used (vpatron's FT245r repo)[https://github.com/vpatron/relay_ft245r] with the first relay hat, and the second time, it was (this relay hat from pi hut)[https://thepihut.com/products/raspberry-pi-zero-relay-hat], and i used (this guide)[https://bc-robotics.com/tutorials/getting-started-raspberry-pi-relay-hat/] which says >Conveniently, the software library we need is included in the default Raspbian image. We won’t need to do much configuration in this tutorial to control the HAT! 

(Which is great! It goes on to suggest using python2.7, but we aren't backwards) We can just import RPi.GPIO and control the relay with the GPIO header pins! 

The idea is that, a barcode is presented to the reader, it is checked against a rule or series of rules and then triggers one of the relays for 2s. So for instance presentation of a specific barcode would allow a light to go on, or a magnetic door lock to be released, or something... 

<img src=https://raw.githubusercontent.com/dobb1n/barcoderelayctrl/main/pizero%20barcode%20relay.svg>

## Hardware
* a pizero. 
* a (relay hat)[https://thepihut.com/products/raspberry-pi-zero-relay-hat] 
* A usb barcode reader. 

I have managed to get this working on a couple of different types of barcode reader. The first was a cheap handheld alacrity thing from amazon. It worked fine and i used (vPatron's barcode reader)[https://github.com/vpatron/barcode_scanner_python] to control the input from the usb device. The second time it was another alacrity reader, but i found it easier to control with (this one )[https://github.com/julzhk/usb_barcode_scanner.git]. With both, some jiggery pokery was required to avoid having to escalate to get control of the device. (This was useful)[https://doc.sccode.org/Guides/HID_permissions.html]

the service file configures the python script to run as a service on raspbian lite. 

## Installation instructions

* find somewhere for the pi to sit which isnt conductive!
* First of all connect the USB adapter to the microusb socket on the rpi - it is labelled usb. Connect the rj45 jack to a network cable and connect to the switch.
* Connect the barcode reader to a free usb port (it doesnt matter which one)
* The cable carrying the power to the appliance needs to be run through the relay. The software has been configured to use relay 1 (the relays are labelled on the pcb, and its on the left if the connectors are facing towards you). if you run it through com and nc then that means the appliance will have constant voltage until a barcode is presented, when it will go off for 2s. If you want the appliance to be off and be triggered to come on when the barcode is presented, wire the 240v main through com and NO. NC = normally closed, NO = normally open. 
* Being careful not to touch any connectors on the pi - connect the usb adapter to the rpi


once the pi is powered on (which should be the last thing to happen), it will take about a minute for the software to become ready (has to wait for the os to start and the service to come up). You will know its ready as the relay triggers once for 2s without a barcode. Once this has happened all should be ready to test!  

<img src=https://github.com/dobb1n/barcoderelayctrl/blob/main/IMG_3216.jpeg>
