
from led import LED

SHORT = 0.2
LONG = SHORT*3
PIN = 15
class Morse:
    def __init__(self) -> None:
        self._morse = {
            'A': [SHORT, LONG, 0, 0], 
            'B': [LONG, SHORT, SHORT, SHORT], 
            'C': [LONG, SHORT, LONG, SHORT], 
            'D': [LONG, SHORT, SHORT, 0], 
            'E': [SHORT, 0, 0, 0], 
            'F': [SHORT, SHORT, LONG, SHORT], 
            'G': [LONG, LONG, SHORT, 0], 
            'H': [SHORT, SHORT, SHORT, SHORT], 
            'I': [SHORT, SHORT, 0, 0], 
            'J': [SHORT, LONG, LONG, LONG], 
            'K': [LONG, SHORT, LONG, 0], 
            'L': [SHORT, LONG, SHORT, SHORT], 
            'M': [LONG, LONG, 0, 0], 
            'N': [LONG, SHORT, 0, 0], 
            'O': [LONG, LONG, LONG, 0], 
            'P': [SHORT, LONG, LONG, SHORT], 
            'Q': [LONG, LONG, SHORT, LONG], 
            'R': [SHORT, LONG, SHORT, 0], 
            'S': [SHORT, SHORT, SHORT, 0], 
            'T': [LONG, 0, 0, 0], 
            'U': [SHORT, SHORT, LONG, 0], 
            'V': [SHORT, SHORT, SHORT, LONG], 
            'W': [SHORT, LONG, LONG, 0], 
            'X': [LONG, SHORT, SHORT, LONG], 
            'Y': [LONG, SHORT, LONG, LONG], 
            'Z': [LONG, LONG, SHORT, SHORT], 
            }
        self._led = LED(PIN)
    
    @staticmethod
    def get_timeunit():
        return SHORT
        
    def get_morsetime(self, char:str):
        return self._morse[char]
