# barcoderelayctrl
Requirement is for a valid barcode presented to an alacrity usb barcode reader connected to a pizero to control a relay which in turn is used to control a magnetic lock for a door. The barcode reader accepts any barcode and then on success triggers relay 1 of 2 to on for 2s. 

Hardware - a pizero. a relay hat : https://www.amazon.co.uk/gp/product/B084ZLMVPX/ref=ox_sc_act_title_3?smid=A2717MKXZVZ1ZW&psc=1 connected to the GPIO header, and a usb barcode reader. 

lsusb to work out the vendor and product id of the barcode reader, then put that in your usb rules file to avoid having to sudo to read the device. 

the service file configures the python script to run as a service on raspbian lite. 
