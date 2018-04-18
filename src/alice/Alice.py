import time
import json
from Zora import Zora

class Alice:

    def __init__(self):
        self.answers = []

        # This depends on what Zora robot you have. Make sure the robot is connected (through UTP-cable).
        self.ZORA_IP = "host.docker.internal"

        print("Starting Program for Alice")
        # Connect to Zora
        self.zora = Zora(self)
        self.run()

    def run(self):
        self.stand()
        # self.zora.talk("Hey, I can talk.")
        # self.conversation()
        # self.stand()

    def conversation(self):
        # The Zora robot has built-in text to speech (TTS):
        self.zora.talk("I will ask a question. You can answer me by responding with yes or no. Are you ready?")
        # The Zora robot also has a (limited by one word) built in speech to text (STT):
        self.recognizedWord = ""
        vocabulary = ["yes", "no"] # The range of words that Zora should be able to recognize. For this example this is only yes or no.
        self.zora.recognize(vocabulary)
        self.answers = self.recognizedWord
        print(self.recognizedWord)
        if self.answers == "yes":
            self.zora.talk("You said yes")
        elif self.answers == "no":
            self.zora.talk("You said no")
        else:
            self.zora.talk("I didn't hear you say anything.")

    def stand(self):
        # Find more at: http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html
        self.posture_service.goToPosture("Stand")

    def onReceivedWord(self, word):
        if(word[1] > 0.3):
            self.recognizedWord = word[0]

Alice()
