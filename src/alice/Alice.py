import time
import json
from Zora import Zora

class Alice:

    def __init__(self):
        self.ZORA_IP = "169.254.58.192"
        print("Starting Program for Alice")
        self.zora = Zora(self)
        self.run()

    def run(self):
        self.zora.goToPosture("Stand")
        time.sleep(1)
        self.zora.talk("Ik ben nu vrienden met \\emph=2\\Frenklin\\emph=0\\ op Facebook.")
        time.sleep(2)
        self.zora.talk("Ik ga even zitten.")
        self.zora.goToPosture("Sit")
        time.sleep(2)
        self.zora.talk("Je kleinzoon Frenklin heeft een \\emph=2\\foto\\emph=0\\ geplaatst.")
        time.sleep(4)
        # Wat voor foto?
        self.zora.talk("Een foto op de Digital Days in Oost West en Middelbeers.")
        time.sleep(3)
        # Wat staat er op de foto?
        self.zora.talk("Frenklin die gepassioneerd zingt.")
        time.sleep(1)
        self.zora.talk("Wil je de foto zien?")
        time.sleep(3)
        # Ja leuk!
        self.zora.talk("Heb je je eipet bij de hand?")
        time.sleep(3)
        # Nee die heb ik niet.
        self.zora.talk("Zal ik de foto als ansichtkaart laten vesturen?")
        time.sleep(3)
        # Ja graag.
        self.zora.talk("Ok, je krijgt straks een kaartje.")
        time.sleep(15)
        self.zora.talk("Zullen we Frenklin straks bellen om te vragen hoe het was?")

Alice()
