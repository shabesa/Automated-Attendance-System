# Automated-Attendance-System

This project uses python and image recognition to identify the faces of students from the images of the students. It verifies the entry using rfid tags and marks the attendance in a csv file which can be opened in Excel Software. The same file is mailed to the designated email id. It can also plot the data into a graph for a given month

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
    firebase_admin
    matplotlib

### Hardware

    Arduino Uno
    Arduino Mega
    RFID Reader
    TFT Module

## Usage

### Different modules of the project use different python files  

#### Run the main.py to start the attendance system

#### To map the rfid tag with the us the add_card.py

## !!! EXTRAS

### This project is integrated with firebase and to an Mobile app

#### Check out the app here

- [Flutter APP](https://github.com/shabesa/Attendance_Viewer)

## Requirements

### Run this line to install the required modules

#### Windows -

    pip install -r requirements.txt

#### Others -

    pip3 install -r requirements.txt

## Circuit Connections

Note: IQR pin is not use in both cases!!!

### Mega Rfid Connection

| Module Pin | Board Pin |
|    ---     |    ---    |
|  Vin/3.3V  |    3.3V   |
|   Reset    |     5     |
|    Gnd     |    Gnd    |
|   MISO     |    50     |
|   MOSI     |    51     |
|    SCK     |    52     |
|    SDA     |    53     |

![Mega](<https://github.com/shabesa/Automated-Attendance-System/blob/main/circuit/rfid_mega.jpg?raw=true>)

### Uno Rfid Connection

| Module Pin | Board Pin |
|    ---     |    ---    |
|  Vin/3.3V  |    3.3V   |
|   Reset    |     9     |
|    Gnd     |    Gnd    |
|   MISO     |    12     |
|   MOSI     |    11     |
|    SCK     |    13     |
|    SDA     |    10     |

![Uno](<https://github.com/shabesa/Automated-Attendance-System/blob/main/circuit/rfid_uno.jpg?raw=true>)
