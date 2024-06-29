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
