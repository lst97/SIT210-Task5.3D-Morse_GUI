import RPi.GPIO as GPIO
from tkinter import *
from morse import Morse
from led import LED

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('SIT210 - Task5.3D')
        self._led = LED(15)
        self._main_panel = Canvas(self.root, width = 200, height = 200) # main screen
        self._main_panel.pack()
        self._entry_text = StringVar()
        self._morse = Morse()
    
    def _led_controller(self, str_var):
        self.root.withdraw()
        string = str_var.get().upper()
        print('Blinking... "{}"'.format(string))
        for char in string:
                try:
                    for delay in self._morse.get_morsetime(char):
                        if delay == 0: continue

                        self._led.click()
                        self._led.wait(delay)
                        self._led.unclick()
                        self._led.wait(self._morse.get_timeunit())
                except KeyError:
                        print('Exception: Unknow Morse Character "{}", Blinking STOP!'.format(char))
                        break
        print("Done!")
        self._entry_text.set("")
        self.root.deiconify()
        
    @staticmethod
    def _character_limit(entry_text):
        if len(entry_text.get()) > 0:
                try:
                        entry_text.set(entry_text.get()[12])
                except IndexError:
                        # know issue
                        pass

    def _quit(self):
        GPIO.cleanup()
        self.root.quit()
            
    def start(self):
        label_title = Label(self.root, text="SIO TOU LAI - 220619375")
        label_title.pack()

        entry_widget = Entry(self.root, width = 20, textvariable=self._entry_text)
        self._main_panel.create_window(100, 20, window=entry_widget)
        self._entry_text.trace("w", lambda *args: self._character_limit(self._entry_text))
        
        button_blink = Button(self.root, text="Blink", command=lambda *args: self._led_controller(self._entry_text))
        button_blink.pack()

        button_exit = Button(self.root, text="Exit", command=self._quit)
        button_exit.pack()

        self.root.mainloop()

GUI().start()
