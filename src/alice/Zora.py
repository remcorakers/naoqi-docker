import time
from naoqi import ALProxy
import qi

class Zora:

    def __init__(self, alice):
        self.alice = alice

        self.SENSITIVTY = 0.85      # The sensitivity of the microphone sensor.
        self.IP = alice.ZORA_IP     # The IP Address of the Zora Robot.
        self.session = qi.Session()
        self.session.connect(alice.ZORA_IP + ":9559")

        # Set up all the Proxies.
        # A lit of available Proxies is available at Github.

        # self.sr_service = self.session.service("ALSpeechRecognition")
        self.tts_service = self.session.service("ALTextToSpeech")
        self.tts_service.setParameter("defaultVoiceSpeed", 50)
        self.tts_service.setLanguage("Dutch")
        self.posture_service = self.session.service("ALRobotPosture")
        self.memory = self.session.service("ALMemory")
        self.ttsProxy = ALProxy("ALTextToSpeech", self.IP, 9559)
        self.postureProxy = ALProxy("ALRobotPosture", self.IP, 9559)
        # self.sound_detect_service = self.session.service("ALSoundDetection")
        # self.sound_detect_service.setParameter("Sensitivity", self.SENSITIVTY)

    # Detects sound levels
    def detectSound(self):
        print("DETECTING")
        self.sound_detect_service.subscribe("TEST_SOUND")
        subscriber = self.memory.subscriber("SoundDetected")
        subscriber.signal.connect(self.alice.onSoundDetected) # onSoundDetected is the callback
        time.sleep(3)
        self.sound_detect_service.unsubscribe("TEST_SOUND")
        print("STOPPING")

    # Text-To-Speech
    def talk(self, sentence):
        self.tts_service.say(sentence)

    # Change position
    def goToPosture(self, posture):
        self.postureProxy.goToPosture(posture, 1.0)

    # Gets the current position
    def getPosture(self):
        print(self.posture_service.getPostureFamily())
        return self.posture_service.getPostureFamily()

    # Speech-To-Text
    def recognize(self, vocabulary):
        # self.sr_service.setVocabulary(vocabulary, False)
        # self.sr_service.subscribe("TEST_ASR")
        subscriber = self.memory.subscriber("WordRecognized")
        subscriber.signal.connect(self.alice.onReceivedWord) # onReceivedWord is the callback
        time.sleep(5)
        # self.sr_service.unsubscribe("TEST_ASR")
