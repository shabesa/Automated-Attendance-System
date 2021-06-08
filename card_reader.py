from cv2 import data
import serial
from time import sleep


class Reader:
    
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.board = serial.Serial(port, baudrate)
        print(self.board)

    def read(self):
        while True:
            data = self.board.readline().decode()
            # print(data)
            return data
