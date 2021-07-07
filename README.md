# Automated-Attendance-System

This project uses python and image recognition to identify the faces of students from the images of the students. It verifies the entry using rfid tags and marks the attendance in a csv file which can be opened in Excel Software. The same file is mailed to the designated email id

## Software

    Python
    Arduino

## MODULES USED

### Python Libraries

    Face_recognition
    Pyttsx3
    Open CV2
    Pyserial
    Tkinter
    Datetime
    Time
    CSV
    JSON

### Hardware

    Arduino Uno
    Arduino Mega
    RFID Reader
    TFT Module

## Usage

### Different modules of the project use different python files  

#### Run the main.py to start the attendance system

#### To map the rfid tag with the us the add_card.py

## Requirements

### Run this line to install the required modules

#### Windows -

    pip install -r requirements.txt

#### Others -

    pip3 install -r requirements.txt

## Circuit Connections

Note: IQR pin is not use in both cases!!!

### Mega Rfid Connection

![Mega](<https://github.com/shabesa/Automated-Attendance-System/blob/main/circuit/rfid_mega.jpg?raw=true>)

### Uno Rfid Connection

![Uno](<https://github.com/shabesa/Automated-Attendance-System/blob/main/circuit/rfid_uno.jpg?raw=true>)


