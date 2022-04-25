import RPi.GPIO as GPIO
import time
class LED:
    def __init__(self, pin, selected=False):
        self.pin = pin
        self._selected = selected
        self._set_pin_mode()
        
        if self._selected:
            self._led_on()
        else: self._led_off()
            
    def _set_pin_mode(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
            
    def _led_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def _led_off(self):
        GPIO.output(self.pin, GPIO.LOW)
    
    def click(self):
        self._led_on()
        self._selected = True
        
    def unclick(self):
        self._led_off()
        self._selected = False

    @staticmethod
    def wait(time_unit):
        time.sleep(time_unit)