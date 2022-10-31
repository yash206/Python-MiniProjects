import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyttsx3
import smtplib
import cv2
import imutils
import pytube
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# Mics and voices
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Assistant")
        icon = QIcon('icon.jpg')
        self.setWindowIcon(icon)
        self.setGeometry(500, 300, 500, 500)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        w = QPushButton(self)
        w.setGeometry(200, 200, 200, 200)
        w.clicked.connect(self.clickme)
        w.setStyleSheet("background-image : url(mic.png); \
        background-repeat : no-repeat;border : 2px solid blue;"
                        " border-radius : 100px;background-position : center;background-color : white")

    def clickme(self):
        run_alexa()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('How would I help you.')
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'uncle john' in command:
                command = command.replace('uncle john', '')
                print('Command :' + command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        print('     playing' + song)
        pywhatkit.playonyt(song)

    elif ('hello' or 'hi') in command:
        print('Hi...')
        talk('Hi')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('     Current time is ' + time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'search' in command:
        topic = command.replace('search', '')
        print('     searching ' + topic)
        pywhatkit.search(topic)
        talk('Searching' + topic)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'whatsapp' in command:
        receiver = input("Enter Receiver whatsapp no. : ")
        msg = input('Enter the message : ')
        hour = int(datetime.datetime.now().strftime('%H'))
        minute = int(datetime.datetime.now().strftime('%M'))+1
        pywhatkit.sendwhatmsg(receiver, msg, hour, minute)
        print('     Sending message...... ')
        talk('Sending message to Receiver')

    elif 'mail' in command:
        server.login('agaryash1008@gmail.com', 'yash@123')
        receiver_address = input("Enter Receiver's Email Address :  ")
        message = input("Enter the Message :  ")
        server.sendmail('agaryash1008@gmail.com', receiver_address, message)
        talk('Sent Email to desired location')

    elif 'camera' in command:
        print('      Turning ON video camera')
        talk('Turning ON video camera')

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            frame = imutils.resize(frame, width=800, height=1200)
            cv2.imshow('Video', frame)
            if cv2.waitKey(10) == ord('c'):
                break

            cap.release()
            cv2.destroyAllWindows()

    elif 'download' in command:
        print("Enter the URL of the YouTube video to be downloaded")
        talk("Please enter the URL of the YouTube video to be downloaded")
        url = input()
        video = pytube.YouTube(url).streams.get_lowest_resolution()
        video.download()
        print("Video Downloaded Successfully!!!!")
        talk("Video Downloaded Successfully!!!!")

    else:
        print("Please say the command again.")
        talk("Please say the command again.")


window = Window()
sys.exit(app.exec())
