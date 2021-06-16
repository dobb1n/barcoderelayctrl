from usb_barcode_scanner.scanner import barcode_reader
import re
import time
import RPi.GPIO as GPIO

def relay_control(interval):
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(4, GPIO.OUT) #set Relay 1 output 
    GPIO.setup(17, GPIO.OUT) #set Relay 2 output
    GPIO.output(4, GPIO.HIGH) #turn relay 1 on
    time.sleep(interval) 
    GPIO.output(4, GPIO.LOW) #turn relay 1 off

def barcode_checker(barcode):
    match = re.match(r"^\d{13}$", barcode)
    if match:
        return True

if __name__ == '__main__':
    try:
        while True:
            upcnumber = barcode_reader()
            if barcode_checker(upcnumber):
                print(upcnumber, "one of ours, open the doors")
                relay_control(2)
    except KeyboardInterrupt:
        logging.debug('Keyboard interrupt')
    except Exception as err:
        logging.error(err)