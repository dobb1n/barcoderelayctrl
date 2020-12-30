# barcoderelayctrl
Requirement is for a barcode presented to a usb barcode reader to trigger a 240v mains powered appliance. 

A small handheld USB barcode reader is attached to a raspberry pi zero. The code accepts any barcode and when one is presented, triggers relay 1 of 2 to on for 2s, thus a mains powered device connected through the relay will have its state changed for 2s.  

<img src=https://raw.githubusercontent.com/dobb1n/barcoderelayctrl/main/pizero%20barcode%20relay.svg>

Hardware - a pizero. a relay hat : https://www.amazon.co.uk/gp/product/B084ZLMVPX/ref=ox_sc_act_title_3?smid=A2717MKXZVZ1ZW&psc=1 connected to the GPIO header, and a usb barcode reader. 

lsusb to work out the vendor and product id of the barcode reader, then put that in your usb rules file to avoid having to sudo to read the device. 

the service file configures the python script to run as a service on raspbian lite. 

<h1>Installation instructions</h1>
<ul>
  <li>First of all connect the USB adapter to the microusb socket on the rpi - it is labelled usb. Connect the rj45 jack to a network cable and connect to the switch. </li>
  <li>Connect the barcode reader to a free usb port (it doesnt matter which one) </li>
  <li>The cable carrying the power to the appliance needs to be run through the relay. The software has been configured to use relay 1 (the relays are labelled on the pcb, and its on the left if the connectors are facing towards you). if you run it through com and nc then that means the appliance will have constant voltage until a barcode is presented, when it will go off for 2s. If you want the appliance to be off and be triggered to come on when the barcode is presented, wire the 240v main through com and NO. NC = normally closed, NO = normally open. 
  <li>connect the usb adapter to the rpi</li>
</ul>

once the pi is powered on (which should be the last thing to happen), it will take about a minute for the software to become ready (has to wait for the os to start and the service to come up). You will know its ready as the relay triggers once for 2s without a barcode. Once this has happened all should be ready to test!  

