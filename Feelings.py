class Feeling:
    def _init_(self, situation, intensity=1, negativeMeter=100):
        self._situation = situation
        self._intensity = intensity
        self._negativeMeter = negativeMeter
        self._heartbeat = 70  # default resting heartbeat

<<<<<<< HEAD
    #initial methods
=======
>>>>>>> a1bc560c6a90890a00cd078abf1866b7e9a7708c
    def describe(self):
        pass
    
    def physicalResponse(self):
        pass
    
    def timePasses(self, days):
        pass

    def response(self, event):
        pass

    def influenceByEnv(self, environment):
        pass

<<<<<<< HEAD
#getters and setters
=======
>>>>>>> a1bc560c6a90890a00cd078abf1866b7e9a7708c
    def getSituation(self):
        return self._situation
    
    def setSituation(self, situation):
        self._situation = situation

    def getIntensity(self):
        return self._intensity

    def setIntensity(self, intensity):
        self._intensity = intensity

    def getNegativeMeter(self):
        return self._negativeMeter

    def setNegativeMeter(self, negativeMeter):
        self._negativeMeter = negativeMeter

    def getHeartbeat(self):
        return self._heartbeat

    def setHeartbeat(self, heartbeat):
        self._heartbeat = heartbeat
        
        class Happiness(Feeling):
    def describe(self):
        return "Happiness often brings a smile and a sense of joy."

    def physicalResponse(self):
        self._heartbeat += 10 * self._intensity
        return self._heartbeat

    def timePasses(self, days):
        self._intensity -= days * 0.1
        if self._intensity < 0:
            self._intensity = 0

    def response(self, event):
        if event == "win a prize":
            self._intensity += 2
        elif event == "receive bad news":
            self._intensity -= 2
            if self._intensity < 0:
                self._intensity = 0

    def influenceByEnv(self, environment):
        if environment == "party":
            self._intensity += 1
        elif environment == "funeral":
            self._intensity -= 3
            if self._intensity < 0:
                self._intensity = 0

class Anger(Feeling):
    def describe(self):
        return "Anger is characterized by frustration and often leads to a raised voice."

    def physicalResponse(self):
        self._heartbeat += 20 * self._intensity
        return self._heartbeat

    def timePasses(self, days):
        self._intensity -= days * 0.3
        if self._intensity < 0:
            self._intensity = 0

    def response(self, event):
        if event == "face injustice":
            self._intensity += 3
        elif event == "meditate":
            self._intensity -= 2
            if self._intensity < 0:
                self._intensity = 0

    def influenceByEnv(self, environment):
        if environment == "hostile":
            self._intensity += 2
        elif environment == "calm":
            self._intensity -= 1
            if self._intensity < 0:
                self._intensity = 0

                class Sadness(Feeling):
    def describe(self):
        return "Sadness can lead to tears and a feeling of loss."

    def physicalResponse(self):
        self._heartbeat -= 5 * self._intensity
        return self._heartbeat

    def timePasses(self, days):
        self._intensity -= days * 0.2
        if self._intensity < 0:
            self._intensity = 0

    def response(self, event):
        if event == "lose a loved one":
            self._intensity += 3
        elif event == "watch a comedy":
            self._intensity -= 2
            if self._intensity < 0:
                self._intensity = 0

    def influenceByEnv(self, environment):
        if environment == "rainy day":
            self._intensity += 1
        elif environment == "sunny day":
            self._intensity -= 1
            if self._intensity < 0:
                self._intensity = 0

                class Fear(Feeling):
    def describe(self):
        return "Fear makes the heart race and creates a sense of dread."

    def physicalResponse(self):
        self._heartbeat += 30 * self._intensity
        return self._heartbeat

    def timePasses(self, days):
        self._intensity -= days * 0.2
        if self._intensity < 0:
            self._intensity = 0

    def response(self, event):
        if event == "confront danger":
            self._intensity += 3
        elif event == "relax":
            self._intensity -= 2
            if self._intensity < 0:
                self._intensity = 0

    def influenceByEnv(self, environment):
        if environment == "threatening":
            self._intensity += 2
        elif environment == "calm":
            self._intensity -= 1
            if self._intensity < 0:
                self._intensity = 0
                
                class TestFeelings(unittest.TestCase):

    def setUp(self):
        # Initialize instances for testing
        self.happiness = Happiness("Celebrating", intensity=3, negativeMeter=80)
        self.anger = Anger("Facing unfair treatment", intensity=2, negativeMeter=90)
        self.sadness = Sadness("Loss of a friend", intensity=4, negativeMeter=85)
        self.fear = Fear("Encountering a threat", intensity=1, negativeMeter=95)

    def testDescribe(self):
        self.assertEqual(self.happiness.describe(), "Happiness often brings a smile and a sense of joy.")
        self.assertEqual(self.anger.describe(), "Anger is characterized by frustration and often leads to a raised voice.")
        self.assertEqual(self.sadness.describe(), "Sadness can lead to tears and a feeling of loss.")
        self.assertEqual(self.fear.describe(), "Fear makes the heart race and creates a sense of dread.")

    def testPhysicalResponse(self):
        self.assertEqual(self.happiness.physicalResponse(), 100)
        self.assertEqual(self.anger.physicalResponse(), 110)
        self.assertEqual(self.sadness.physicalResponse(), 55)
        self.assertEqual(self.fear.physicalResponse(), 100)

    def testTimePasses(self):
        self.happiness.timePasses(5)
        self.assertEqual(self.happiness.getIntensity(), 2.5)
        self.anger.timePasses(3)
        self.assertEqual(self.anger.getIntensity(), 0)
        self.sadness.timePasses(2)
        self.assertEqual(self.sadness.getIntensity(), 3.6)
        self.fear.timePasses(4)
        self.assertEqual(self.fear.getIntensity(), 0.2)

    def testResponse(self):
        self.happiness.response("win a prize")
        self.assertEqual(self.happiness.getIntensity(), 5)
        self.anger.response("meditate")
        self.assertEqual(self.anger.getIntensity(), 0)
        self.sadness.response("lose a loved one")
        self.assertEqual(self.sadness.getIntensity(), 7)
        self.fear.response("confront danger")
        self.assertEqual(self.fear.getIntensity(), 4)

    def testInfluenceByEnv(self):
        self.happiness.influenceByEnv("party")
        self.assertEqual(self.happiness.getIntensity(), 4)
        self.anger.influenceByEnv("calm")
        self.assertEqual(self.anger.getIntensity(), 1)
        self.sadness.influenceByEnv("rainy day")
        self.assertEqual(self.sadness.getIntensity(), 5)
        self.fear.influenceByEnv("threatening")
        self.assertEqual(self.fear.getIntensity(), 3)

if _name_ == '_main_':
    unittest.main()